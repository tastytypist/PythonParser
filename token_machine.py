import re

def token(file_name):
# Tokenize txt file
    # read file
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    content = ignoreComment(content)
    content = content.split(" ")
    # list of operators    
    operator = [r'\+', '-', r'\*', '/', '//', '%', r'\*\*', '>', '=', '<', '<=', '>=', '!=', '&', r'\|', r'^', '~', '<<', '>>', r'\(', r'\)', r'\'', r'\"', ':', ',', '\n']
    # tokenize input for each operator
    for op in operator:
        tkn = []
        for c in content:
            splitted = re.split(r"(" + op + r")", c)
            for s in splitted:
                tkn.append(s) 
        content = [x for x in tkn if x != '' and x != '\n']
    tkn = content
    ''' TESTING
    print(tkn)
    '''
    return tkn


def ignoreComment(Str):
# Exclude comment
    Str = re.sub('#[^\n]+\n', '', Str)                  # Single-line comment
    Str = re.sub(r'\'\'\'[^\'\'\']+\'\'\'', '', Str)    # Multiline comment
    Str = re.sub(r'\"\"\"[^\"\"\"]+\"\"\"', '', Str)    # Multiline comment
    return Str