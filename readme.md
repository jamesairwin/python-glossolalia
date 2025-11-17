# Python Glossolalia

## Description

Python Glossolalia is a text-to-speech generation project that uses the Eleven Labs API to convert randomly generated text (based on graphemes and sounds) into audio streams. The project plays the generated speech in real-time, simulating a stream of non-sensical speech patterns, or "glossolalia."

This project demonstrates basic usage of the Eleven Labs text-to-speech API, multi-threading, and subprocess handling in Python to stream and play audio data.

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [FFmpeg Installation](#ffmpeg-installation)

## Installation

1. Clone this repository: `git clone https://github.com/jamesairwin/python-glossolalia.git`

2. Navigate to the project directory: `cd python-glossolalia`

3. Set up a virtual environment (optional but recommended): `python -m venv venv`

4. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

5. Install the required dependencies: `pip install -r requirements.txt`

6. Set up the environment variable for the Eleven Labs API key by creating a `.env` file in the project root. Add your API key as follows: `API_KEY=your_api_key_here`

## Usage

1. Run the project: `python main.py`

2. The program will generate random strings based on graphemes and sounds and send them to the Eleven Labs API for text-to-speech conversion. The audio will be played in real-time via `ffplay`.

3. You can adjust the `similarity_boost`, `stability`, and `set_sound` variables to modify the randomness and characteristics of the generated speech.

## FFmpeg Installation

This project uses `ffplay` (part of the FFmpeg package) for audio playback. To ensure proper audio playback, follow the instructions below to install FFmpeg on your platform.

### Prerequisites
Before running this project, ensure the following are installed on your system:

- **Python 3.8+**: Download and install Python from [python.org](https://www.python.org).

- **FFmpeg**: FFmpeg is needed to run `ffplay`. Follow the installation instructions for your platform:

### Installing FFmpeg

#### Windows:

1. Download the latest FFmpeg build from [FFmpeg.org](https://ffmpeg.org/download.html).
2. Extract the downloaded zip file to a folder (e.g., `C:\ffmpeg`).
3. Add the bin directory to your system's PATH:
   - Open **System Properties** > **Advanced** > **Environment Variables**.
   - Under **System Variables**, find and edit the **Path** variable.
   - Add the full path to the bin folder (e.g., `C:\ffmpeg\bin`).
   - Click **OK** to save changes.
4. To verify the installation, open a Command Prompt and type: `ffplay -version`
   
   You should see version information.

#### macOS:

1. Install FFmpeg via Homebrew: `brew install ffmpeg`

#### Linux:

1. Install FFmpeg using your package manager: `sudo apt update | sudo apt install ffmpeg`

Now your system should be ready to play audio using `ffplay`!
