---
name: tts
description: Generate speech from text using voice cloning. Requires /tts-setup and /tts-init first.
argument-hint: "text" [--output file.wav] [--voice ref.wav]
allowed-tools: [Bash, Read, Write]
---

# TTS - Text to Speech (Voice Clone)

Generate speech from text using a reference voice.

## Arguments

The user provided: $ARGUMENTS

## Instructions

1. **Check setup status**
   - Verify `~/.config/claude-qwen-tts/config.yaml` exists
   - If not, inform user to run `/tts-setup` and `/tts-init` first

2. **Parse arguments**
   - Extract text (required, in quotes)
   - Extract `--output` or `-o` (optional, default: `./output/tts_{timestamp}.wav`)
   - Extract `--voice` or `-v` (optional, use config default)

3. **Run TTS generation**
   ```bash
   source ~/.config/claude-qwen-tts/venv/bin/activate && \
   python ~/.config/claude-qwen-tts/scripts/tts_runner.py voice_clone \
     --text "TEXT_HERE" \
     --output "OUTPUT_PATH" \
     --config ~/.config/claude-qwen-tts/config.yaml
   ```

4. **Report result**
   - Show output file path
   - Show audio duration
   - Suggest playback command: `afplay OUTPUT_PATH`

## Example Usage

```
/tts "안녕하세요 여러분"
/tts "오늘의 주제입니다" -o intro.wav
/tts "다른 목소리로" -v ~/other_voice.wav
```

## Error Handling

- If config not found: "Run `/tts-setup` first to set up the environment"
- If reference voice not set: "Run `/tts-init` to configure your voice"
- If generation fails: Show error message and suggest troubleshooting
