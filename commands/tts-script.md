---
name: tts-script
description: Convert a script file (markdown/text) to audio narration
argument-hint: <script.md> [--output file.wav] [--pause 0.8] [--speed 1.0]
allowed-tools: [Bash, Read, Write]
---

# TTS-Script - Script to Audio Conversion

Convert a markdown or text script file to audio narration.

## Arguments

The user provided: $ARGUMENTS

## Instructions

1. **Check setup status**
   - Verify `~/.config/claude-qwen-tts/config.yaml` exists
   - If not, inform user to run `/tts-setup` and `/tts-init` first

2. **Parse arguments**
   - Extract script path (required)
   - Extract `--output` or `-o` (optional, default: `{script_name}.wav`)
   - Extract `--pause` (optional, silence between paragraphs, default: 0.8s)
   - Extract `--speed` (optional, playback speed, default: 1.0)

3. **Validate script file**
   - Check file exists
   - Supported formats: `.md`, `.txt`
   - Read and preview first few lines

4. **Run TTS generation**
   ```bash
   source ~/.config/claude-qwen-tts/venv/bin/activate && \
   python ~/.config/claude-qwen-tts/scripts/tts_runner.py script_to_audio \
     --script "SCRIPT_PATH" \
     --output "OUTPUT_PATH" \
     --pause PAUSE_SECONDS \
     --speed SPEED_RATIO \
     --config ~/.config/claude-qwen-tts/config.yaml
   ```

5. **Report result**
   - Show output file path
   - Show total audio duration
   - Show number of processed paragraphs

## Processing Logic

- Markdown headers (#, ##) are removed
- Horizontal rules (---) are removed
- Text is split by paragraphs
- Each paragraph is generated separately
- Silence is inserted between paragraphs
- All audio is merged into final output

## Example Usage

```
/tts-script scripts/episode01.md
/tts-script SCRIPT.md -o narration.wav
/tts-script intro.txt --pause 1.0 --speed 0.9
```

## Error Handling

- If file not found: "Script file not found: {path}"
- If unsupported format: "Supported formats: .md, .txt"
- If empty script: "Script file is empty"
