# File name: fa.py
# Goal: checks variable name validity in Python

# Q (states): q0 (0), q1 (1), q2 (2)
# Sigma (input alphabet): ASCII chars
# Delta (transition function): (shown in diagram)
# q0 (start state): q0 (0)
# F (final state): q1 (1)
# q2 (2) is dead state

# implementing most primitive method

def validVarName(varName):
    # Goal: returns true if variable name is valid
    state = 0
    for char in varName:
        if (state == 0):
            if (char.isalpha() or char == '_'):
                state = 1
            else:
                state = 2
        elif (state == 1):
            if (char.isalnum() or char == '_'):
                state = 1
            else:
                state = 2
        elif (state == 2): # to create valid FA
            state = 2
    return (state == 1)

def allVarNameValid(varNames):
    for varName in varNames:
        if (not(validVarName(varName))):
            return False
    return True

'''
for checking purposes
print(validVarName('varsaya')) # True

arrVar = ['varsaya', 'var_saya', '_var_saya', 'varSaya', 'VARSAYA', 'varsaya2', 'var saya']
print(allVarNameValid(arrVar)) # False
'''