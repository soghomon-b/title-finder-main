from c_bigram_trigram import m 

def dict_maker(txt : str)-> dict: 
    probs_dict = {}
    with open(txt , "r") as file:
        loda = file.readlines()
    for i in loda: 
        i = i.replace("\n", "")
        if i not in probs_dict: 
            probs_dict[i ] = 1
        if i in probs_dict:
            probs_dict[i ] += 1
    overall = len(probs_dict)
    for key in probs_dict:
         probs_dict[key] /= overall
    with open("/Users/cedarspace/Documents/GitHub/title-finder/title finder/2.training/single POS /probabilities_2.txt", "w") as txt_file:
        for key, value in probs_dict.items():
              txt_file.write(f"{key}: {value}" + "\n")
    return probs_dict



dict_maker("/Users/cedarspace/Documents/GitHub/title-finder/title finder/1.data_collection/sample titles from boas/test.txt")
