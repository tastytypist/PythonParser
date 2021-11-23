import fa
import cyk
import token_machine

tkn = []
parse_table = []
invalid_var = False
print('Python Parser')
print('Type "help" for more information.')
while (True):
    command = input('>>> ')
    if (command == 'help'):
        print('Welcome to Python Parser! Here are list of available commands:')
        print(' py <file_path>       Parsing a file')
        print(' help                 Display help menu')
        print(' quit                 Exit program')
    elif (command[0:3] == 'py '):
        # input python source code
        file_name = command[3:]
        try:
            file = open(file_name)
            file.close()
            # tokenize python file
            tkn = token_machine.token(file_name)

            # input CNF (.txt) file
            dict = cyk.cnf_to_dictionary('../grammar/cnf.txt')

            # base of CYK parsing table
            base = cyk.cykBase(tkn, dict)

            # varible and number checking (FA)
            for i in range (len(base)):
                x = base[i]
                if (not bool(x)):
                    if (fa.validVarName(tkn[i])):
                        tkn[i] = 'variable'
                    elif (fa.validNum(tkn[i])):
                        tkn[i] = 'number'
                    else:
                        error = [tkn[i-1],tkn[i],tkn[i+1]]
                        invalid_var = True
                        tkn[i] = 'exception'
            ''' TESTING
            print(tkn)
            '''
            # syntax checking (CYK)
            result, parse_table = cyk.cyk(tkn, dict)
            if (result):
                print("Accepted")
            else:
                if (invalid_var):
                    line, column, content = token_machine.findError(file_name, error)
                    print('  ' + content)
                    print('  ' + ' '*(column) + '^ invalid variable in line ' + str(line))
                print("Syntax Error")
        except IOError:
            print("File not accessible")
    elif (command == 'quit'):
        break
    elif (command == 'token'):
        print('Token: ')
        print(token_machine.token(file_name))
        print('Parsing Table: ')
        cyk.displayParseTable(parse_table)
    else:
        print('Invalid command, type "help" to see available commands')
    print('')