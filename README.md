# TTS
Text to speech using coqui's deep-learning toolkit.

## Why 🐸Coqui
TTS from 🐸Coqui has the biggest number of models for TTS compared to all of the others. It is faster and the voice sounds less robotic. 

### Tested python libraries
- **NeMo**
	- many features
	- it can be complicated to understand
	- you can change the vocoder and spectogram
	- it has many models
	- loading of model is slow
	- Source code: https://github.com/NVIDIA/NeMo/tree/main
	- Tutorials: https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/starthere/tutorials.html
	- NeMo: https://developer.nvidia.com/pt-br/nvidia-nemo
- **gTTS** 
	 - online
	 - uses Google's API
	 - robotic voice
	 - Pypi: https://pypi.org/project/gTTS/
- **pyttsx3**
	- offline
	- one line tts
	- only male voices
	- robotic voice
	- Pypi:  https://pypi.org/project/pyttsx3/
	- Docs: https://pyttsx3.readthedocs.io/en/latest/
	- Source code: https://github.com/nateshmbhat/pyttsx3
- **CoquiTTS**
	- many modelos (66 of them)
	- you can code with the models or spectograms + vocoders
	- paid models are in Coqui Studio
	- multilanguages
	- best english models:
	  - 7 - tts_models/en/ljspeech/tacotron2-DDC
	  - 12 - tts_models/en/ljspeech/vits 
	  - 13 - tts_models/en/ljspeech/vits--neon 
	  - 23 - tts_models/en/jenny/jenny
	- natural voice for the models above
	- some models have extra options like: speaker and language 
	- Website: https://coqui.ai/
	- Docs: https://tts.readthedocs.io/en/latest/index.html
	- Source code: https://github.com/coqui-ai/TTS
## Install requirements
```bash
$ pip install -r requirements.txt
```
### How to run
```bash
$ git clone https://github.com/pinguimbotsathome/TTS
$ cd TTS
$ python coTTS.py "sentence"
```
### How the code works
The text is passed as an argument when running the script. The model is loaded and passed together with the string to 🐸Coqui TTS. It then generates an audio file in the wav format that is played with playsound. After this, the audio file is deleted. 

#### Notes
❌ TTS does not work in python3.10</br>
🔢 The model in the code is number 23 - Jenny.
