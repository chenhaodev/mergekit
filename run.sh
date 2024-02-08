git clone https://github.com/chenhaodev/mergekit.git; cd mergekit/; pip install -e .
mergekit-yaml configs/solar-sakura-carbonvillain-19b.yml merge --copy-tokenizer --trust-remote-code --allow-crimes --out-shard-size 4B --lazy-unpickle
#python run-upload.py #sleep infinity
