import urllib.request
import re
import os
import argparse
from nltk.tokenize import word_tokenize

def get_text(url):
    with urllib.request.urlopen(url) as response:
       text = response.read().decode("utf-8")
    return text

def sent_tokenize(text):
    text = text.replace("—", " — ")
    sents = re.split("(?<=[!?.;])[ ]", text)
    _sents = []
    for s in sents:
        _sents.extend(re.split("[ ](?=[—])", s))

    return _sents
def refine(text, seqlen=None):
    print("refine..")
    if seqlen is None:
        return text

    text = text.strip().replace("\r\n", " ")
    text = re.sub("[ ]+", " ", text)
    sents = sent_tokenize(text) + ['dummy'*100]

    samples = []
    for start in range(len(sents)):
        for end in range(start+1, len(sents)+1):
            sample = sents[start:end]
            sample = " ".join(sample)
            length = len(sample) + (end-start-1) # space between sents
            if length > seqlen:
                sample = sents[start:end-1]
                if sample != []:
                    sample = " ".join(sample)
                    sample = ' '.join(word_tokenize(sample))
                    samples.append(sample)
                break

    text = "\n".join(samples)
    # print(text)
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seqlen", type=int, default=250)
    hp = parser.parse_args()

    url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    text = get_text(url)

    train_start = "Call me Ishmael"
    train_end = "sat due eastward for the earliest sun."
    test_end = "Epilogue"
    train_text = re.search(f"(?s)({train_start}.+?{train_end})", text).group(1)
    test_text = re.search(f"(?s){train_end}(.+?){test_end}", text).group(1)

    train_text = refine(train_text, hp.seqlen)
    test_text = refine(test_text)

    # save
    if not os.path.exists('corpus/train'): os.makedirs('corpus/train')
    with open('corpus/train/train.txt', 'w') as fout:
        fout.write(train_text)
    with open("corpus/valid.txt", 'w') as fout:
        fout.write(test_text)
    with open("corpus/test.txt", 'w') as fout:
        fout.write(test_text)





