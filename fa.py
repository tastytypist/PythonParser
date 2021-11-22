# File name: fa.py
# Goal: checks variable name validity in Python

# Variable Name DFA:
# Q (states): q0 (0), q1 (1), q2 (2)
# Sigma (input alphabet): ASCII chars
# Delta (transition function): (shown in diagram)
# q0 (start state): q0 (0)
# F (final state): q1 (1)
# q2 (2) is dead state

# Number DFA:
# Q (states): q0 (0), q1 (1), q2 (2), q3 (3), q4 (4), q5 (5), q6 (6), q7 (7), q8 (8)
# Sigma (input alphabet): numeric (0-9), point ('.'), plus ('+'), minus ('-'), 'E'
# Delta (transition function): (shown in diagram)
# q0 (start state): q0 (0)
# F (final state): q1 (1), q2 (2), q3 (3), q5 (5)
# q8 (8) is dead state

# implementing most primitive method

alphaBig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphaSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def validVarName(varName):
    # Goal: returns true if variable name is valid (i.e. accepted string of FA)
    state = 0
    for char in varName:
        if (state == 0):
            # if (char.isalpha() or char == '_'):
            if (char in alphaBig or char in alphaSmall or char == '_'):
                state = 1
            else:
                state = 2
        elif (state == 1):
            # if (char.isalnum() or char == '_'):
            if (char in alphaBig or char in alphaSmall or char in num or char == '_'):
                state = 1
            else:
                state = 2
        elif (state == 2): # to create valid FA
            state = 2
    return (state == 1)

def allVarNameValid(varNames):
    # Goal: returns true if all variable names are valid (i.e. accepted string in FA)
    for varName in varNames:
        if (not(validVarName(varName))):
            return False
    return True

def validNum(input):
    # Goal: returns true if string is a number (i.e. accepted string of FA)
    state = 0
    for char in input:
        if (state == 0):
            if (char in num):
                state = 1
            elif (char == '+' or char == '-'):
                state = 6
            else:
                state = 8
        elif (state == 1):
            if (char in num):
                state = 1
            elif (char == '.'):
                state = 2
            else:
                state = 8
        elif (state == 2):
            if (char in num):
                state = 3
            else:
                state = 8
        elif (state == 3):
            if (char in num):
                state = 3
            elif (char == 'E'):
                state = 4
            else:
                state = 8
        elif (state == 4):
            if (char in num):
                state = 5
            elif (char == '+' or char == '-'):
                state = 7
            else:
                state = 8
        elif (state == 5):
            if (char in num):
                state = 5
            else:
                state = 8
        elif (state == 6):
            if (char in num):
                state = 1
            else:
                state = 8
        elif (state == 7):
            if (char in num):
                state = 1
            else:
                state = 8
        elif (state == 8):
            state = 8   
    return (state == 1 or state == 2 or state == 3 or state == 5)

'''
# for checking purposes
print(validVarName('varsaya')) # True

arrVar = ['varsaya', 'var_saya', '_var_saya', 'varSaya', 'VARSAYA', 'varsaya2']
print(allVarNameValid(arrVar)) # True

print(validNum('-123.4E-5')) # True
'''