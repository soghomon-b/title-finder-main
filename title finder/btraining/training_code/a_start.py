#collects data and preprocess it as follows; 
# divides each passage into sentences when they are separated by a full-stop. 
# assigns Part of Speech Tags to each sentence 


# Start here, call this function to extract the sentences. 
def sentence_extractor(file : str ) -> list:
    """
    consumes a .txt file and outputs a list of sentences
    """
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
        

def sentence_processor(sentence : str ) -> str: 
    """
    consumes a sentence and process it to 
    take out all unnecessary words. 
    """
    identity_words = [ "a", "the", "is", "are", "was", "were", "am" ]
    list_of_words = sentence.split(" ")
    for i in list_of_words:
        if i in identity_words:
            sentence = sentence.replace(" "+ i + " ", " ")
    return sentence
# now call the output of the previous function to this function. 
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

