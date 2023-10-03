

def titles_finder(text : str ) -> list : 
    '''
    divides string into a list by the dot, filters the elements to ones less than
    n words 
    '''
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
    return clean_titles





with open("/Users/cedarspace/Documents/GitHub/title-finder/title finder/4.deployment/test_deploy.txt", "r") as file: 
    m = file.read()


print(titles_finder(m))