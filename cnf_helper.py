# Copyright (c) 2018 Adel Massimo Ramadan
# Copyright (c) 2021 tastytypist
#
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

import itertools

left, right = 0, 1


def union(lst1, lst2):
    final_list = list(set().union(lst1, lst2))
    return final_list


def load_model(model_path):
    file = open(model_path).read()
    terminals = (file.split("Variables:\n")[0].replace("Terminals:\n", "").replace("\n", ""))
    variables = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n", "").replace("\n", ""))
    productions = (file.split("Productions:\n")[1])

    return clean_alphabet(terminals), clean_alphabet(variables), clean_production(productions)


# Make production easy to work with
def clean_production(expression):
    result = []
    # remove spaces and explode on ";"
    raw_rules = expression.replace('\n', '').split(';')

    for rule in raw_rules:
        # Explode every rule on "->" and make a couple
        left_side = rule.split(' -> ')[0].replace(' ', '')
        right_terms = rule.split(' -> ')[1].split(' | ')
        for term in right_terms:
            result.append((left_side, term.split(' ')))
    return result


def clean_alphabet(expression):
    return expression.replace('  ', ' ').split(' ')


def seek_and_destroy(target, productions):
    trash, erased = [], []
    for production in productions:
        if target in production[right] and len(production[right]) == 1:
            trash.append(production[left])
        else:
            erased.append(production)

    return trash, erased


def setup_dict(productions, variables, terms):
    result = {}
    for production in productions:
        #
        if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result


def rewrite(target, production):
    result = []
    # get positions corresponding to the occurrences of target in production right side
    # positions = [m.start() for m in re.finditer(target, production[right])]
    positions = [i for i, x in enumerate(production[right]) if x == target]
    # for all found targets in production
    for i in range(len(positions) + 1):
        # for all combinations of all possible length phrases of targets
        for element in list(itertools.combinations(positions, i)):
            # Example: if positions is [1 4 6]
            # now i've got: [] [1] [4] [6] [1 4] [1 6] [4 6] [1 4 6]
            # erase position corresponding to the target in production right side
            target_res = [production[right][i] for i in range(len(production[right])) if i not in element]
            if target_res:
                result.append((production[left], target_res))
    return result


def dict_to_set(dictionary):
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    return result


def print_rules(rules):
    for rule in rules:
        tot = ""
        for term in rule[right]:
            tot = tot + " " + term
        print(rule[left] + " -> " + tot)


def pretty_form(rules):
    dictionary = {}
    for rule in rules:
        if rule[left] in dictionary:
            dictionary[rule[left]] += ' | ' + ' '.join(rule[right])
        else:
            dictionary[rule[left]] = ' '.join(rule[right])
    result = ""
    for key in dictionary:
        result += key + " -> " + dictionary[key] + "\n"
    return result
