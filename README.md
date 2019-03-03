# Language Model Fine-tuning for Moby Dick

I have a dream. I'd like to write a novel. But, unfortunately, I don't think I can. Simply I don't have such talents.
Hopefully I'll be able to make a machine write a novel someday instead of me. Someday ...
Luckily and thankfully we don't have to train a language model from scratch. Many great pretrained models are available.
What we need to do is fine-tune it for our task.
I want to see what will happen if we fine-tune a language model to Moby Dick--one of the greatest novels of all time--and continue to generate text.
Does it look as if it belongs to the novel? I don't think so.
But, anyway I decided to run a small experiment.


## Requirements
* python 3.6+
* flair==0.4.1
* nltk==3.4
* tqdm==4.30.0
* torch==1.0

## Pretrained Language Model
* News-forward LM from [Flair](https://github.com/zalandoresearch/flair)
* It's a character rnn model.

## Fine-tuning
* STEP 1. Let's get [Moby Dick](https://www.gutenberg.org/files/2701/2701-0.txt) from [Project Gutenberg](https://www.gutenberg.org/). We take chapter 1 though chapter 134 for training.
```
python prepare_data.py
```

* STEP 2. Finetune the news-forward pretrained lm with Moby Dick text during 100 epochs. At every epoch, we save generated text.
```
python finetune.py
```

## Check the outputs in [outputs](outputs).
