from pyknp import Jumanpp
import random

words = open('./words.txt')

jumanpp = Jumanpp()

markov = {}
for word in words:
    result = jumanpp.analysis(word)
    w1 = ''
    w2 = ''

    for word in result.mrph_list():
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word.midasi)
        w1, w2 = w2, word.midasi

for _ in range(300):
    sentence = ''
    w1, w2 = random.choice(list(markov.keys()))
    sentence += w1 + w2
    for _ in range(1000):
        try:
            tmp = random.choice(markov[(w1, w2)])
            sentence += tmp
            w1, w2 = w2, tmp

        except:
            break

    print(sentence)
