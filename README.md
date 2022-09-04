# python_sphinx_sample
Voice recognition program sample.

# Useful links

## Free audio files
- https://www.voiptroubleshooter.com/open_speech/american.html

# Scripts
## recognize.py
**Description**
Generates a wav file which contains a speech.
Just for testing purpose.

**Usage**
1. Run `python recognize.py "some speech"`
1. It generates a wav file which contains a speech at "/audios/speech.wav".

## speech.py
**Description**
Generates a wav file which contains a speech.
Just for testing purpose.

**Usage**
1. Run `mkdir /path/to/python_sphinx_sample/audios`
1. Run `python speech.py`
1. It recognizes the speech in the wav file at "/audios/speech.wav" and prints the text of the speech.

## install_deps.sh
**Description**
Installs all dependencies.

**Usage**
1. Run `chmod +x ./install_deps.sh`
1. Run `sudo ./install_deps.sh`

## install_py_mod.sh
**Description**
Install necessary pip modules.

**Usage**
1. Run `chmod +x ./install_py_mod.sh`
1. Run `./install_py_mod.sh`
