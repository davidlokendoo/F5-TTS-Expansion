# F5-TTS-Expansion
This project fine-tunes the F5-TTS model to add a new language, using a pre-trained base to enhance multilingual capabilities.

# Installation
```
# create a python 3.10 env
conda create --name f5-tts python=3.10
conda activate f5-tts

# Install PyTorch with your CUDA version, e.g.
pip install torch==2.3.0+cu118 torchaudio==2.3.0+cu118 --extra-index-url https://download.pytorch.org/whl/cu118

#Install PyTorch (CPU Version) on Mac
pip install torch==2.3.0 torchaudio==2.3.0


