import nltk 
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import first_sentence
from first_sentence import title , no_title


def pos_tagger(sentence : str )-> list: 
    tokens = word_tokenize(sentence)
    tagged_sentence = pos_tag(tokens)
    return tagged_sentence
def los_pos_tagger(losentence : list ) -> list: 
    lolotags = [ ]
    for i in losentence:
        lotags = pos_tagger(i)
        lolotags.append(lotags)
    return lolotags

def tags_extractor(lolotags : list) -> list:
    lolotags_only = []
    for i in lolotags:
        lotags = []
        for sot in i: 
            lotags.append(sot[1])
        lolotags_only.append(lotags)
    with open("C:\\Users\\soghm\\OneDrive\\Documents\\GitHub\\title-finder\\evaluation\\eval_tags.txt", "w") as txt_file:
        for i in lolotags_only: 
            txt_file.write(str(i) + "\n")

    return lolotags_only


title_tags = tags_extractor(los_pos_tagger(no_title))

