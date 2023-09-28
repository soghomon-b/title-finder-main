import model 
from model import model_dict, title , no_title

class txt_file:
    def __init__(self, address : str, mode : str ) -> None:
        self.address = address
        self.mode = mode
        open(address, mode)

class evaluator:
    def __init__(self, optimal_threshold : int , model : dict , title : list , no_title : list ) -> None:
        self.optimal_threshold = optimal_threshold 
        self.model = model 
        self.title = title
        self.no_title = no_title

    def title_tagger(self, threshold : int) -> dict: 
        '''decides how to evaluate each title'''
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

                        
    def false_negative_detector(self , threshold : int): 
        title_dict = self.title_tagger(threshold)
        false_negatives = []
        for i in title_dict:
            if title_dict[i] == 0:
                false_negatives.append(i)
        return false_negatives
    
    def false_positive_detector(self , threshold : int): 
        no_title_dict = self.no_title_tagger(threshold)
        false_positives = []
        for i in no_title_dict:
            if no_title_dict[i] == 1:
                false_positives.append(i)
        return false_positives
    
    def numbers(self, threshold : int):
        falses = {"fp" : 0 , "fn" : 0}
        falses["fp"] = len(self.false_positive_detector(threshold))
        falses["fn"] = len(self.false_negative_detector(threshold))
        return falses
    
    def thresholds_evaluator(self):
        dict_of_thresholds = {}
        for i in range(1, 20): 
            dict_of_thresholds[i] = self.numbers(i)
        return dict_of_thresholds
    
    
test_eval = evaluator(0, model_dict , [ ["NNP.NN.", "NNP.NN."] , ["NN.IN.", "NNP.NN.", "NN."] , ["NNP.,.NN."] , ["CD..."] ] , [ ["NNP.NN.", "NNP.NN."] , ["NN.IN.", "NNP.NN.", "NN."] , ["NNP.,.NN."] , ["CD..."] ] )

no_title_results = test_eval.no_title_tagger(0)
title_results = test_eval.title_tagger(0)
numbers = test_eval.numbers(0)
print(numbers)
print(no_title_results)
print(title_results)

