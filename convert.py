# refer to install if you can't run these
from google.cloud import texttospeech
from pydub import AudioSegment
import os


# put a folder here -- make sure to add double slashes for windows directories
path = "C:\\Users\\Emily Shao\\Desktop\\Text-to-WAV\\" 

# Instantiates a client -- this will create client object that can talk to the google API
client = texttospeech.TextToSpeechClient()

# sets the type of voice that you want to hear it as
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',      # language
    name='en-US-Wavenet-C',     # type of voice "neutral"
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)


# Type of audio file you want -- I can't find if it can directly change to WAV...
file_type = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# recording mp3 files
with open(path + "words.txt", 'r') as input_file:
    for line in input_file:
        
        text = texttospeech.types.SynthesisInput(text=line)

        response = client.synthesize_speech(text, voice, file_type)

        save_path = path + f"temp_files\\{line}.mp3"

        with open(save_path, 'wb') as out_file:
            out_file.write(response.audio_content)
            print(f'Finished writing {line}')


directory = path + "temp_files"
output = path + "wav_files"
 
# iterate over files in directory
for filename in os.scandir(directory):
    if filename.is_file():
        sound = AudioSegment.from_mp3(directory + "\\" + filename)
        sound.export(output + filename + ".wav", format="wav")

