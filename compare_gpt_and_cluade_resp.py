import ollama

def chat_with_local_gpt(prompt, model="Eomer/gpt-3.5-turbo"):
    try:
        # Get response from the model
        response = ollama.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        # Ollama response may have 'message' as attribute
        return response.message.content

    except Exception as e:
        return f"Error: {str(e)}"

# Claude

def chat_with_local_claude(prompt, model="chevalblanc/claude-3-haiku"):
    try:
        # Get response from the model
        response = ollama.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        # Ollama response may have 'message' as attribute
        return response.message.content

    except Exception as e:
        return f"Error: {str(e)}"    

if __name__ == "__main__":
    print("Connecting to local Ollama...")

    prompt = "Explain quantum computing to a 10-year-old. Please respond in English."
    print(f"\nSending prompt to gpt: {prompt}")
    gpt_model = "Eomer/gpt-3.5-turbo"
    gpt_response = chat_with_local_gpt(prompt, gpt_model)

    print("\nModel GPT response:")
    print(gpt_response)

    print(f"\nSending prompt to claude: {prompt}")
    claude_model = "chevalblanc/claude-3-haiku"
    claude_response = chat_with_local_gpt(prompt, claude_model)

    print("\nModel Claude response:")
    print(claude_response)
    # Save to Markdown
    with open("ollama_output_report.md", "w", encoding="utf-8") as f:
        f.write(f"# Ollama Model Output\n\n")
        f.write(f"**Prompt:** {prompt}\n\n")
        f.write(f"## Model: {gpt_model}\n\n{gpt_response}\n")
        f.write(f"## Model: {claude_model}\n\n{claude_response}\n")

    print("\nReport saved to ollama_output_report.md")

