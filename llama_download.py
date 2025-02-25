from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_path = "TheBloke/Llama-2-13B-chat-GGML"
model_basename = "llama-2-13b-chat.ggmlv3.q5_1.bin" 
model_path = hf_hub_download(repo_id=model_path, filename=model_basename)