import re

def token(file_name):
    file = open(file_name, 'r')
    content = file.read()
    file.close()

    content = ignoreComment(content)
    print(content, "\n")
    content = content.split(" ")
    
    operator = [r'\+', '-', r'\*', '/', '//', '%', r'\*\*', '>', '=', '<', '<=', '>=', '!=', '&', r'\|', r'^', '~', '<<', '>>', r'\(', r'\)', r'\'', r'\"', ':', ',', '\n']
    
    for op in operator:
        tkn = []
        for c in content:
            splitted = re.split(r"(" + op + r")", c)
            for s in splitted:
                tkn.append(s) 
        content = [x for x in tkn if x != '']
    tkn = content
    print(tkn)
    return tkn


def ignoreComment(Str):
    Str = re.sub('#[^\n]+\n', '', Str)                  # Single-line comment
    Str = re.sub(r'\'\'\'[^\'\'\']+\'\'\'', '', Str)    # Multiline comment
    return Str


token('test.py')