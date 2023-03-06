# LLaMa Inference

## Getting Started

1. Create a new Conda environment:

```bash
conda create --name llama-inference python=3.10
conda activate llama-inference
```

2. Install the package:

```bash
git clone git@github.com:codekansas/llama-inference.git
cd llama-inference

# Installs with the nightly version of PyTorch, on CPU.
pip install --pre --extra-index-url https://download.pytorch.org/whl/nightly/cpu -e '.[dev]'
# Installs with the nightly version of PyTorch, on GPU.
pip install --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu117 -e '.[dev]'
```

3. Set the environment variable for the root directory where the weights were downloaded from:

```bash
export LLAMA_WEIGHTS_ROOT=/path/to/root/dir
```

