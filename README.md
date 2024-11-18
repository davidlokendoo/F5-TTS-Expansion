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
|   |-- new_language/
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
|   |-- new_language/
|   |   |-- metadata.csv
|   |   |-- wavs/
|   |   |   |-- audio_001.wav
|   |   |   |-- audio_002.wav
|   |   |   |-- ...
```
4. Prepare your metadata and WAV files by running the `prepare_csv_wavs.py` script.

The `prepare_csv_wavs.py` script requires both an input and output directory. Specify the directory where your `metadata.csv` and WAV files are located when running the script.
```
cd F5-TTS/src/f5_tts/train/datasets
python prepare_csv_wavs.py /F5-TTS/data/new_language_pinyin /F5-TTS/data/new_language_pinyin
```
Three new files should have been created: `raw.arrow`, `duration.json`, and `vocab.txt`.
If the `duration.json` file is empty, it likely means the input path was not set correctly. At this point, the file structure should look like this:
```
/F5-TTS
|-- data/
|   |-- new_language/
|   |   |-- raw.arrow
|   |   |-- duration.json
|   |   |-- vocab.txt
|   |   |-- metadata.csv
|   |   |-- wavs/
|   |   |   |-- audio_001.wav
|   |   |   |-- audio_002.wav
|   |   |   |-- ...
```
## Proceed to Training
1. Create the base directory and download the pre-trained model.
   
To get started, create a directory named F5-TTS_BASE inside your ckpts directory. This directory will store the base model required for fine-tuning.
Next, download the base model required for fine-tuning. Use the following command:
```
curl -L -o ckpts/F5-TTS_BASE/model_1200000.pt "https://huggingface.co/SWivid/F5-TTS/resolve/main/F5TTS_Base/model_1200000.pt?download=true"
```
Make sure the directory structure matches the expected format before moving on.
```
/F5-TTS
|--ckpts/
|   |-- model_1200000.pt
|-- data/
|   |-- new_language/
|   |   |-- raw.arrow
|   |   |-- duration.json
|   |   |-- vocab.txt
|   |   |-- metadata.csv
|   |   |-- wavs/
|   |   |   |-- audio_001.wav
|   |   |   |-- audio_002.wav
|   |   |   |-- ...
```
2. Start training

Start the training process by specifying parameters for the script; if parameters are omitted, default values will be used.
```
# Define parameters
exp_name = "F5TTS_Base"
learning_rate = 1e-05
batch_size_per_gpu = 1
batch_size_type = "frame"
max_samples = 25
grad_accumulation_steps = 1
max_grad_norm = 1
epochs = 5
num_warmup_updates = 2
save_per_updates = 20
last_per_steps = 10
dataset_name = "test5"
finetune = True
logger = "tensorboard"
tokenizer = "pinyin"
pretrained_model_path = "data/new_language/model_last.pt"

# Build and run the command
!accelerate launch src/f5_tts/train/finetune_cli.py \
    --exp_name {exp_name} \
    --learning_rate {learning_rate} \
    --batch_size_per_gpu {batch_size_per_gpu} \
    --batch_size_type {batch_size_type} \
    --max_samples {max_samples} \
    --grad_accumulation_steps {grad_accumulation_steps} \
    --max_grad_norm {max_grad_norm} \
    --epochs {epochs} \
    --num_warmup_updates {num_warmup_updates} \
    --save_per_updates {save_per_updates} \
    --last_per_steps {last_per_steps} \
    --dataset_name {dataset_name} \
    --finetune {finetune} \
    --tokenizer {tokenizer} # \
    # --logger {logger} \
    # --pretrain {pretrained_model_path}
```
