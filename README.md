# python_sphinx_sample
Voice recognition program sample.

# Useful links

## Free audio files
- https://www.voiptroubleshooter.com/open_speech/american.html

# Scripts
## speech.py
**Description**
Generates a wav file which contains a speech.
Just for testing purpose.

**Usage**
1. Run `mkdir /path/to/python_sphinx_sample/audios`
1. Run `python speech.py "some speech"`
1. It generates a wav file which contains a speech at `WAV_OUT` in constants.py.

## recognize.py
**Description**
Generates a wav file which contains a speech.
Just for testing purpose.

**Usage**
1. Run `python recognize.py <mode>`
  - Set mode as `mic` for using microphone connected to your PC.
1. It recognizes the speech in the wav file at `WAV_OUT` in constants.py and prints the text of the speech.

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
