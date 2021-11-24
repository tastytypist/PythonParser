# Python Parser  
**Python Parser** is a Python program syntax evaluator that can 
be used to determine whether a given Python code is syntactically 
correct or not.  

Supported keywords:

| __False__  |    __as__    |   __def__    |   __from__   |    __is__    |  __raise__   |
|:----------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|  __None__  |  __break__   |   __elif__   |    __if__    |   __not__    |  __return__  |
|  __True__  |  __class__   |   __else__   |  __import__  |    __or__    |  __while__   |
|  __and__   | __continue__ |   __for__    |    __in__    |   __pass__   |   __with__   |

## Project Structure  
```
python_parser
├── doc                     # Contains documentation in the form or a report
├── grammar
│   ├── cfg.txt             # Contains Context-Free Grammar for the program
│   └── cnf.txt             # Contains Chomsky Normal Form for the program
├── src
│   ├── cfg_cnf.py          # Contains functions for CFG to CNF conversion
│   ├── cnf_helper.py       # Contains utility functions for cfg_cnf.py
│   ├── cyk.py              # Contains an implementation of Cocke–Younger–Kasami algorithm
│   ├── fa.py               # Contains FA for checking variables and numbers validity
│   ├── main.py             # Contains the main program
│   └── token_machine.py    # Contains functions for tokenisation
├── test                    # Contains test cases
├── .gitignore
└── README.md
```

## Setup  
1. Change directory to `src` using `cd src`
2. Run the program using `python main.py`
3. Use the `help` command to show the list of commands
