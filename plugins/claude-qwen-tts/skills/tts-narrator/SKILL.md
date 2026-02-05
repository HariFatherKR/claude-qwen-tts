---
name: tts-narrator
description: Automatically generate audio narration from text or scripts. Use when user asks to "read this script", "convert to audio", "generate narration", "TTS this", "make voice file", or mentions "read aloud".
---

# TTS Narrator Skill

Automatically detect TTS requests and invoke the appropriate command.

## When to Activate

This skill activates when the user:
- Asks to "read" a script or text aloud
- Wants to convert text/script to audio
- Mentions TTS, voice synthesis, or narration
- Says "make this into audio/voice"

## Decision Logic

### For direct text input:
- Short text (< 500 chars): Use `/tts "text"`
- User wants custom voice: Use `/tts-design`

### For file input:
- Script files (.md, .txt): Use `/tts-script`
- Multiple files: Process each with `/tts-script`

## Pre-check

Before generating, verify setup:
1. Check if `~/.config/claude-qwen-tts/config.yaml` exists
2. If not, guide user to run `/tts-setup` then `/tts-init`

## Examples

**User:** "이 대본 읽어줘"
**Action:** Identify the script file in context, use `/tts-script`

**User:** "TTS로 변환해줘: 안녕하세요 여러분"
**Action:** Use `/tts "안녕하세요 여러분"`

**User:** "차분한 여성 목소리로 읽어줘"
**Action:** Use `/tts-design` with appropriate voice description

**User:** "나레이션 음성 파일 만들어줘"
**Action:** Identify text/script, use appropriate TTS command

## Output Guidance

After generation:
- Report the output file path
- Show audio duration
- Offer to play: `afplay output.wav` (macOS)
