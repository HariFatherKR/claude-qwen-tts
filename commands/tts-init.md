---
name: tts-init
description: Interactive setup for TTS configuration (reference voice, output settings)
allowed-tools: [Bash, Read, Write, AskUserQuestion]
disable-model-invocation: true
---

# TTS-Init - Interactive Configuration

Set up TTS configuration through interactive questions.

## Prerequisites

Check if `/tts-setup` has been run:
```bash
test -d ~/.config/claude-qwen-tts/venv && echo "Setup complete" || echo "Setup needed"
```

If setup needed, inform user: "Please run `/tts-setup` first."

## Interactive Flow

### Question 1: Reference Voice Selection

Ask the user using AskUserQuestion:

**Question:** "Select your reference voice for TTS:"

**Options:**
- A) Use default sample (Korean male)
- B) Use default sample (Korean female)
- C) Register my own voice file

### If Option A or B selected:

Set config based on selection:
- A: `~/.config/claude-qwen-tts/samples/ko_male.wav`
- B: `~/.config/claude-qwen-tts/samples/ko_female.wav`

Read the corresponding text file for reference text.

### If Option C selected:

Ask: "Please provide the path to your voice file (5-10 seconds, WAV recommended):"

Then ask: "What is the exact transcript of the audio? (accuracy improves quality)"

### Question 2: Default Output Directory

Ask the user:

**Question:** "Select default output directory:"

**Options:**
- A) ./output (current project)
- B) ~/Documents/tts-output (home directory)
- C) Enter custom path

### Save Configuration

Write to `~/.config/claude-qwen-tts/config.yaml`:

```yaml
reference:
  audio: PATH_TO_AUDIO
  text: "TRANSCRIPT_TEXT"

output:
  default_dir: OUTPUT_DIRECTORY
  sample_rate: 24000

environment:
  venv_path: ~/.config/claude-qwen-tts/venv
  device: auto
```

```bash
cat > ~/.config/claude-qwen-tts/config.yaml << 'EOF'
reference:
  audio: "AUDIO_PATH"
  text: "REFERENCE_TEXT"

output:
  default_dir: "OUTPUT_DIR"
  sample_rate: 24000

environment:
  venv_path: ~/.config/claude-qwen-tts/venv
  device: auto
EOF
```

### Test Configuration

Run a quick test:
```bash
source ~/.config/claude-qwen-tts/venv/bin/activate && \
python ~/.config/claude-qwen-tts/scripts/tts_runner.py voice_clone \
  --text "설정 테스트입니다" \
  --output ~/.config/claude-qwen-tts/test_output.wav \
  --config ~/.config/claude-qwen-tts/config.yaml
```

## Completion Message

```
Configuration complete!

Reference voice: [selected option]
Output directory: [selected directory]

You can now use:
- /tts "text" - Generate speech
- /tts-design "text" --voice "description" - Design voice
- /tts-script script.md - Convert script to audio

Try it: /tts "안녕하세요 여러분"
```

## Reconfiguration

User can run `/tts-init` again anytime to change settings.
