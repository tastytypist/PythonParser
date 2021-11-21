import cyk
import token_machine

# input file yang akan di-parsing
file_name = input("Python source code path: ")
tkn = token_machine.token(file_name)

# input file production rule dalam bentuk cnf
dict = cyk.cnf_to_dictionary('testcnf.txt')

# parsing dengan cyk
if(cyk.cyk(tkn,dict)):
    print("Accepted\n")
else:
    print("Syntax Error\n")