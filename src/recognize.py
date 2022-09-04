import speech_recognition as sr
import sys

from constants import BASE_DIR, WAV_OUT

def main():
    mode = None

    # Get mode from args
    if len(sys.argv) > 2:
        raise Exception('Too many args. (pass "mic" or don\'t pass to use "/audios/speech.wav" file)')
    elif len(sys.argv) == 2:
        mode = sys.argv[1]

    recognize_result = recognize(mode)

    print(recognize_result)

def recognize(mode):
    text = None
    audio_src = sr.Microphone() if mode == 'mic' else sr.AudioFile(WAV_OUT)

    with audio_src as audio_file:
        # Initialize a Recognizer
        r = sr.Recognizer()
        # Remove noise
        # r.adjust_for_ambient_noise(audio_file, duration=10)
        # Convert audio source to a recognizable object
        recognizable = r.record(audio_file, duration=10)
        text = r.recognize_sphinx(recognizable)

    return text


if __name__ == '__main__':
    main()
