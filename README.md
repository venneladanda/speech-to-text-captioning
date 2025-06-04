# Real-Time Speech-to-Text Captioning App

This Python application converts speech into real-time text captions using the microphone. It is designed for accessibility to help deaf or hard-of-hearing users.

## Features
- Captures live speech through your microphone
- Converts it to text in real time
- Displays captions in a clean GUI using Tkinter

## Installation

1. Install Python 3.x
2. Install dependencies:

```bash
pip install -r requirements.txt
```

> For Windows: If `pyaudio` fails, run:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

## Usage

```bash
python app.py
```

## Dependencies
- speechrecognition
- pyaudio
- tkinter (built into Python)

## License
MIT
