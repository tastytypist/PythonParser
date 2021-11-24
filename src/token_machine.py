import re

def token(file_name):
# Tokenize txt file
    # read file
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    content = ignoreComment(content)
    content = re.sub(r'\'[\x00-\x7F][^\'\"]*\'', 'string', content) 
    content = re.sub(r'\"[\x00-\x7F][^\'\"]*\"', 'string', content) 
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


def findError(file_name, error):
# find error line (invalid variable)
    file = open(file_name, 'r')
    contents = file.readlines()
    line = 0
    for content in contents:
        line += 1
        i = content.find(error[0])
        j = content.find(error[1])
        k = content.find(error[2])
        if (i != -1 and j != -1) or (j != -1 and k != -1):
            break
    content = content.replace('\n', '')
    return line, j, content