import b_pos_tagger
from b_pos_tagger import loda
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



def list_of_list(lopos: list ) -> list:

    lopos2 = []
    for i in lopos: 
        m = bigram_triagram(i)
        lopos2.append(m)
    lopos3 = [ ]
    for i in lopos2: 
        m = all_string(i)
        lopos3.append(m)
    with open("/Users/cedarspace/Documents/GitHub/title-finder/title finder/1.data_collection/sample titles from boas/test.txt", "w") as txt_file:
        for i in lopos3: 
            for ii in i: 
               txt_file.write(str(ii) + "\n")
    return lopos3


m = list_of_list(loda)
print("loda: " + str(loda))
print("m: " + str(m))