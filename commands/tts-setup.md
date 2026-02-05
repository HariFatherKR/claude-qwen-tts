---
name: tts-setup
description: Set up the TTS environment (Python venv, packages, models)
allowed-tools: [Bash, Read, Write]
disable-model-invocation: true
---

# TTS-Setup - Environment Setup

Set up the Qwen TTS environment including Python virtual environment, packages, and models.

## Instructions

Execute the following steps and report progress to the user:

### Step 1: Check Python Version

```bash
python3 --version
```

- Requires Python 3.10 or higher
- If version is too low, inform user to upgrade Python

### Step 2: Create Config Directory

```bash
mkdir -p ~/.config/claude-qwen-tts/scripts
mkdir -p ~/.config/claude-qwen-tts/samples
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv ~/.config/claude-qwen-tts/venv
```

### Step 4: Install Packages

```bash
source ~/.config/claude-qwen-tts/venv/bin/activate && \
pip install --upgrade pip && \
pip install torch soundfile librosa pyyaml numpy
```

Then install qwen_tts:
```bash
source ~/.config/claude-qwen-tts/venv/bin/activate && \
pip install qwen-tts
```

### Step 5: Copy Plugin Scripts

Copy scripts from the plugin directory to config:
```bash
cp -r /path/to/plugin/scripts/* ~/.config/claude-qwen-tts/scripts/
```

The plugin scripts location can be found at the plugin installation path.

### Step 6: Copy Sample Voices

```bash
cp -r /path/to/plugin/samples/* ~/.config/claude-qwen-tts/samples/
```

### Step 7: Test Installation

```bash
source ~/.config/claude-qwen-tts/venv/bin/activate && \
python -c "import torch; import qwen_tts; print('Installation successful!')"
```

### Step 8: Detect Device

```bash
source ~/.config/claude-qwen-tts/venv/bin/activate && \
python -c "
import torch
if torch.backends.mps.is_available():
    print('Device: mps (Apple Silicon)')
elif torch.cuda.is_available():
    print('Device: cuda (NVIDIA GPU)')
else:
    print('Device: cpu (No GPU - will be slower)')
"
```

## Progress Messages

Report to user:
- "1/6 Checking Python version... Python X.X found"
- "2/6 Creating directories..."
- "3/6 Creating virtual environment..."
- "4/6 Installing packages... (this may take 2-3 minutes)"
- "5/6 Copying scripts and samples..."
- "6/6 Testing installation..."

## Completion Message

```
Setup complete!

Device detected: [mps/cuda/cpu]
Config location: ~/.config/claude-qwen-tts/

Next step: Run /tts-init to configure your voice settings.
```

## Error Handling

| Error | Solution |
|-------|----------|
| Python < 3.10 | "Please install Python 3.10 or higher" |
| pip install fails | Show error, suggest checking network |
| Disk space | "Need ~8GB free space for models" |
