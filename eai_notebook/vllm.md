# vllm配置指南

## 详细步骤

### 1.新建环境（建议 3.10）

```bash
conda create -n eai-vllm python=3.10 -y
conda activate eai-vllm
```

### 2. 安装 PyTorch（按 nvidia-smi 的 CUDA 版本二选一）

```bash
pip install "torch>=2.4,<2.6" --index-url https://download.pytorch.org/whl/cu124
```

### 3.安装 vLLM + 依赖

```bash
pip install "vllm==0.6.3.post1" "transformers==4.46.3" "accelerate==1.0.1" sentencepiece
```

### 4.配置 tokens

```bash
export HUGGING_FACE_HUB_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
source ~/.bashrc
```

### 5.启动

```bash
vllm serve Qwen/Qwen2.5-7B-Instruct\ --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.92 --max-model-len 8192
```

### 6.测试
``` 
# client_test.py
from openai import OpenAI
cli = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key="EMPTY")

resp = cli.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[{"role":"user","content":"who are you?"}],
    temperature=0.2, max_tokens=8192
)
print(resp.choices[0].message.content)
```

