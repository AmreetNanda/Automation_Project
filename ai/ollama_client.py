# from langchain_ollama import OllamaLLM

# # Create ONE global LLM instance (important)
# llm = OllamaLLM(model="codellama")

# def ask_ollama(prompt: str) -> str:
#     try:
#         response = llm(prompt)   # OllamaLLM IS callable
#         if not response or not response.strip():
#             raise RuntimeError("Ollama returned empty response")
#         return response.strip()
#     except Exception as e:
#         print(f"[AI ERROR] ask_ollama failed: {e}")
#         return ""


from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="codellama")

def ask_ollama(prompt: str) -> str:
    try:
        response = llm.invoke(prompt)   # ✅ THIS IS THE FIX
        if not response or not response.strip():
            raise RuntimeError("Ollama returned empty response")
        return response.strip()
    except Exception as e:
        print(f"[AI ERROR] ask_ollama failed: {e}")
        return ""
