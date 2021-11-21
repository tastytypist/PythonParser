import re

def token(file_name):
# mendekomposisi python file menjadi token
    # load file
    file = open(file_name, 'r')
    content = file.read()
    file.close()

    content = ignoreComment(content)
    content = content.split(" ")

    # list operator    
    operator = [r'\+', '-', r'\*', '/', '//', '%', r'\*\*', '>', '=', '<', '<=', '>=', '!=', '&', r'\|', r'^', '~', '<<', '>>', r'\(', r'\)', r'\'', r'\"', ':', ',', '\n']
    
    # tokenisasi
    for op in operator:
        tkn = []
        for c in content:
            splitted = re.split(r"(" + op + r")", c)
            for s in splitted:
                tkn.append(s) 
        content = [x for x in tkn if x != '']
    tkn = content
    return tkn


def ignoreComment(Str):
# Meng-exclude comment dari proses parsing
    Str = re.sub('#[^\n]+\n', '', Str)                  # Single-line comment
    Str = re.sub(r'\'\'\'[^\'\'\']+\'\'\'', '', Str)    # Multiline comment
    Str = re.sub(r'\"\"\"[^\"\"\"]+\"\"\"', '', Str)    # Multiline comment
    return Str