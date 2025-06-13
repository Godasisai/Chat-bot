from llama_cpp import Llama

# Load the GGUF model
llm = Llama(model_path="models/llama-2-7b-chat.Q4_K_M.gguf")

# Ask a question
output = llm("Q: What is AI?\nA:", max_tokens=100)

# Print the response
print("🧠 Response from LLaMA:\n", output['choices'][0]['text'].strip())