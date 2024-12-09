# Self-Improving Zero-Shot Biomedical NER with LLMs
This repository contains the code for the DSC 253/CSE 291 Project "Self-Improving Zero-Shot Biomedical Named Entity Recognition with Large Language Models".

## Setup
To setup the environment, run the following command:
```bash
bash setup.sh
conda create --name zero-shot-bioner-env python=3.10
conda activate zero-shot-bioner-env
pip install -r requirements.txt
```

## Datasets
The datasets used in this project are:
1. [NCBI Disease](https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/)
2. [I2B2 2010](https://www.i2b2.org/NLP/DataSets/)
3. [BC2GM](https://github.com/spyysalo/bc2gm-corpus)

## References
- Code for Self-Evaluation Guided Decoding is adapted from [SelfEval-Guided Decoding for Multi-step Reasoning](https://github.com/YuxiXie/SelfEval-Guided-Decoding)
- Necessary changes have been made to the code to adapt it to the biomedical NER task.