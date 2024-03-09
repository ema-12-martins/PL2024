import sys
import ply.lex as lex

state = True  # True corresponds to on
count = 0

def main(file_path):
    
    tokens = (
        'NUMBER',
        'EQUAL',
        'ON',
        'OFF',
    )
    # A regular expression rule with some action code
    def t_NUMBER(t):
        r'[+\-]?\d+'
        global count  # Declare count as a global variable
        if state == True:
            count += int(t.value) 
        return t
    
    def t_EQUAL(t):
        r'='
        global count  # Declare count as a global variable
        print(count)
        return t

    def t_ON(t):
        r'(?i)ON'
        global state  # Declare state as a global variable
        state = True
        return t
    
    def t_OFF(t):
        r'(?i)OFF'
        global state  # Declare state as a global variable
        state = False
        return t
    
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        t.lexer.skip(1)    # Skip over the letter

    # Build the lexer
    lexer = lex.lex()

    # Read the file
    with open(file_path,'r') as file:
        content = file.read()
    
    # Give the lexer some input
    lexer.input(content)
    for token in lexer:
        pass  # Printing handled in token functions

if __name__ == "__main__":
    main(sys.argv[1])
