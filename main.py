from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('Qwen/Qwen2.5-0.5B-Instruct-GGUF', allow_patterns='qwen2.5-0.5b-instruct-q4_k_m.gguf', local_dir='d:/Projects/Models/modelscope/Qwen/Qwen2.5-0.5B-Instruct-GGUF')
