# File: test_ollama.py
import ollama

def test_llama3_connection():
    print("--- STARTING TEST ---")
    print("Attempting to connect to Ollama server at http://localhost:11434...")
    try:
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': 'Hi! Just a quick test.'}],
            stream=False  # Ensure we get the full response at once
        )
        
        print("\n✅ SUCCESS: Connection to Ollama was successful!")
        
        print("\n--- Full Response from Library ---")
        print(response)
        
        # Check if the expected keys are in the response
        if 'message' in response and 'content' in response['message']:
            print("\n✅ SUCCESS: Received a valid message structure.")
            print(f"LLM Response Content: \"{response['message']['content']}\"")
        else:
            print("\n❌ FAILED: The response structure from Ollama is not valid.")

    except Exception as e:
        print(f"\n❌ FAILED: An error occurred while trying to connect or get a response.")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Details: {e}")
    
    print("\n--- END OF TEST ---")

if __name__ == "__main__":
    test_llama3_connection()