#helper functions for the trainer class. Focusing on pre-processing training data. 


#REQUIRES: file to be a txt file path
#EFFECTS: extracts training data from a txt file and stores them in a list (not used in trainer class)
def sentence_extractor(file : str ) -> list:
    splitters = [".", "!", "?"  ]
    zero_words = [ "a", "the", "is", "are", "was", "were", "am" ]
    final_list : list = []
    with open(file, "r") as passage:
        data : str = passage.read().replace('\n', '.')
        for splitter in splitters:
            data = data.replace(splitter, splitters[0])
        data_list : list = data.split(splitters[0])
        for i in data_list: 
            for word in zero_words:
                i = i.replace(word, "")
                final_list.append(i)
        return final_list
        
#MODIFIES: sentence
#EFFECTS: removes the words in identity_words from the training data. 
def sentence_processor(sentence : str ) -> str: 
    identity_words = [ "a", "the", "is", "are", "was", "were", "am" ]
    list_of_words = sentence.split(" ")
    for i in list_of_words:
        if i in identity_words:
            sentence = sentence.replace(" "+ i + " ", " ")
    return sentence

#MODIFIES: losentence 
#EFFECTS: applies sentence_processor to each of sentences in losentence
def series_processor(losentence : list ) -> list: 
    """
    uses sentence_processor to process all sentences in the losentence 
    """
    output_los : list = []

    for i in losentence:
        i = sentence_processor(i)
        output_los.append(i)
    return output_los

def remove_repetitions(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

