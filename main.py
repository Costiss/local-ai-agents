import litellm

def main():
    response = litellm.completion(
        model="ollama/llama3",
        messages=[{"role": "user", "content": "Hello from db-ia!"}],
        api_base="http://localhost:11434"
    )
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
