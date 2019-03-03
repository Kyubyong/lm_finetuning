'''
Consulted the followings
https://github.com/zalandoresearch/flair/blob/master/resources/docs/TUTORIAL_9_TRAINING_LM_EMBEDDINGS.md
https://github.com/zalandoresearch/flair/issues/167
https://github.com/zalandoresearch/flair/issues/53
'''

import torch
from pathlib import Path
import argparse
# from flair.data import Dictionary
from flair.models import LanguageModel
from flair.trainers.language_model_trainer import LanguageModelTrainer, TextCorpus
from flair.embeddings import FlairEmbeddings
from tqdm import tqdm
import os

def generate(model, inputs, n_chars, fout, device="cuda"):
    idx2item = model.dictionary.idx2item
    # print(inputs.size())

    # initial hidden state
    hidden = model.init_hidden(1)

    # generate text character by character
    characters = []
    for i in tqdm(range(n_chars)):
        with torch.no_grad():
            prediction, rnn_output, hidden = model.forward(inputs, hidden)
            word_weights = prediction.squeeze(1).data.div(1.0).exp().cpu()
            word_idx = torch.multinomial(word_weights, 1)[0]

            inputs = word_idx.unsqueeze(-1).to(device) # (1, 1)
            word = idx2item[word_idx].decode('UTF-8')
            characters.append(word)

    # save
    with open(fout, 'w') as fout:
        fout.write(''.join(characters))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seqlen", type=int, default=250,
                        help="prompt / sequence length")
    parser.add_argument("--n_epochs", type=int, default=100)
    parser.add_argument("--n_chars", type=int, default=3000,
                        help="number of generated characters")
    parser.add_argument("--ckpt_dir", type=str, default="checkpoints2")
    parser.add_argument("--output_dir", type=str, default="outputs2")
    hp = parser.parse_args()

    if not os.path.exists(hp.ckpt_dir): os.makedirs(hp.ckpt_dir)
    if not os.path.exists(hp.output_dir): os.makedirs(hp.output_dir)

    # device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    print("# load existing language model")
    news_forward = FlairEmbeddings('news-forward')
    model = LanguageModel.load_language_model(news_forward)
    model.to(device)

    print("# load input data")
    item2idx = model.dictionary.item2idx
    print(item2idx["\n".encode()])

    inputs = open('corpus/train/train.txt', 'r').read().splitlines()[-1]
    inputs = [item2idx.get(char.encode(), 0) for char in inputs]
    inputs = torch.LongTensor(inputs).unsqueeze(-1)  # (seqlen, 1)
    inputs = inputs.to(device)

    print("# load corpus")
    corpus = TextCorpus(Path('corpus/'),
                        model.dictionary,
                        model.is_forward_lm,
                        character_level=True)

    print("# trainer")
    trainer = LanguageModelTrainer(model, corpus)

    print("# Generating characters with pretraned model")
    generate(model, inputs, hp.n_chars, f"{hp.output_dir}/0.out", device)

    print("# continue training the model on the new corpus")
    for epoch in range(1, hp.n_epochs):
        print(f"# epoch: {epoch}")
        print("training ..")
        trainer.train(f'{hp.ckpt_dir}', sequence_length=hp.seqlen, max_epochs=1)

        print("Generating ..")
        generate(model, inputs, hp.n_chars, f"{hp.output_dir}/{epoch}.out", device)

        print("Loading saved model")
        model = LanguageModel.load_language_model(f'{hp.ckpt_dir}/best-lm.pt')
        model.to(device)