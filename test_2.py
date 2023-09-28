def bigram_triagram(pos_list : list ) -> list :
    """consumes a list of tags and groups them as bigrams or trigrams"""
    bi_tri_list = []
    ii = 0
    while ii < len(pos_list) - 3:
        seq = ""
        for i in pos_list[ii : ii + 2]: 
            seq += i + "."
        bi_tri_list.append(seq)
        ii = ii + 2
    seq2 = ""
    for i in pos_list[ ii :  ii + 3 ]:
        seq2 += i + "."
    bi_tri_list.append(seq2)
    return bi_tri_list

def list_of_list(lol):
    for i in lol:
        m = bigram_triagram(i)
        print(m)


test = [ ['NN', 'IN', 'VBG', 'NNS'],
['NNP', 'NNP'],
['DT', 'NNP', 'IN', 'NNP'],
['NNP', 'VBD', 'NNP'],
['JJ', 'NNS', 'IN', 'NNP'],
['JJ', 'NNP'],
['VBN', 'JJ', 'NNS'],
['JJ', 'NNP'],
['JJ', 'NNP'],
['NN', 'IN', 'NNP'],
['DT', 'JJ', 'NNS'],
['DT', 'NNP', 'IN', 'NNP'],
['VBN', 'JJ', 'NNP', 'CC', 'NNP'],
['VBN', 'NNP', 'NNP'],
['NN', 'NNP'],
['VBN', 'NNP', 'NNP'],
['JJ'],
['VBN', 'NNP', 'NNP'],
['DT', 'NNP', 'IN', 'NNP'],
['VBG', 'IN', 'NNP'],
['NN', 'IN', 'NNP'],
['NNP', 'NNP', 'CC', 'NNP'],
['DT', 'NNP', 'IN', 'NNP', 'NNP'],
['DT', 'NNP', 'IN', 'NNP', 'NNP']
 ]

list_of_list(test)
