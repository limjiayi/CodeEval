# Created by JiaYi Lim on 11/1/2014

import sys
from operator import itemgetter, attrgetter

def process(text):
    text = text.split()
    processed = []
    for word in text:
        new_word = word.strip('.,;?"')
        processed.append(new_word)
    return processed

def build_chains(len_phrase, n_gram, text):
    d = {}
    for i in range(len(text)-1-len_phrase):
        word = ' '.join(text[i:i+len_phrase])
        start = i + len_phrase
        end = i + n_gram
        next_word = ' '.join(text[start:end])
        if d.get(word):
            d[word].append(next_word)
        else:
            d[word] = [next_word]
    return d

def build_freqs(chains):
    for key in chains.keys():
        vals = chains[key]
        freqs = {}
        for val in vals:
            if freqs.get(val):
                freqs[val] += 1
            else:
                freqs[val] = 1
        chains[key] = freqs.items()
    return chains


def normalize(freq):
    freq = str(freq)
    if freq[0] == 1:
        return '1.000'
    else:
        if len(freq) == 5:
            return freq
        elif len(freq) < 5:
            while len(freq) < 5:
                freq += '0'
            return freq
        else: # len(freq) > 5:
            return freq[:5]

def start():
    text = 'Mary had a little lamb its fleece was white as snow; \
            And everywhere that Mary went, the lamb was sure to go. \
            It followed her to school one day, which was against the rule; \
            It made the children laugh and play, to see a lamb at school. \
            And so the teacher turned it out, but still it lingered near, \
            And waited patiently about till Mary did appear. \
            "Why does the lamb love Mary so?" the eager children cry; "Why, Mary loves the lamb, you know" the teacher did reply."'
    text = process(text)

    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line != '':
                line = line.split(',')
                n_gram = int(line[0])
                phrase = line[1]
                len_phrase = len(phrase.split())
                chains = build_chains(len_phrase, n_gram, text)
                freqs = build_freqs(chains)
                predictions = freqs[phrase]
                total = sum([ p[1] for p in predictions ])
                results = []
                for p in predictions:
                    results.append((p[0], p[1]/float(total)))
                    # sort by the secondary key first, alphabetical order
                    results = sorted(results, key=itemgetter(0))
                    # now sort by the primary key, frequency
                    # set reverse=True to get results in descending frequency
                    results = sorted(results, key=itemgetter(1), reverse=True)
                string = ''
                for idx, res in enumerate(results):
                    if idx != len(results) - 1:
                        string += res[0] + ',' + normalize(res[1]) + ';'
                    else:
                        string += res[0] + ',' + normalize(res[1])
                print string


if __name__ == '__main__':
        start()