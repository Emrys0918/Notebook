# LoRA :muscle:

## 环境准备 :zap:
```bash
conda create -n eai-lora python=3.10 -y
conda activate eai-lora

# 固定到 cu121 轮子（与驱动无关，最兼容）
pip install --index-url https://download.pytorch.org/whl/cu121 \
  torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1

# 训练/LoRA 相关依赖（与 2.5.1 兼容）
pip install -U transformers==4.46.3 accelerate==1.0.1 peft==0.13.2 \
  bitsandbytes==0.44.1 datasets==3.0.1 trl==0.11.4 einops

# xformers 建议配合 torch 2.5.x 用 0.0.27.post2（更稳）
pip install xformers==0.0.27.post2
```

## 第一次尝试（失败 :disappointed:）

由于`action_sequencing`任务的测评结果是有`error_info.json`的，可以知道那些任务规划成功，哪些任务规划失败，以及失败的原因。

本次的思路是，将`prompts`喂给超大参数量的模型（如DeepSeekv3 :whale:），得到输出，通过这些输出中正确的部分作为`groundtruth`，错误的部分作为对比学习的数据来源，以此进行微调。

微调参数如下：
|  Parameter                   | Value       |
| ---------------------------  | ----------- |
| r                            | 64          |
| lora_alpha                   | 16          |
| lora_dropout                 | 0.05        |
| epoch                        | 10          |
| per_device_train_batch_size  | 1           |
|gradient_accumulation_steps   | 8           |
|learning_rate                 | 2e-4        |
|weight_decay                  | 0.0         |
|max_grad_norm                 | 1.0         |
|logging_steps                 | 10          |
|save_total_limit              | 2           |
|max_seq_length                | 1024        |

微调之后，本地测试发现效果不好，我觉得原因可能有以下几点：
:heavy_exclamation_mark: 数据量太少，对于微调而言不痛不痒
:heavy_exclamation_mark: 数据格式不恰当 

```
accelerate launch --multi_gpu loratrain/train_qlora.py \
  --model_name_or_path /data/xjq/hf_cache/hub/models--Qwen--Qwen2.5-7B-Instruct \
  --dataset_path /data/xjq/embodied-agent-interface/src/LoRA/virtualhome/goal_interpretation/dataset/fine_tune_dataset.jsonl \
  --output_dir ./loratrain/out_smoke \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --num_train_epochs 0.5 \
  --learning_rate 2e-5 \
  --lora_r 8 \
  --lora_alpha 16
```