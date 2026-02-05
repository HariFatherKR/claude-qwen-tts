---
name: tts-design
description: Generate speech with a designed virtual voice from text description
argument-hint: "text" --voice "voice description" [--lang Korean] [--output file.wav]
allowed-tools: [Bash, Read, Write]
---

# TTS-Design - Virtual Voice Generation

Generate speech using a designed virtual voice based on text description.

## Arguments

The user provided: $ARGUMENTS

## Instructions

1. **Check setup status**
   - Verify `~/.config/claude-qwen-tts/config.yaml` exists
   - If not, inform user to run `/tts-setup` first

2. **Parse arguments**
   - Extract text (required, in quotes)
   - Extract `--voice` or `-v` (required, voice description)
   - Extract `--lang` or `-l` (optional, default: Korean)
   - Extract `--output` or `-o` (optional, default: `./output/tts_design_{timestamp}.wav`)

3. **Voice description tips**
   - Chinese descriptions work best: "温暖、友好的年轻男性声音"
   - Korean/English also supported: "따뜻한 남성 목소리", "warm male voice"

4. **Run TTS generation**
   ```bash
   source ~/.config/claude-qwen-tts/venv/bin/activate && \
   python ~/.config/claude-qwen-tts/scripts/tts_runner.py voice_design \
     --text "TEXT_HERE" \
     --instruct "VOICE_DESCRIPTION" \
     --language "LANGUAGE" \
     --output "OUTPUT_PATH" \
     --config ~/.config/claude-qwen-tts/config.yaml
   ```

5. **Report result**
   - Show output file path
   - Show audio duration

## Supported Languages

- Korean
- Chinese
- English
- Japanese
- Cantonese

## Example Usage

```
/tts-design "안녕하세요" --voice "温暖、友好的年轻男性声音"
/tts-design "Hello world" --voice "calm female announcer" --lang English
/tts-design "오늘의 뉴스입니다" --voice "차분한 여성 아나운서" -o news.wav
```

## Error Handling

- If --voice not provided: "Please provide a voice description with --voice"
- If unsupported language: Show list of supported languages
