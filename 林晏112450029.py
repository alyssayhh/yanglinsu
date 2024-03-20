
import janome

from janome.tokenizer import Tokenizer

t = Tokenizer()

sample='すもももももももものうち'


for token in t.tokenize(sample):
    print(token.part_of_speech.split(','))