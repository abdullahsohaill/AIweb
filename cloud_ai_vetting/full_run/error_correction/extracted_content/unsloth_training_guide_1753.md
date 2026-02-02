# Unsloth Training Guide
**URL:** https://docs.unsloth.ai/new/how-to-train-llms-with-unsloth-and-docker
**Page Title:** How to Fine-tune LLMs with Unsloth & Docker | Unsloth Documentation
--------------------

Local training can be complex due to dependency hell or breaking environments. Unsloth’s Docker image can bypass these issues. No setup is needed: pull and run the image and start training.
- Unsloth official Docker image: unsloth/unsloth
Unsloth official Docker image: unsloth/unsloth
Why Use Unsloth & Docker?
Unsloth’s Docker image is stable, up-to-date and works in supported setups like Windows.
[LINK: supported setups](/docs/get-started/fine-tuning-for-beginners/unsloth-requirements#system-requirements)
- Fully contained dependencies keep your system clean. Runs safely without root.
Fully contained dependencies keep your system clean. Runs safely without root.
- Use locally or on any platform with pre-installed notebooks.
Use locally or on any platform with pre-installed notebooks.
You can now use our main Docker image unsloth/unsloth for Blackwell and 50-series GPUs - no separate image needed.

### ⚡ Step-by-Step Tutorial

Install Docker and NVIDIA Container Toolkit.
Install Docker via Linux or Desktop (other).
Then install NVIDIA Container Toolkit :
[LINK: Linux](https://docs.docker.com/engine/install/)
[LINK: Desktop](https://docs.docker.com/desktop/)
[LINK: NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation)
Run the container.
unsloth/unsloth is Unsloth's only Docker image. For Blackwell and 50-series GPUs, use this same image - no separate image needed. If using DGX Spark, you'll need to follow our DGX guide .
[LINK: Blackwell](/docs/basics/fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth)
[LINK: DGX guide](/docs/basics/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth)
Access Jupyter Lab
Go to http://localhost:8888 and open Unsloth.
Access the unsloth-notebooks tabs to see Unsloth notebooks.
Start training with Unsloth
If you're new, follow our step-by-step Fine-tuning Guide , RL Guide or just save/copy any of our premade notebooks .
[LINK: Fine-tuning Guide](/docs/get-started/fine-tuning-llms-guide)
[LINK: RL Guide](/docs/get-started/reinforcement-learning-rl-guide)
[LINK: notebooks](/docs/get-started/unsloth-notebooks)
- /workspace/work/ — Your mounted work directory
/workspace/work/ — Your mounted work directory
- /workspace/unsloth-notebooks/ — Example fine-tuning notebooks
/workspace/unsloth-notebooks/ — Example fine-tuning notebooks
- /home/unsloth/ — User home directory
/home/unsloth/ — User home directory

### 📖 Usage Example

If you don't have an SSH key pair:

### ⚙️ Advanced Settings

JUPYTER_PASSWORD
Jupyter Lab password
unsloth
JUPYTER_PORT
Jupyter Lab port inside container
8888
SSH_KEY
SSH public key for authentication
None
USER_PASSWORD
Password for unsloth user (sudo)
unsloth
- Jupyter Lab: -p 8000:8888
Jupyter Lab: -p 8000:8888
- SSH access: -p 2222:22
SSH access: -p 2222:22
Important : Use volume mounts to preserve your work between container runs.

### 🔒 Security Notes

- Container runs as non-root unsloth user by default
Container runs as non-root unsloth user by default
- Use USER_PASSWORD for sudo operations inside container
Use USER_PASSWORD for sudo operations inside container
- SSH access requires public key authentication
SSH access requires public key authentication
[LINK: Previous Vision Fine-tuning](/docs/basics/vision-fine-tuning)
[LINK: Next DGX Spark and Unsloth](/docs/basics/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth)
Last updated 22 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the privacy policy .

--------------------