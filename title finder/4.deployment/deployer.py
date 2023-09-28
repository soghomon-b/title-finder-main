# class that finds titles using a model 

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
        n : int = 4
        sentence_list =  text.split(". ")
        filtered_sentences : list = []
        for sentence in sentence_list: 
            low = sentence.split(" ")
            if len(low) <= n:
                filtered_sentences.append(sentence)
        clean_titles = []
        for i in filtered_sentences: 
            clean_titles.append(i.replace("\n", "").replace("|", ""))
        self.sentences = clean_titles


        #REQUIRES: len(sentences) > 0
        #MODIFIES: self 
        #EFFECTS: uses the sentences to produce a list of POS tags. 
    def tags_producer(self)-> None:
        #stub
        return None

        # REQUIRES: len(tags) > 0 
        #MODIFIES: self
        #EFFECTS: 
    def title_tagger(self) -> dict: 
        
        '''decides how to evaluate each title'''
        title_dict = {}
        for tag in self.tags:
            if len(tag) == 1:
                i = self.tags[0]
                '''if there is only one sequence, evaluate it'''
                if i in self.model and self.model[i] >= self.threshold:
                    title_dict[i] = 1
                else: 
                    title_dict[i] = 0
            else: 
                probabilites = []
                seq_title = ""
                '''if more than one, use a given b given c ..etc'''
                for sequence in tag: 
                    seq_title += sequence
                    if sequence in self.model and self.model[sequence] >= self.threshold: 
                        probabilites.append(self.model[sequence])
                product = 1
                for i in probabilites:
                    product *= i
                if product >= self.threshold:
                    title_dict[seq_title] = 1
                else: 
                    title_dict[seq_title] = 0
        
        return title_dict