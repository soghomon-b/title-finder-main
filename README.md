# title-finder-main
Uses Part of Speech Tagging to decide whether a given sentence is a title or not


## Background and Introduction
While processing had-written books, the OCR model has omitted the formatting clues that existed in the textbook that identified titles, like bolding or lines. Therefore, this library helps find titles using meaning and no formatting clues using little data.
The title finder learns sequences of [Part of Speech Tags](https://www.nltk.org/book/ch05.html) and calculates the occurance probability of each POS tag and sotres the tag and its occurance probability in a model. Then, the model can be used to decide whether a sentence is 
title by first converting it into POS tags (using NLTK library) and then seeing if the sequence exists in the model and has a probability higher than a threshold. 

## Steps on training, evaluating, and tagging
  This project is coded using Python, make sure you have Python 3.7.0 or higher and NLTK installed before using it. We suggest first making an empty .py file and importing the class you want use, then follow the step below;
### Training 
  - make an instance of the trainer class with your training data as a list.
  - call the tags_getter function on the instance
  - call the model_creator function on the instance
    ```python
    training_data: list = ["CEDaR Space", "Indiginous Languages"] #add the training data here as a list. 
    trainer : Trainer = Trainer(training_data)
    trainer.tags_getter()
    trainer.tags_trainer()
    ```
### Evaluation 
  - after obtaining the model from training, or your own model (check examples in model.py), make an instance of the evaluator class from the file main_eval.py
  - call the title tagger and no_title tagger functions
  - call the numbers functions to see a summary of fp (false positives) and fn (false negatives).
### Deployment 
  if you want to use a model to find titles in some passages you have, do the following
  - make an instance of the deployer class
  - call the titles-finder function
  - call the tags-producer function
  - then the title-tagger function.
  - if you want the page to be printed with the titles found on separate lines, call the page-printer function. 
