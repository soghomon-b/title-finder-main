# class that finds titles using a model 
from training_file_copies import b_pos_tagger_deploy 
from training_file_copies import model

class deployer:
    def __init__(self, threshold : int , model : dict , sentences : list , tags : list) -> None:
        self.threshold = threshold 
        self.model = model 
        self.sentences = sentences
        self.tags = tags


        #REQUIRES: text to be a txt file path
        #MODIFIES: self
        #EFFECTS: extracts the tags in a txt file to a list. 
    def titles_finder(self, text : str ) -> None : 
        n_max : int = 4
        sentence_list =  text.split(". ")
        filtered_sentences : list = []
        clean_titles = []
        for i in sentence_list: 
            clean_titles.append(i.replace("\n", "").replace("|", ""))
        for sentence in clean_titles: 
            low = sentence.split(" ")
            if len(low) <= n_max:
                filtered_sentences.append(sentence)
        self.sentences = filtered_sentences


        #REQUIRES: len(sentences) > 0
        #MODIFIES: self 
        #EFFECTS: uses the sentences to produce a list of POS tags. 
    def tags_producer(self)-> None:
        raw_tags = b_pos_tagger_deploy.tagger(self.sentences)
        for tags in raw_tags:
             bi_tri_list = []
             i = 0
             while i < len(tags) - 3:
                 sub_list = tags[ i :  i + 2 ]
                 bi_tri_list.append(sub_list)
                 i = i + 2
             sub_list = tags[ i :  i + 3 ]
             bi_tri_list.append(sub_list)
             self.tags.append(bi_tri_list)

        # REQUIRES: len(tags) > 0 
        #MODIFIES: self
        #EFFECTS: 
    def title_tagger(self) -> list: 
        title = []
        for i in range(0, len(self.tags)): 
            tag = self.tags[i]
            sentence = self.sentences[i]

            if tag in self.model and self.model[tag] >= self.threshold:
                title.append(sentence)
        return title


    


loda = deployer(0.001, model.model_dict, [], [] )

loda.titles_finder(model.text)
loda.tags_producer()
print(loda.sentences)
m = loda.title_tagger()
print(m)
