## make sure to have pyttsx3 installed
## if you don't, run this in terminal: pip install pyttsx3

import pyttsx3
import wave

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Set the output file name -- change to local path on YOUR computer
# make sure to add double fwd slashes \\ for windows directories
path = 'Text-to-WAV\\'

with open(path + "words.txt", 'r') as input_file:
    for line in input_file:
        text = line.strip()
        output_file = path + "wav_files\\" + f'{text}.wav'
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        print(text)

print("---finished---")


