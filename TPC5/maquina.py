import csv
import re
import ply.lex as lex

def main():
    tokens = [
        'LISTAR',
        'SAIR',
        'SALDO',
        'MOEDA',
        'SELECIONAR',
    ]
    
    # A regular expression rule with some action code
    def t_LISTAR(t):
        r'LISTAR'
        for row in t.lexer.listagem:
            print(f"{row[0]}----->{row[1]}----->{row[2]}")
        return t
    
    def t_SAIR(t):
        r'SAIR'
        print(f"Troco: {t.lexer.saldo}")
        t.lexer.flag=1
        return t
    
    def t_SALDO(t):
        r'SALDO'
        print(f"Saldo disponivel: {int(t.lexer.saldo/100)}e {t.lexer.saldo%100}c")
        return t

    def t_MOEDA(t):
        r'MOEDA((\s(5|10|20|50)c)|\s(1|2)e)+'
        matches_digits = re.findall(r'\d{1,2}', t.value)  
        matches_e_c = re.findall(r'[ec]', t.value)      
        groups = list(zip(matches_digits, matches_e_c)) 
        for elem in groups:
            if elem[1] =='c':
                t.lexer.saldo+=int(elem[0])
            else:
                t.lexer.saldo+=int(elem[0])*100

        return t

    def t_SELECIONAR(t):
        r'SELECIONAR\s(\d)+'
        product= int(re.findall(r'(\d)+', t.value)[0])
        if product>=0 and product<len(t.lexer.listagem):
            price=t.lexer.listagem[product][2]
            price_list=price.split(" ")

            final_price=0
            for elem in price_list:
                if elem[-1]=='e':
                    final_price+=int(elem[:-1])*100
                else:
                    final_price+=int(elem[:-1])
            
            if final_price<t.lexer.saldo:
                t.lexer.saldo-=final_price
                print("Produto adquirido")
            else:
                print("Saldo insuficiente")

        else:
            print("Produto indisponível!")
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

    

    lexer.flag=0
    lexer.saldo=0
    while (lexer.flag==0):
        input_utilizador = input("Introduza a instrucao a realizar: ")
        lexer.input(input_utilizador)
        tok = lexer.token()
        if not tok:
            print("Operacao inválida")

if __name__ == "__main__":
    main()