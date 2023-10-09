

# evaluates a model from training on data. 
class evaluator:
    #EFFECTS: constructs an evaluator. 
    # optimal_thrshold: the number above which the tag in a model is labelled as a title 
    # model: the model produced from training 
    # title: list of sentences that are titles
    # no_title: list of sentences that are not titles. 
    # See model.py for examples on each of the arguments
    def __init__(self, optimal_threshold : int , model : dict , title : list , no_title : list ) -> None:
        self.optimal_threshold = optimal_threshold 
        self.model = model 
        self.title = title
        self.no_title = no_title

    #EFFECTS: tags each title labelled as title with 0 (is not a title), 1 (is a title)
    def title_tagger(self, threshold : int) -> dict: 
       
        title_dict = {}
        for title in self.title:
            if len(title) == 1:
                i = title[0]
                '''if there is only one sequence, evaluate it'''
                if i in self.model and self.model[i] >= threshold:
                    title_dict[i] = 1
                else: 
                    title_dict[i] = 0
            else: 
                probabilites = []
                seq_title = ""
                '''if more than one, use a given b given c ..etc'''
                for sequence in title: 
                    seq_title += sequence
                    if sequence in self.model and self.model[sequence] >= threshold: 
                        probabilites.append(self.model[sequence])
                product = 1
                for i in probabilites:
                    product *= i
                if product >= threshold:
                    title_dict[seq_title] = 1
                if product < threshold: 
                    title_dict[seq_title] = 0
        
        return title_dict
    
    #EFFECTS: tags each title labelled as not a title with 0 (is not a title), 1 (is a title)
    def no_title_tagger(self, threshold : int) -> dict: 
        '''decides how to evaluate each title'''
        no_title_dict = {}
        for title in self.no_title:
            if len(title) == 1:
                i = title[0]
                '''if there is only one sequence, evaluate it'''
                if i in self.model and self.model[i] >= threshold:
                    no_title_dict[i] = 1
                else: 
                    no_title_dict[i] = 0
            else: 
                seq_title = ""
                '''if more than one, use a given b given c ..etc'''
                for sequence in title: 
                    seq_title += sequence
                if seq_title in self.model and self.model[seq_title] >= threshold: 
                    no_title_dict[seq_title] = 1
                else: 
                    no_title_dict[seq_title] = 0
        
        return no_title_dict

    #EFFECTS: Detects whether some titles labelled as titles were tagged by the model as not titles.                     
    def false_negative_detector(self , threshold : int): 
        title_dict = self.title_tagger(threshold)
        false_negatives = []
        for i in title_dict:
            if title_dict[i] == 0:
                false_negatives.append(i)
        return false_negatives
    
    #EFFECTS: Detects whether some titles labelled as not titles were tagged by the model as titles.
    def false_positive_detector(self , threshold : int): 
        no_title_dict = self.no_title_tagger(threshold)
        false_positives = []
        for i in no_title_dict:
            if no_title_dict[i] == 1:
                false_positives.append(i)
        return false_positives
    
    #EFFECTS: produces a numbers summary of the evaluation 
    def numbers(self, threshold : int):
        falses = {"fp" : 0 , "fn" : 0}
        falses["fp"] = len(self.false_positive_detector(threshold))
        falses["fn"] = len(self.false_negative_detector(threshold))
        return falses
    #EFFECTS: evaluates the optimal threshold 
    def thresholds_evaluator(self):
        dict_of_thresholds = {}
        for i in range(1, 20): 
            dict_of_thresholds[i] = self.numbers(i)
        return dict_of_thresholds
    
    
