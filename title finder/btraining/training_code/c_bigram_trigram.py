import b_pos_tagger


#REQUIRES: pos_list >= 2
#EFFECTS: groups the items of the list into tags of 2 or 3 lists. 
# [a, b, c, d, e] will produce [a.b. , c.d.e.]
def bigram_triagram(pos_list : list ) -> list :
    """consumes a list of tags and groups them as bigrams or trigrams"""
    bi_tri_list = []
    i = 0
    while i < len(pos_list) - 3:
        sub_list = pos_list[ i :  i + 2 ]
        bi_tri_list.append(sub_list)
        i = i + 2
    sub_list = pos_list[ i :  i + 3 ]
    bi_tri_list.append(sub_list)
    return bi_tri_list

def all_string(lop : list) -> list:
    new_list = [] 
    for i in lop: 
         str_1 = ""
         for ii in range(0, len(i)):
            str_1 += i[ii] + "."
         new_list.append(str_1)
    return new_list


#REQUIRES: lopos to be a list of lists. 
#EFFECTS: applies the bigram_triagram to a list of lists. 
def list_of_list(lopos: list ) -> list:

    lopos2 = []
    for i in lopos: 
        m = bigram_triagram(i)
        lopos2.append(m)
    lopos3 = [ ]
    for i in lopos2: 
        m = all_string(i)
        lopos3.append(m)
    return lopos3


