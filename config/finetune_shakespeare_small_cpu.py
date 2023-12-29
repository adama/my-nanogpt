import time

out_dir = 'out-shakespeare-small-cpu'
eval_interval = 20
# seems like saving a checkpoint more than 10x iter time on CPU with compilation on
# TODO maybe it's because it does the eval/doesn't reset the timers when checkpointing
# saving checkpoint to out-shakespeare-small-cpu
# iter 5: loss 3.6509, time 808662.34ms, mfu 0.01%
# iter 6: loss 3.5466, time 58659.21ms, mfu 0.03%
# iter 7: loss 3.5728, time 58616.83ms, mfu 0.04%
# even worse uncompiled
# saving checkpoint to out-shakespeare-small-cpu
# iter 20: loss 3.5700, time 901903.61ms, mfu 0.14%
# iter 21: loss 3.3917, time 58142.60ms, mfu 0.14%
# iter 22: loss 3.3074, time 58025.57ms, mfu 0.14%
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'shakespeare-small'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'shakespeare'
init_from = 'gpt2' # this is the largest GPT-2 model

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
# in the case of CPU only, it doesn't look like disabling the compiler
# doesn't help very much, so up to you if you want to disable
compile = False