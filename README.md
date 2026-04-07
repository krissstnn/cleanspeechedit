# CleanSpeechEdit

Небольшое GUI на CustomTkinter: выбирает XML и аудио, три режима очистки (Default/Soft/Aggressive) и кнопка транскрипции (Whisper).
Сейчас кнопка генерирует `*.transcript.json` c таймкодами.

## Запуск
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python clean_speech_edit.py
```

Требования:
- установленный `ffmpeg` в PATH
- интернет для первой загрузки модели Whisper (по умолчанию `small`, CPU)

Вывод транскрипта:
- выбрать аудио и нажать «Генерировать»
- JSON появится рядом с аудио: `имя_файла.transcript.json`
