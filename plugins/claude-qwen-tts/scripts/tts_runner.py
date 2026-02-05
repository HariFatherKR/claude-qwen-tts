#!/usr/bin/env python3
"""
Qwen3-TTS Runner for Claude Code Plugin
Unified CLI for voice clone, voice design, and script-to-audio conversion.
"""

import argparse
import sys
import time
from pathlib import Path
from typing import Optional, Tuple, List
import yaml

import torch
import soundfile as sf
import numpy as np


class Qwen3TTSRunner:
    """Qwen3-TTS unified runner"""

    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.device = self._get_device()
        self.dtype = torch.float32

        self._model_clone = None
        self._model_design = None

    def _load_config(self, config_path: Optional[str]) -> dict:
        """Load configuration file"""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)

        # Default config
        return {
            'reference': {
                'audio': None,
                'text': None
            },
            'output': {
                'default_dir': 'output',
                'sample_rate': 24000
            },
            'environment': {
                'device': 'auto'
            }
        }

    def _get_device(self) -> str:
        """Auto-detect device"""
        device_config = self.config.get('environment', {}).get('device', 'auto')

        if device_config != 'auto':
            return device_config

        if torch.backends.mps.is_available():
            return "mps"
        elif torch.cuda.is_available():
            return "cuda:0"
        return "cpu"

    @property
    def model_clone(self):
        """Voice Clone model (lazy loading)"""
        if self._model_clone is None:
            print(f"Loading Voice Clone model on {self.device}...")
            from qwen_tts import Qwen3TTSModel
            self._model_clone = Qwen3TTSModel.from_pretrained(
                "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
                device_map=self.device,
                dtype=self.dtype,
            )
            print("Model loaded.")
        return self._model_clone

    @property
    def model_design(self):
        """Voice Design model (lazy loading)"""
        if self._model_design is None:
            print(f"Loading Voice Design model on {self.device}...")
            from qwen_tts import Qwen3TTSModel
            self._model_design = Qwen3TTSModel.from_pretrained(
                "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign",
                device_map=self.device,
                dtype=self.dtype,
            )
            print("Model loaded.")
        return self._model_design

    def voice_clone(
        self,
        text: str,
        ref_audio: Optional[str] = None,
        ref_text: Optional[str] = None,
        output_path: Optional[str] = None
    ) -> Tuple[str, float]:
        """
        Voice cloning TTS

        Args:
            text: Text to generate
            ref_audio: Reference audio path
            ref_text: Reference text
            output_path: Output file path

        Returns:
            (output_path, duration_seconds)
        """
        # Apply defaults from config
        if ref_audio is None:
            ref_audio = self.config.get('reference', {}).get('audio')
        if ref_text is None:
            ref_text = self.config.get('reference', {}).get('text')

        if ref_audio is None or ref_text is None:
            raise ValueError("Reference audio and text are required. Run /tts-init first.")

        # Expand home directory
        ref_audio = str(Path(ref_audio).expanduser())

        if output_path is None:
            output_dir = Path(self.config.get('output', {}).get('default_dir', 'output'))
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = str(output_dir / f"tts_{int(time.time())}.wav")

        # Generate
        start_time = time.time()
        wavs, sr = self.model_clone.generate_voice_clone(
            text=text,
            ref_audio=ref_audio,
            ref_text=ref_text,
        )
        elapsed = time.time() - start_time

        # Save
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        sf.write(output_path, wavs[0], sr)

        duration = len(wavs[0]) / sr
        print(f"Generated: {output_path} ({duration:.1f}s in {elapsed:.1f}s)")

        return output_path, duration

    def voice_design(
        self,
        text: str,
        language: str = "Korean",
        instruct: str = "温暖、友好的年轻男性声音",
        output_path: Optional[str] = None
    ) -> Tuple[str, float]:
        """
        Voice design TTS

        Args:
            text: Text to generate
            language: Language (Chinese, English, Japanese, Korean, Cantonese)
            instruct: Voice description
            output_path: Output file path

        Returns:
            (output_path, duration_seconds)
        """
        if output_path is None:
            output_dir = Path(self.config.get('output', {}).get('default_dir', 'output'))
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = str(output_dir / f"tts_design_{int(time.time())}.wav")

        # Generate
        start_time = time.time()
        wavs, sr = self.model_design.generate_voice_design(
            text=text,
            language=language,
            instruct=instruct,
        )
        elapsed = time.time() - start_time

        # Save
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        sf.write(output_path, wavs[0], sr)

        duration = len(wavs[0]) / sr
        print(f"Generated: {output_path} ({duration:.1f}s in {elapsed:.1f}s)")

        return output_path, duration

    def script_to_audio(
        self,
        script_path: str,
        output_path: Optional[str] = None,
        pause_duration: float = 0.8,
        speed: float = 1.0
    ) -> Tuple[str, float]:
        """
        Convert script file to audio

        Args:
            script_path: Script file path (.md, .txt)
            output_path: Output file path
            pause_duration: Silence between paragraphs (seconds)
            speed: Playback speed ratio

        Returns:
            (output_path, total_duration_seconds)
        """
        # Read script
        script_path = Path(script_path).expanduser()
        if not script_path.exists():
            raise FileNotFoundError(f"Script not found: {script_path}")

        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean markdown
        lines = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('#'):
                continue
            if line.startswith('---'):
                continue
            if line:
                lines.append(line)

        text = ' '.join(lines)

        if not text:
            raise ValueError("Script file is empty after processing")

        # Set output path
        if output_path is None:
            output_dir = Path(self.config.get('output', {}).get('default_dir', 'output'))
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = str(output_dir / f"{script_path.stem}.wav")

        # Split into paragraphs
        paragraphs = self._split_text(text)
        print(f"Processing {len(paragraphs)} paragraphs...")

        all_audio = []
        sample_rate = 24000
        silence = np.zeros(int(pause_duration * sample_rate))

        for i, para in enumerate(paragraphs):
            print(f"  [{i+1}/{len(paragraphs)}] {para[:30]}...")

            wavs, sr = self.model_clone.generate_voice_clone(
                text=para,
                ref_audio=str(Path(self.config['reference']['audio']).expanduser()),
                ref_text=self.config['reference']['text'],
            )

            all_audio.append(wavs[0])
            if i < len(paragraphs) - 1:
                all_audio.append(silence)

        # Merge
        combined = np.concatenate(all_audio)

        # Apply speed adjustment if needed
        if speed != 1.0:
            try:
                import librosa
                combined = librosa.effects.time_stretch(combined, rate=1.0/speed)
            except ImportError:
                print("Warning: librosa not installed, speed adjustment skipped")

        # Save
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        sf.write(output_path, combined, sample_rate)

        total_duration = len(combined) / sample_rate
        print(f"Generated: {output_path} ({total_duration:.1f}s, {len(paragraphs)} paragraphs)")

        return output_path, total_duration

    def _split_text(self, text: str, max_chars: int = 300) -> List[str]:
        """Split text into sentences"""
        import re

        sentences = re.split(r'(?<=[.!?。！？])\s+', text)

        paragraphs = []
        current = []
        current_len = 0

        for sent in sentences:
            if current_len + len(sent) > max_chars and current:
                paragraphs.append(' '.join(current))
                current = []
                current_len = 0
            current.append(sent)
            current_len += len(sent)

        if current:
            paragraphs.append(' '.join(current))

        return paragraphs


