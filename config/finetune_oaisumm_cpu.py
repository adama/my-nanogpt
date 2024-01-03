import time

out_dir = 'out-shakespeare-small-cpu'
eval_interval = 20
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'oaisum-cpu'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'oai_summarization'
init_from = 'gpt2'

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 16
gradient_accumulation_steps = 2
max_iters = 100

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False

# cpu-specific stuff
device = "cpu"

# torch.compile uses CUDA when it's available
# but set `CUDA_VISIBLE_DEVICES=` and it will use the CPU
# in the case of CPU only, it looks like disabling the compiler
# doesn't help very much, so up to you if you want to disable
compile = True