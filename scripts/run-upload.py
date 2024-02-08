MODEL_NAME = 'Yi-2x34B-v2-Merge-Slerp'
# @title ## Upload model to Hugging Face { display-mode: "form" }
# @markdown Enter your HF username and the name of Colab secret that stores your [Hugging Face access token](https://huggingface.co/settings/tokens).
username = 'chenhugging' # @param {type:"string"}
token = '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' # @param {type:"string"}
license = "apache-2.0" # @param ["apache-2.0", "cc-by-nc-4.0", "mit", "openrail"] {allow-input: true}

import yaml

from huggingface_hub import ModelCard, ModelCardData, HfApi
from jinja2 import Template

branch = "mixtral"

if branch == "mixtral":
    template_text = """
---
license: {{ license }}
base_model:
{%- for model in models %}
  - {{ model }}
{%- endfor %}
tags:
- moe
- frankenmoe
- merge
- mergekit
- lazymergekit
{%- for model in models %}
- {{ model }}
{%- endfor %}
---

# {{ model_name }}

{{ model_name }} is a Mixure of Experts (MoE) made with the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):

{%- for model in models %}
* [{{ model }}](https://huggingface.co/{{ model }})
{%- endfor %}

## 🧩 Configuration

```yaml
{{- yaml_config -}}
```

"""

    # Create a Jinja template object
    jinja_template = Template(template_text.strip())

    content = jinja_template.render(
        model_name=MODEL_NAME,
        username=username,
        license=license
    )

# Save the model card
card = ModelCard(content)
card.save('merge/README.md')

# Defined in the secrets tab in Google Colab
api = HfApi(token=token)

api.create_repo(
    repo_id=f"{username}/{MODEL_NAME}",
    repo_type="model"
)
api.upload_folder(
    repo_id=f"{username}/{MODEL_NAME}",
    folder_path="merge",
)