def main():
    parser = argparse.ArgumentParser(description='Qwen3-TTS Runner')
    parser.add_argument('command', choices=['voice_clone', 'voice_design', 'script_to_audio'],
                        help='Command to execute')
    parser.add_argument('--text', '-t', help='Text to generate')
    parser.add_argument('--ref-audio', '-ra', help='Reference audio path')
    parser.add_argument('--ref-text', '-rt', help='Reference text')
    parser.add_argument('--script', '-s', help='Script file path')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--language', '-l', default='Korean', help='Voice Design language')
    parser.add_argument('--instruct', '-i', default='温暖、友好的年轻男性声音',
                        help='Voice Design description')
    parser.add_argument('--pause', type=float, default=0.8, help='Pause between paragraphs')
    parser.add_argument('--speed', type=float, default=1.0, help='Playback speed')
    parser.add_argument('--config', '-c', help='Config file path')

    args = parser.parse_args()

    runner = Qwen3TTSRunner(args.config)

    if args.command == 'voice_clone':
        if not args.text:
            parser.error('voice_clone requires --text')
        runner.voice_clone(args.text, args.ref_audio, args.ref_text, args.output)

    elif args.command == 'voice_design':
        if not args.text:
            parser.error('voice_design requires --text')
        runner.voice_design(args.text, args.language, args.instruct, args.output)

    elif args.command == 'script_to_audio':
        if not args.script:
            parser.error('script_to_audio requires --script')
        runner.script_to_audio(args.script, args.output, args.pause, args.speed)


if __name__ == '__main__':
    main()
