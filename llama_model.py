from llama_cpp import Llama

class llama_model():
    def llama_model(self, prompt):
        model_path = "C:/Users/FAISAL/.cache/huggingface/hub/models--TheBloke--Llama-2-13B-chat-GGML/snapshots/3140827b4dfcb6b562cd87ee3d7f07109b014dd0/llama-2-13b-chat.ggmlv3.q5_1.bin"
        lcpp_llm = Llama(model_path=model_path, n_threads=4, n_batch=1)

        try:
            print("Starting inference...")
            response = lcpp_llm(prompt=prompt, max_tokens=50, temperature=0.5)
            print("Inference complete.")
            # print(response["choices"][0]["text"])
            return response["choices"][0]["text"]
        
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return None