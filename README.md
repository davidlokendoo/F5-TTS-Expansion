# F5-TTS-Expansion
This project fine-tunes the F5-TTS model to add a new language, using a pre-trained base to enhance multilingual capabilities.

# Installation
```
# create a python 3.10 env
conda create --name f5-tts python=3.10
conda activate f5-tts
```
## Install PyTorch with your CUDA version
```
pip install torch==2.3.0+cu118 torchaudio==2.3.0+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
```
## Install PyTorch (CPU Version) on Mac
```
pip install torch==2.3.0 torchaudio==2.3.0
```
## Clone the original repository and install the required dependencies
```
git clone https://github.com/SWivid/F5-TTS.git
cd F5-TTS
pip install -e .
```
## Setting up your dataset
1. Create a directory for your data within the f5-tts/data folder. For example: f5-tts/data/new_language.
2. Inside your new language directory, create a folder named wavs to store your audio files. For example: f5-tts/data/new_language/wavs.

At this point, your file structure should look like this:
```
/F5-TTS
|-- data/
|   |-- new_language_pinyin/
|   |   |-- wavs/
|   |   |   |-- ...
|   |   |   |-- ...
|   |   |   |-- ...
```
3. Use `wav_and_metadata.py` to convert your MP3 files to WAV format and generate a `metadata.csv` file.
   
* Specify the relative paths for your MP3 file (source audio in MP3 format), WAV file (destination in the `wavs` directory you created), and `metadata.csv` file, and then run the following command:
```
python wav_and_metadata.py
```
* After running the script, your `metadata.csv` file should be structured like this:
```
audio_file|text
wavs/audio_001.wav|tenían prohibida por ley la presencia en teatros y aglomeraciones públicas
wavs/audio_002.wav|Cómo operan el camarote claro que no nada de eso
```
Once your `metadata.csv` file is created and your MP3 files are converted to WAV, your file structure should look like this:
```
/F5-TTS
|-- data/
|   |-- new_language_pinyin/
|   |   |-- metadata.csv
|   |   |-- wavs/
|   |   |   |-- audio_001.wav
|   |   |   |-- audio_002.wav
|   |   |   |-- ...
```
   






