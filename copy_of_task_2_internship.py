# -*- coding: utf-8 -*-
"""Copy of Task 2 Internship

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17oSZnYnTNYMci-sfAG1S5Ms-RnAuu2MK
"""

# Commented out IPython magic to ensure Python compatibility.
# Clone the WebUI repo
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
# %cd stable-diffusion-webui

# Install dependencies
!pip install -r requirements.txt

# Install xformers for efficient memory usage (optional but recommended)
!pip install xformers

# Install Hugging Face libraries
!pip install huggingface_hub

# Download model to the correct folder
from huggingface_hub import hf_hub_download

# Example: Download the Stable Diffusion v1.4 model
model_path = hf_hub_download("CompVis/stable-diffusion-v-1-4-original", filename="sd-v1-4.ckpt")
!mv {model_path} models/Stable-diffusion/

# Start the WebUI with a public link
!python launch.py --share --xformers