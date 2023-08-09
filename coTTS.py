#! /usr/bin/env python3

# CoquiTTS 
from TTS.api import TTS

# import
import sys
import playsound as ps
import os

# receives text and model
def coqui(text, model):
    tts = TTS(model)
    # path to file
    path =os.path.abspath("output.wav")
    #path = "/home/gvalkyr/Documents/testes/tts-2/coqui/output.wav"
    
    # transforms to audio and saves in wav format
    wav  = tts.tts_to_file(text=text,
                       speed=2,
                       file_path=path)
    
    # plays audio
    ps.playsound(sound=path)
    # deletes the file
    delete_file(path)

# deletes file
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("no file")

# tts main func
def tts(text):
    ## Models - english only
    ## 7 - 12 - 13 - 23(jenny)
    n = 23
    # loads model
    model = TTS.list_models()[n]
    # coqui
    coqui(text,model)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python coTTS.py <string_argument>")
    else:
        input_string = sys.argv[1]
        tts(input_string)