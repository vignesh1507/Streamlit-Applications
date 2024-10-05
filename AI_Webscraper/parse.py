from groq import Groq
import os

# Prompt Template like LangChain's ChatPromptTemplate
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. *Extract Information:* Only extract the information that directly matches the provided description: {parse_description}. "
    "2. *No Extra Content:* Do not include any additional text, comments, or explanations in your response. "
    "3. *Empty Response:* If no information matches the description, return an empty string ('')."
    "4. *Direct Data Only:* Your output should contain only the data that is explicitly requested, with no other text."
)

def extract_events(prompt):
    groq_api_key = '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'  # Input your own groq api key.
    
    client = Groq(api_key=groq_api_key)

    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    # Gather response
    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""
    
    return result


def parse_with_groq(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        # Create prompt using the template
        prompt = template.format(dom_content=chunk, parse_description=parse_description)
        
        # Call extract_events with the constructed prompt
        response = extract_events(prompt)
        
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        
        # Append response to the result
        parsed_results.append(response)
    
    # Return the concatenated parsed results
    return "\n".join(parsed_results)
