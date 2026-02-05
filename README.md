# 🎙️ claude-qwen-tts

Qwen3-TTS based high-quality Korean/multilingual text-to-speech plugin for Claude Code.

[한국어 문서](README_KO.md)

## ✨ Features

- **Voice Clone** - Clone voice from reference audio
- **Voice Design** - Create virtual voices from text descriptions
- **Script to Audio** - Convert markdown/text scripts to narration
- **Auto Detection** - Claude automatically recognizes TTS requests

## 🚀 Quick Start

### 1. Install Plugin

```
/install claude-qwen-tts@HariFatherKR
```

### 2. Setup Environment

```
/tts-setup
```

This will:
- Create Python virtual environment
- Install required packages (torch, qwen-tts, etc.)
- Download TTS models (~4-6GB)

### 3. Initialize Configuration

```
/tts-init
```

Interactive setup for:
- Reference voice selection (default samples or your own)
- Output directory configuration

### 4. Generate Speech!

```
/tts "Hello, this is a test"
```

## 📋 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/tts` | Text to speech (voice clone) | `/tts "안녕하세요"` |
| `/tts-design` | Generate with designed voice | `/tts-design "Hello" --voice "calm female"` |
| `/tts-script` | Convert script file to audio | `/tts-script script.md` |
| `/tts-setup` | Setup environment | `/tts-setup` |
| `/tts-init` | Interactive configuration | `/tts-init` |

### /tts Options

```
/tts "text" [--output file.wav] [--voice ref.wav]
```

- `--output`, `-o`: Output file path
- `--voice`, `-v`: Alternative reference voice

### /tts-design Options

```
/tts-design "text" --voice "description" [--lang Korean] [--output file.wav]
```

- `--voice`, `-v`: Voice description (Chinese recommended for best results)
- `--lang`, `-l`: Language (Korean, English, Chinese, Japanese, Cantonese)
- `--output`, `-o`: Output file path

### /tts-script Options

```
/tts-script script.md [--output file.wav] [--pause 0.8] [--speed 1.0]
```

- `--output`, `-o`: Output file path
- `--pause`: Silence between paragraphs (seconds)
- `--speed`: Playback speed ratio

## 🎤 Sample Voices

Default sample voices are included (CC0 license):
- `ko_male.wav` - Korean male voice
- `ko_female.wav` - Korean female voice

To use your own voice:
1. Prepare a 5-10 second WAV recording
2. Run `/tts-init` and select "Register my own voice"

## ⚙️ Requirements

- **Python**: 3.10+
- **Disk Space**: ~8GB (for models)
- **GPU**: Recommended (Apple Silicon MPS or NVIDIA CUDA)
- **CPU**: Supported but slower

## 🔧 Supported Devices

| Device | Support | Notes |
|--------|---------|-------|
| Apple Silicon (MPS) | ✅ | Recommended for Mac |
| NVIDIA GPU (CUDA) | ✅ | Recommended |
| CPU | ✅ | Slower performance |

## 📁 File Structure

```
~/.config/claude-qwen-tts/
├── venv/              # Python virtual environment
├── scripts/           # TTS runner scripts
├── samples/           # Sample voice files
└── config.yaml        # User configuration
```

## 🌐 Supported Languages

- Korean (한국어)
- English
- Chinese (中文)
- Japanese (日本語)
- Cantonese (粤语)

## 📄 License

MIT License

## 🙏 Credits

- [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Base TTS model by Alibaba
- [Claude Code](https://claude.ai/code) - AI coding assistant by Anthropic

## 🐛 Issues & Contributions

Please report issues at [GitHub Issues](https://github.com/HariFatherKR/claude-qwen-tts/issues)

Pull requests are welcome!
