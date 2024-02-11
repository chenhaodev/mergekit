# #q- how to merge llm for mix-of-expert? @runpod-rtx-3080ti, 20min
# apt-get update; apt-get install -y silversearcher-ag tmux vim git-lfs; tmux new -s download; pip install huggingface_hub; huggingface-cli login; git clone https://github.com/chenhaodev/mergekit; cat configs/[xxx, e.g solar-sakura-carbonvillain-19b.yml]; huggingface-cli download --resume-download [xxx, e.g kyujinpy/Sakura-SOLAR-Instruct]; huggingface-cli download --resume-download [xxx, e.g jeonsworld/CarbonVillain-en-10.7B-v1]
# git clone https://github.com/chenhaodev/mergekit.git; cd mergekit/; pip install -e .; mergekit-yaml configs/solar-sakura-carbonvillain-19b-v1.yml /workspace/merged_model --copy-tokenizer --trust-remote-code --allow-crimes --lazy-unpickle; cd /workspace/merged_model; huggingface-cli upload solar-sakura-carbonvillain-19b-v1 . .

mergekit-yaml configs/solar-sakura-carbonvillain-19b-v1.yml /workspace/merged_model --copy-tokenizer --trust-remote-code --allow-crimes --lazy-unpickle;

