import os
import csv
from pydub import AudioSegment
import speech_recognition as sr

# Set paths
mp3_dir = ""       # Directory containing MP3 files
wav_dir = ""       # Directory to save converted WAV files
metadata_file = "" # Directory to save metadata.csv files
file_limit = 50       # Set the maximum number of files to process

# Ensure WAV output directory exists
os.makedirs(wav_dir, exist_ok=True)

# Initialize the recognizer for transcription
recognizer = sr.Recognizer()

# Open CSV file for writing
with open(metadata_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter="|")
    
    # Loop through MP3 files and process up to the file limit
    for i, mp3_filename in enumerate(os.listdir(mp3_dir), start=1):
        if i > file_limit:
            break
        if mp3_filename.endswith(".mp3"):
            # Define paths
            mp3_path = os.path.join(mp3_dir, mp3_filename)
            wav_filename = f"audio_{i:04d}.wav"
            wav_path = os.path.join(wav_dir, wav_filename)
            
            # Convert MP3 to WAV
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")
            
            # Transcribe the WAV file
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data, language="es-MX")
                except sr.UnknownValueError:
                    text = "[Unintelligible]"  # Fallback for non-recognizable audio
                except sr.RequestError:
                    print("API request error.")
                    text = "[Error]"
            
            # Write metadata entry
            writer.writerow([wav_path, text])
            print(f"Processed {wav_filename}: {text}")
