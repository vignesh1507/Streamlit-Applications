import streamlit as st
import pandas as pd
import json
import xml.etree.ElementTree as ET
from io import StringIO
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_groq
import re

# Function to extract specific links from the DOM content
def extract_links(dom_content, keyword):
    links = re.findall(r'href=[\'"]?([^\'" >]+)', dom_content)
    if keyword:
        links = [link for link in links if keyword in link]
    return links

# Streamlit UI
st.title("AI WebScraper")
url = st.text_input("Enter Website URL:")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Ensure all content is captured
        if len(cleaned_content) == 0:
            st.error("Failed to scrape content. Please check the URL or try again.")

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    # Extract links if requested
    if st.checkbox("Extract specific links from the website"):
        link_keyword = st.text_input("Enter a keyword to filter links")
        links = extract_links(st.session_state.dom_content, link_keyword)
        if links:
            st.subheader("Extracted Links")
            st.write(links)
            links_csv = pd.DataFrame(links, columns=["Links"]).to_csv(index=False).encode('utf-8')
            st.download_button("Download Links CSV", links_csv, "extracted_links.csv", "text/csv")
        else:
            st.write("No matching links found.")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Groq
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_groq(dom_chunks, parse_description)

            # Attempt to parse the table string into a DataFrame
            try:
                if isinstance(parsed_result, str):
                    df_parsed = pd.read_csv(StringIO(parsed_result), sep="|")
                    df_parsed.columns = df_parsed.columns.str.strip()

                    # Display parsed content in a table (always shown)
                    st.subheader("Parsed Content (Table)")
                    st.dataframe(df_parsed)

                    # Keep parsed content in session state for persistence
                    st.session_state.parsed_content = df_parsed

                    # CSV Download
                    csv = df_parsed.to_csv(index=False).encode('utf-8')
                    st.download_button("Download CSV", csv, "parsed_content.csv", "text/csv")

                    # JSON Download
                    json_data = df_parsed.to_json(orient="records", indent=4).encode('utf-8')
                    st.download_button("Download JSON", json_data, "parsed_content.json", "application/json")

                    # XML Download
                    root = ET.Element("ParsedContent")
                    for _, row in df_parsed.iterrows():
                        entry = ET.SubElement(root, "Entry")
                        for key, value in row.items():
                            ET.SubElement(entry, key).text = str(value)
                    xml_data = ET.tostring(root, encoding='utf-8').decode('utf-8')
                    st.download_button("Download XML", xml_data, "parsed_content.xml", "application/xml")

                else:
                    st.error("Parsed result is not a string or not in expected format.")
            except Exception as e:
                st.error(f"Error parsing the result: {e}")

    # Ensure parsed content is visible after downloading
    if "parsed_content" in st.session_state:
        st.subheader("Parsed Content")
        st.dataframe(st.session_state.parsed_content)
else:
    st.write("Waiting on file upload...")
