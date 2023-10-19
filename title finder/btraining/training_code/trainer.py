from b_pos_tagger import tagger
from c_bigram_trigram import list_of_list


# training class with the tags it extracts from the training data and the model it outputs after training. 
class Trainer: 

    #EFFECTS: constructs a trainer with the training data and empty POS tags and model. 
    def __init__(self, training_data: list) -> None:
        self.tags = []
        self.model = []
        self.training_data = training_data

    #MDIFIES: self
    #EFFECTS: creates a list of tags for each sentence in the training data. 
    def tags_getter(self) -> None: 
        extracted_tags = tagger(self.training_data)
        self.tags = list_of_list(extracted_tags)

    #REQUIRES: len(self.tags) > 0
    #MODIFIES: self
    #EFFECTS: produces a model with probabilites of POS tags as a dictionary 
    def model_creator(self) -> None: 
        probs_dict = {}
        all_tags = []
        for i in self.tags: 
            for ii in i:
                all_tags.append(ii)
        for i in all_tags: 
            if i not in probs_dict.keys(): 
                probs_dict[i ] = 1
            else:
                probs_dict[i ] += 1
        overall = len(probs_dict)
        for key in probs_dict:
            probs_dict[key] /= overall
        self.model = probs_dict
        
    

training_data: list = ["CEDaR Space", "Indiginous Languages"] #add the training data here as a list. 
trainer : Trainer = Trainer(training_data)
trainer.tags_getter()
trainer.model_creator()