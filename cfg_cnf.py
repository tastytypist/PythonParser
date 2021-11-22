# This file contains modified portions of code by Adel Massimo Ramadan

# Copyright (c) 2018 Adel Massimo Ramadan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-
# It's assumed that starting variable is the first typed
import sys
import cnf_helper

left, right = 0, 1

terminal, variable, products = [], [], []
variables_jar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1",
                 "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "W1",
                 "X1", "Y1", "Z1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
                 "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2",
                 "T2", "U2", "V2", "W2", "X2", "Y2", "Z2", "A3", "B3", "C3", "D3",
                 "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3",
                 "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
                 "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4",
                 "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4",
                 "W4", "X4", "Y4", "Z4"]


def is_unitary(rule, variables):
    if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
        return True
    return False


def is_simple(rule):
    if rule[left] in variable and rule[right][0] in terminal and len(rule[right]) == 1:
        return True
    return False


for nonTerminal in variable:
    if nonTerminal in variables_jar:
        variables_jar.remove(nonTerminal)


# Add S0->S rule
def start(productions, variables):
    variables.append('S0')
    return [('S0', [variables[0]])] + productions


# Remove rules containing both terms and variables, like A->Bc, replacing by A->BZ and Z->c
def delete_mixed_terms(productions, variables):
    new_productions = []
    # create a dictionary for all base production, like A->a, in the form dic['a'] = 'A'
    dictionary = cnf_helper.setup_dict(productions, variables, terms=terminal)
    for production in productions:
        # check if the production is simple
        if is_simple(production):
            # in that case there is nothing to change
            new_productions.append(production)
        else:
            for term in terminal:
                for index, value in enumerate(production[right]):
                    if term == value and term not in dictionary:
                        # it's created a new production variable->term and added to it
                        dictionary[term] = variables_jar.pop()
                        # Variables set it's updated adding new variable
                        variable.append(dictionary[term])
                        new_productions.append((dictionary[term], [term]))

                        production[right][index] = dictionary[term]
                    elif term == value:
                        production[right][index] = dictionary[term]
            new_productions.append((production[left], production[right]))

    # merge created set and the introduced rules
    return new_productions


# Eliminate non unitary rules
def delete_unitary(productions, variables):
    result = []
    for production in productions:
        k = len(production[right])
        # newVar = production[left]
        if k <= 2:
            result.append(production)
        else:
            new_var = variables_jar.pop(0)
            variables.append(new_var + '1')
            result.append((production[left], [production[right][0]] + [new_var + '1']))
            for i in range(1, k - 2):
                var, var2 = new_var + str(i), new_var + str(i + 1)
                variables.append(var2)
                result.append((var, [production[right][i], var2]))
            result.append((new_var + str(k - 2), production[right][k - 2:k]))
    return result


# Delete non terminal rules
def delete_nonterminal(productions):
    new_set = []
    # seekAndDestroy throw back in:
    #        – outlaws all left side of productions such that right side is equal to the outlaw
    #        – productions the productions without outlaws
    outlaws, productions = cnf_helper.seek_and_destroy(target='e', productions=productions)
    # add new reformulation of old rules
    for outlaw in outlaws:
        # consider every production: old + new resulting important when more than one outlaws are in the same prod.
        for production in productions + [e for e in new_set if e not in productions]:
            # if outlaw is present in the right side of a rule
            if outlaw in production[right]:
                # the rule is rewritten in all combination of it, rewriting "e" rather than outlaw
                # this cycle prevent to insert duplicate rules
                new_set = new_set + [e for e in cnf_helper.rewrite(outlaw, production) if e not in new_set]

    # add unchanged rules and return
    return new_set + ([productions[i] for i in range(len(productions))
                      if productions[i] not in new_set])


def unit_routine(rules, variables):
    unitaries, result = [], []
    # check if a rule is unitary
    for aRule in rules:
        if is_unitary(aRule, variables):
            unitaries.append((aRule[left], aRule[right][0]))
        else:
            result.append(aRule)
    # otherwise I check if I can replace it in all the others
    for uni in unitaries:
        for rule in rules:
            if uni[right] == rule[left] and uni[left] != rule[left]:
                result.append((uni[left], rule[right]))

    return result


def create_unit(productions, variables):
    i = 0
    result = unit_routine(productions, variables)
    tmp = unit_routine(result, variables)
    while result != tmp and i < 1000:
        result = unit_routine(tmp, variables)
        tmp = unit_routine(result, variables)
        i += 1
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        modelPath = str(sys.argv[1])
    else:
        modelPath = 'cfg.txt'

    terminal, variable, products = cnf_helper.load_model(modelPath)

    products = start(products, variables=variable)
    products = delete_mixed_terms(products, variables=variable)
    products = delete_unitary(products, variables=variable)
    products = delete_nonterminal(products)
    products = create_unit(products, variables=variable)

    print(cnf_helper.pretty_form(products))
    print(len(products))
    open('cnf.txt', 'w').write(cnf_helper.pretty_form(products))
