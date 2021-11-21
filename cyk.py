# Algoritma CYK

def cnf_to_dictionary(cnf_file):
# convert cnf (text file) ke dictionary
    # load file
    file = open(cnf_file, 'r')
    content = file.readlines()
    file.close()
    dictionary = {}
    for line in content:
        # rapihin text line (hapus baris kosong dan karakter newline(\n))
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        if (line != ''):
            LHS = line.split('->')[0]               # bagian kiri production rule
            RHS = line.split('->')[1].split('|')    # bagian kanan production rule
            # masukkan ke dictionary
            for x in RHS:
                if (dictionary.get(x) == None):
                    dictionary.update({x:[LHS]})
                else:
                    dictionary[x].append(LHS)
    #print(dictionary)
    return dictionary


def cyk(tkn, dictionary):
# Program Utama CYK
    n = len(tkn)
    # membuat parse tree table
    parse_table = [[[] for j in range (i)] for i in range (1,n+1)]
    for j in range (n): # mengisi isi baris n-1 
        if (dictionary.get(tkn[j]) != None):
            parse_table[n-1][j] = dictionary.get(tkn[j])
    for i in range (n-2,-1,-1): # mengisi baris n-2 sampai 0
        for j in range (i+1):
            # kombinasi yang mungkin
            combination = []
            for k in range (1,n-i):
                temp = [f'{a}{b}' for a in parse_table[n-k][j] for b in parse_table[i+k][j+k]]
                combination.extend(x for x in temp if x not in combination)
            # cek dictionary
            for x in combination:
                if (dictionary.get(x) != None):
                    temp = dictionary.get(x)
                else:
                    temp = []
                parse_table[i][j].extend(x for x in temp if x not in parse_table[i][j])
    #print(parse_table)
    if 'S' in parse_table[0][0]:
        return True
    else:
        return False