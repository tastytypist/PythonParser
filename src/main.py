import fa
import cyk
import token_machine
import sys

tkn = []
parse_table = []
invalid_var = False
first_iteration = True
print('Python Parser')
print('Type "help" for more information.')
while (True):
    if (len((sys.argv)) > 1) and first_iteration:
        command = 'py ' + str(sys.argv[1])
        print('>>> ' + command)
        first_iteration = False
    else:
        command = input('>>> ')
    if (command == 'help'):
        print('Welcome to Python Parser! Here are list of available commands:')
        print(' py <file_path>       Parsing a file')
        print(' help                 Display help menu')
        print(' quit                 Exit program')
        print(' token                Inspect code token and parse table')
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
                        error = []
                        for j in range(i-1,i+2):
                            try:
                                error.append(tkn[j])
                            except IndexError:
                                error.append('null')
                        invalid_var = True
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
                    invalid_var = False
                print("Syntax Error")
        except IOError:
            print("File not accessible")
    elif (command == 'quit'):
        break
    elif (command == 'token'):
        try:
            x = file_name   # check if variable file_name is defined
            print('Token: ')
            print(token_machine.token(file_name))
            print('Parse Table: ')
            cyk.displayParseTable(parse_table)
        except NameError:
            print("Use the parser before using the token command")
    else:
        print('Invalid command, type "help" to see available commands')
    print('')