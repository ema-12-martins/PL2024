import sys
import csv
import ply.lex as lex

state = True  # True corresponds to on
count = 0

def main():
    tokens = [
        'LISTAR',
        'SAIR',
    ]

    # A regular expression rule with some action code
    def t_LISTAR(t):
        r'LISTAR'
        for row in t.lexer.listagem:
            print(f"{row[0]} {row[1]} {row[2]}")
        return t
    
    def t_SAIR(t):
        r'SAIR'
        t.lexer.flag=1
        return t
    
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()

    # Read the file
    with open("listagem.csv",'r') as file:
        listagem = list(csv.reader(file,delimiter=';'))
    lexer.listagem=listagem
    print(listagem)
    

    lexer.flag=0
    while (lexer.flag==0):
        input_utilizador = input("Introduza a instrucao a realizar: ")
        lexer.input(input_utilizador)
        tok = lexer.token()
        if not tok:
            print("Operacao inválida")

if __name__ == "__main__":
    main()