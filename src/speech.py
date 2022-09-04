import os
import sys

from gtts import gTTS
from pydub import AudioSegment
from constants import BASE_DIR, MP3_TEMP_OUT, WAV_OUT

def main():
  # Get a speech text from args
  speech_text = ' '.join(sys.argv[1:])

  # Generate speech mp3 audio
  tts = gTTS(speech_text)
  tts.save(MP3_TEMP_OUT)

  # Convert to wav
  sound = AudioSegment.from_mp3(MP3_TEMP_OUT)
  sound.export(WAV_OUT, format="wav")

  # Remove unnecessary mp3
  os.remove(MP3_TEMP_OUT)

  print(f'Successfully exported a wav file with "{speech_text}"')

if __name__ == '__main__':
  main()
