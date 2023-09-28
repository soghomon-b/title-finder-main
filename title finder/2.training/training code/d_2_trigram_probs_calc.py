m = [['NN.IN.NN.'], ['RB.NNS.'], ['RB.NNS.'], ['NN.IN.NN.'], ['NN.IN.NN.'], ['NN.IN.NN.'], ['NN.IN.NNP.'], ['VBG.NN.', 'IN.NN.'], ['NNP.NN.'], ['NNP.POS.NNS.'], ['VB.NN.'], ['NN.TO.', 'VBG.NN.NN.'], ['NN.TO.', 'VBG.NN.NN.'], ['NNP.IN.NNP.'], ['NNP.NN.'], ['NNP.IN.NN.'], ['NNP.IN.NN.'], ['NNP.IN.NN.'], ['NNP.TO.VB.'], ['NNP.TO.VB.'], ['NNP.IN.', 'NN.IN.', 'JJ.NN.'], ['NNP.IN.', 'NN.IN.', 'JJ.NN.'], ['DT.NNS.', 'IN.NN.'], ['DT.NNS.', 'IN.NN.'], ['NNP.NN.'], ['NN.NNS.'], ['NN.'], ['JJ.NNS.'], ['NNP.NN.'], ['NNP.NN.NN.'], ['NNP.NN.NN.'], ['NNP.POS.', 'NN.NN.', 'NN.NNP.'], ['NNP.POS.', 'NN.NN.', 'NN.NNP.'], ['NN.NN.', 'NN.IN.', 'NNP.POS.NN.'], ['NN.NN.', 'NN.IN.', 'NNP.POS.NN.'], ['VBN.NNP.VBD.'], ['JJ.NN.'], ['VBN.NN.'], ['NNS.IN.NNP.'], ['VBG.JJ.'], ['NNP.IN.NNS.'], ['NNP.NNP.'], ['NNP.NNP.'], ['NNP.NNP.'], ['NNP.NNP.'], ['DT.NN.', 'IN.NNP.NNP.'], ['VBG.IN.', 'NNP.NNP.'], ['VBG.IN.', 'NNP.NNP.'], ['VBG.IN.', 'NNP.NNP.'], ['VBN.NNP.NNP.'], ['NNP.NNP.', 'NN.NNP.NNP.'], ['NN.'], ['NNP.NNP.', 'NNP.NNP.'], ['JJ.CD.'], ['NNP.NNP.CD.'], ['DT.CD.', 'NNP.NNP.'], ['NNP.NNP.NNP.'], ['WP.VBD.', 'NNP.IN.', 'VBG.IN.NNP.'], ['DT.NN.'], ['DT.NNP.NNP.'], ['CD.NNP.NNP.'], ['NNP.NNS.'], ['NNP.NNP.'], ['NNP.NNP.'], ['NN.'], ['NNP.IN.NNP.'], ['NNP.NN.'], ['NN.IN.NNP.'], ['NN.IN.NNP.'], ['NNP.NNP.'], ['NNS.'], ['NNS.'], ['NN.NNS.'], ['DT.NN.', 'IN.NN.'], ['DT.NN.', 'IN.NN.'], ['NN.IN.NNP.'], ['NN.IN.NNP.'], ['VBN.TO.', 'VB.NNP.', 'IN.NNP.'], ['DT.JJ.NNS.'], ['NN.IN.NN.'], ['DT.NNP.'], ['NN.'], ['DT.NN.', 'IN.NN.NN.'], ['DT.NN.', 'IN.NN.NN.'], ['NN.NN.'], ['DT.NN.'], ['NN.'], ['DT.NN.'], ['NN.'], ['NNP.IN.NN.'], ['NNP.NN.'], ['NNP.NN.'], ['NN.NN.'], ['NN.IN.NNP.'], ['NNP.POS.NN.']]
m2 = []
for i in m: 
    if len(i) > 1: 
        m2.append(i)
m3 = []
for i in m2:
    str = ""
    for ii in i: 
        str += ii
    m3.append(str)

probs_dict = {}
for i in m3: 
    if i in probs_dict: 
        probs_dict[i ] += 1
    if i not in probs_dict: 
        probs_dict[i ] = 1

overall = len(probs_dict)
for key in probs_dict:
    probs_dict[key] /= overall
with open("/Users/cedarspace/Documents/GitHub/title-finder/title finder/2.training/all POS /probabilities_3.txt", "w") as txt_file:
    for key, value in probs_dict.items():
        txt_file.write(f"{key}: {value}" + "\n")


print(m3)
