from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq = Groq()

def classify_with_llm(log_msg):
    prompt = f'''Classify the log message into one of the following categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you cannot figure out the category, return "Unclassified".
    Only return the category name, do not return any other text. NO PREAMBLE.
    Log Message: {log_msg}
    '''

    chat_response = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ]
    )
    
    return chat_response.choices[0].message.content.strip()

if __name__ == "__main__":  
    print("Testing LLM Classification")
    test_messages = [
        "Workflow Error: Failed to connect to the database.",
        "Deprecation Warning: The 'old_function' is deprecated and will be removed in future versions.",
        "Workflow Error: Timeout occurred while processing the request.",
        "Deprecation Warning: 'legacy_method' is no longer supported.",
        "This is a random log message that does not fit any category."
    ]

    for message in test_messages:
        print(f"Log Message: {message} | Classification: {classify_with_llm(message)}")