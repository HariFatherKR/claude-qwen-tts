# 🎙️ claude-qwen-tts

Qwen3-TTS 기반 고품질 한국어/다국어 음성 합성 Claude Code 플러그인

## ✨ 주요 기능

- **Voice Clone** - 레퍼런스 음성을 복제하여 TTS 생성
- **Voice Design** - 텍스트 설명으로 가상 목소리 생성
- **Script to Audio** - 마크다운/텍스트 대본을 나레이션으로 변환
- **자동 인식** - Claude가 TTS 요청을 자동으로 인식

## 🚀 빠른 시작

### 1. 플러그인 설치

```
/install claude-qwen-tts@HariFatherKR
```

### 2. 환경 구축

```
/tts-setup
```

자동으로 진행되는 작업:
- Python 가상환경 생성
- 필요 패키지 설치 (torch, qwen-tts 등)
- TTS 모델 다운로드 (~4-6GB)

### 3. 초기 설정

```
/tts-init
```

대화형으로 설정:
- 레퍼런스 음성 선택 (기본 샘플 또는 내 목소리)
- 출력 폴더 설정

### 4. 음성 생성!

```
/tts "안녕하세요 여러분"
```

## 📋 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `/tts` | 텍스트 → 음성 (voice clone) | `/tts "안녕하세요"` |
| `/tts-design` | 가상 목소리로 생성 | `/tts-design "안녕" --voice "따뜻한 남성"` |
| `/tts-script` | 대본 파일 → 음성 | `/tts-script script.md` |
| `/tts-setup` | 환경 구축 | `/tts-setup` |
| `/tts-init` | 대화형 설정 | `/tts-init` |

### /tts 옵션

```
/tts "텍스트" [--output file.wav] [--voice ref.wav]
```

- `--output`, `-o`: 출력 파일 경로
- `--voice`, `-v`: 다른 레퍼런스 음성 사용

### /tts-design 옵션

```
/tts-design "텍스트" --voice "목소리 설명" [--lang Korean] [--output file.wav]
```

- `--voice`, `-v`: 목소리 설명 (중국어로 작성 시 품질 향상)
- `--lang`, `-l`: 언어 (Korean, English, Chinese, Japanese, Cantonese)
- `--output`, `-o`: 출력 파일 경로

### /tts-script 옵션

```
/tts-script script.md [--output file.wav] [--pause 0.8] [--speed 1.0]
```

- `--output`, `-o`: 출력 파일 경로
- `--pause`: 문단 사이 묵음 (초)
- `--speed`: 재생 속도 배율

## 🎤 샘플 음성

기본 제공 샘플 (CC0 라이선스):
- `ko_male.wav` - 한국어 남성 목소리
- `ko_female.wav` - 한국어 여성 목소리

본인 목소리 사용하기:
1. 5-10초 분량의 WAV 파일 녹음
2. `/tts-init` 실행 후 "내 음성 파일 등록" 선택

## ⚙️ 요구사항

- **Python**: 3.10 이상
- **디스크 공간**: 약 8GB (모델용)
- **GPU**: 권장 (Apple Silicon MPS 또는 NVIDIA CUDA)
- **CPU**: 지원하지만 느림

## 🔧 지원 디바이스

| 디바이스 | 지원 | 비고 |
|----------|------|------|
| Apple Silicon (MPS) | ✅ | Mac 사용자 권장 |
| NVIDIA GPU (CUDA) | ✅ | 권장 |
| CPU | ✅ | 느린 성능 |

## 📁 파일 구조

```
~/.config/claude-qwen-tts/
├── venv/              # Python 가상환경
├── scripts/           # TTS 실행 스크립트
├── samples/           # 샘플 음성 파일
└── config.yaml        # 사용자 설정
```

## 🌐 지원 언어

- 한국어 (Korean)
- 영어 (English)
- 중국어 (Chinese)
- 일본어 (Japanese)
- 광동어 (Cantonese)

## 📄 라이선스

MIT License

## 🙏 크레딧

- [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Alibaba의 TTS 모델
- [Claude Code](https://claude.ai/code) - Anthropic의 AI 코딩 어시스턴트

## 🐛 이슈 & 기여

이슈는 [GitHub Issues](https://github.com/HariFatherKR/claude-qwen-tts/issues)에 등록해주세요.

Pull Request 환영합니다!
