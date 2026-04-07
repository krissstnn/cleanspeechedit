import subprocess
import tempfile
from pathlib import Path
from typing import List, Dict, Any

from faster_whisper import WhisperModel


def transcribe_audio(
    audio_path: str,
    model_size: str = "small",
    device: str = "cpu",
    compute_type: str = "int8",
) -> List[Dict[str, Any]]:
    """
    Transcribe audio to segments with timestamps.
    Returns list of dicts: {"start": float, "end": float, "text": str}
    """
    src = Path(audio_path)
    if not src.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    with tempfile.TemporaryDirectory(prefix="cse_audio_") as tmp_dir:
        wav_path = Path(tmp_dir) / "audio.wav"
        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            str(src),
            "-ar",
            "16000",
            "-ac",
            "1",
            str(wav_path),
        ]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            raise RuntimeError(f"ffmpeg failed: {proc.stderr.decode(errors='ignore')}")

        model = WhisperModel(model_size, device=device, compute_type=compute_type)
        segments, _ = model.transcribe(
            str(wav_path),
            beam_size=5,
            word_timestamps=True,
            vad_filter=True,
        )

        results: List[Dict[str, Any]] = []
        for seg in segments:
            results.append(
                {
                    "start": float(seg.start),
                    "end": float(seg.end),
                    "text": seg.text.strip(),
                }
            )

        return results
