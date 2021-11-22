# CYK Algorithm

def cnf_to_dictionary(cnf_file):
# Convert cnf (text file) to dictionary data type
    # read file
    file = open(cnf_file, 'r')
    content = file.readlines()
    file.close()
    dictionary = {}
    # process each line
    for line in content:
        # delete empty line ('') and newline ('\n')
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        if (line != ''):
            LHS = line.split('->')[0]               # left hand side of production rule
            RHS = line.split('->')[1].split('|')    # right hand side of production rule
            # fill dictionary: RHS as dictionary key and LHS as value 
            for x in RHS:
                if (dictionary.get(x) == None):
                    dictionary.update({x:[LHS]})
                else:
                    dictionary[x].append(LHS)
    ''' TESTING
    print(dictionary)
    '''
    return dictionary


def cyk(tkn, dictionary):
# CYK Main Program
    n = len(tkn)
    # create parse tree table
    parse_table = [[[] for j in range (i)] for i in range (1,n+1)]
    parse_table[n-1] = cykBase(tkn, dictionary) # fill base (row = n-1)
    for i in range (n-2,-1,-1): # fill row n-2 to 0
        for j in range (i+1):
            # find all key combination
            combination = []
            for k in range (1,n-i):
                temp = [f'{a}{b}' for a in parse_table[n-k][j] for b in parse_table[i+k][j+k]]
                combination.extend(x for x in temp if x not in combination)
            # search the key's value in dictionary
            for x in combination:
                if (dictionary.get(x) != None):
                    temp = dictionary.get(x)
                else:
                    temp = []
                parse_table[i][j].extend(x for x in temp if x not in parse_table[i][j])
    ''' TESTING
    print(parse_table)
    print("Base: ")
    print(parse_table[n-1])
    '''
    if 'S' in parse_table[0][0]:
        return True
    else:
        return False


def cykBase(tkn, dictionary):
# Base of CYK Parsing Table
    n = len(tkn)
    base = [[] for i in range(n)]
    # Checking dictionary
    for i in range (n):
        if (dictionary.get(tkn[i]) != None):
            base[i] = dictionary.get(tkn[i])
    ''' TESTING
    print(base)
    '''
    return base