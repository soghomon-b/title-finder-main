# title-finder-main
Uses Part of Speech Tagging to decide whether a given sentence is a title or not


## Background and Introduction
While processing had-written books, the OCR model has omitted the formatting clues that existed in the textbook that identified titles, like bolding or lines. Therefore, this library helps find titles using meaning and no formatting clues using little data.
The title finder learns sequences of [Part of Speech Tags](https://www.nltk.org/book/ch05.html) and calculates the occurance probability of each POS tag and sotres the tag and its occurance probability in a model. Then, the model can be used to decide whether a sentence is 
title by first converting it into POS tags (using NLTK library) then seeing if the sequence exists in the model and has a probability higher than a threshold. 

## Steps on training, evaluating, and tagging

### Training 
  - make an instance of the trainer class with your training data as a list.
  - call the tags_getter funciton on the instance
  - call the model_creator function on the instance
    (note that there are helper functions that the functions above use, check them out if you want to understand how the functions work.)
### Evaluation 
  - after optaining the model from training, or your own model (check examples in model.py), make an instance of the evaluator class from the file main_eval.py
  - call the title tagger, and no_title tagger funcitons
  - call the numbers functions to see summary of fp (false positives) and fn (false negatives).
### Deployment 
  if you want to just use the model 
  - 
