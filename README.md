# AI Chat Bot Powered by OpenAI API

This project is an implementation of an AI chatbot that utilizes OpenAI's API to enable natural and responsive interactions.

## Features

- **Speech Recognition**: Uses the `speech_recognition` library to convert speech into text.
- **Natural Language Processing**: Integrates with the OpenAI API to understand and respond to user input.
- **Text-to-Speech**: Uses the `pyttsx3` library to convert text responses into spoken audio.

## Prerequisites

Before running this project, make sure you have the following libraries installed:

- `pyaudio`
- `speech_recognition`
- `pyttsx3`
- `openai`

Install them using pip:

```bash
pip install pyaudio speechrecognition pyttsx3 openai
```

## Usage

1. **OpenAI API Configuration**: Make sure you have a valid OpenAI API key and have configured it in the code.
2. **Run the Chatbot**: Execute the main script to start interacting with the AI.

## Project Structure

- `ai.py`: The main script that controls the chatbot workflow.
- `memory.py`: Module to manage conversation memory or context.
- `record.py`: Handles user voice input recording.
- `tts.py`: Converts text responses into speech.
- `wav.py`: Processes audio files.
- `tes.html`: (Optional) Basic HTML interface for interacting with the chatbot.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
