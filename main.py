import fa
import cyk
import token_machine

# input python source code
file_name = input("Python source code path: ")
# tokenize python file
tkn = token_machine.token(file_name)

# input CNF (.txt) file
dict = cyk.cnf_to_dictionary('cnf.txt')

# base of CYK parsing table
base = cyk.cykBase(tkn, dict)

# varible and number checking (FA)
var = []
num = []
invalidWord = False
for i in range (len(base)):
    x = base[i]
    if (not bool(x)):
        if (fa.validVarName(tkn[i])):
            var.append(tkn[i])
        else:
            if (fa.validNum(tkn[i])):
                num.append(tkn[i])
            else:
                invalidWord = True
                break

if (not invalidWord):
    # replace variables and numbers in tkn
    for v in var:
        for i in range (len(tkn)):
            if (v == tkn[i]):
                tkn[i] = 'variable'
    for n in num:
        for i in range (len(tkn)):
            if (n == tkn[i]):
                tkn[i] = 'number'
    ''' TESTING
    print(tkn)
    '''
    # syntax checking (CYK)
    if(cyk.cyk(tkn, dict)):
        print("Accepted\n")
    else:
        print("Syntax Error\n")
else:
    print("Syntax Error\n")