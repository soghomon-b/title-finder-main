import nltk 
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import a_start
from a_start import remove_repetitions
from a_start import series_processor 
from a_start import sentence_extractor


#EFFECTS: produces a dictionary of Part Of Speech Tags with the words for each sentence. 
def pos_tagger(sentence : str )-> list: 
    tagged_sentences = [ ]
    for i in sentence: 
        tokens = word_tokenize(sentence)
        tagged_sentence = pos_tag(tokens)
        tagged_sentences.append(tagged_sentence)
    return tagged_sentence

#EFFECTS: applies pos_tagger to a list of sentences
def los_pos_tagger(losentence : list ) -> list: 
    lolotags = [ ]
    for i in losentence:
        lotags = pos_tagger(i)
        lolotags.append(lotags)
    return lolotags

#EFFECTS: Extracts the POS tags from the dict above
def tags_extractor(lolotags : list) -> list:
    lolotags_only = []
    for i in lolotags:
        lotags = []
        for sot in i: 
            lotags.append(sot[1])
        lolotags_only.append(lotags)

    return lolotags_only

#EFFECTS: applies different functions above to a list of sentences to produce the list of tags.  
def tagger(sentences: str)-> list:
    return tags_extractor(los_pos_tagger(remove_repetitions(series_processor(sentences))))


#a= tagger("C://Users//soghm//OneDrive//Desktop//title-finder-main//title finder//1.data_collection//sample titles from boas//titles.txt")
