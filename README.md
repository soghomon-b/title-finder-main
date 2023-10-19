# title-finder-main
Uses Part of Speech Tagging to decide whether a given sentence is a title or not


## Background and Introduction
While processing had-written books, the OCR model has omitted the formatting clues that existed in the textbook that identified titles, like bolding or lines. Therefore, this library helps find titles using meaning and no formatting clues using little data.
The title finder learns sequences of [Part of Speech Tags](https://www.nltk.org/book/ch05.html) and calculates the occurrence probability of each POS tag and stores the tag and its occurrence probability in a model. Then, the model can be used to decide whether a sentence is 
title by first converting it into POS tags (using NLTK library) and then seeing if the sequence exists in the model and has a probability higher than a threshold. 

## Steps on training, evaluating, and tagging
  This project is coded using Python, make sure you have Python 3.7.0 or higher and NLTK installed before using it. We suggest first making an empty .py file and importing the class you want to use, then following the steps below;
### Training 
  - make an instance of the trainer class with your training data as a list.
  - call the tags_getter function on the instance
  - call the model_creator function on the instance
  - save the model you got in the model.py file in the evaluation package. 
    ```python

    #define the parameters needed for the evaluator object
    training_data: list = ["CEDaR Space", "Indiginous Languages"] #add the training data here as a list.

    #make an object instance and follow the steps above
    trainer : Trainer = Trainer(training_data)
    trainer.tags_getter()
    trainer.model_creator()
    ```
### Evaluation 
  - after obtaining the model from training, or your own model (check examples in model.py), make an instance of the evaluator class from the file main_eval.py
  - call the title tagger and no_title tagger functions
  - call the numbers functions to see a summary of fp (false positives) and fn (false negatives).
    ```python
    #import the model 
    from model import model_dict

    #define the parameters needed for the evaluator object
    optimal_threshold: int = 0.002 #the threshold of the probability of the tags to be seen as titles.
    title: list = ["English Dialects", "Kwak'wala grammar" ] #insert phrases that are known to be titled in the scope of your data
    no_title = ["tomorrow", "then or now" ] #insert phrases that are known to be not typically a title in the scope of your data

    #make an object instance and follow the steps above
    evaluator: Evaluator = Evaluator(optimal_threshold, model_dict, title, no_title)
    evaluator.title_tagger(optimal_threshold)
    evaluator.no_title_tagger(optimal_threshold)
    print(evaluator.numbers(optimal_threshold))
    ```
### Deployment 
  if you want to use a model to find titles in some passages you have, do the following
  - make an instance of the deployer class
  - call the titles-finder function
  - call the tags-producer function
  - then the title-tagger function.
  - Call the page-printer function if you want the page to be printed with the titles found on separate lines.

    ```python
    #import the model 
    from training_file_copies import model
    
    #define the parameters needed for the deployer object
    optimal_threshold: int = 0.002 #the threshold of the probability of the tags to be seen as titles.
    text : str = "title finder\ddeployment\82.txt"  
    
    #make an object instance and follow the steps above
    deployer: Deployer = Deployer(optimal_threshold, model.model_dict)
    deployer.titles_finder(text)
    deployer.tags_producer()
    deployer.title_tagger()
    ```
