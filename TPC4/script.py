import ply.lex as lex

def SqlLexer(data):
    tokens = (
        'OPERATION',
        'FROM',
        'WHERE',
        'VARIABLE',
        'DELIMITERS',
        'OPERAND',
        'NUMBER'
    )

    t_OPERATION = r'(?i)SELECT'
    t_FROM = r'(?i)FROM'
    t_WHERE = r'(?i)WHERE'
    t_OPERAND = r'>='
    t_DELIMITERS = r',|;'
    t_NUMBER = r'\d+'
    t_VARIABLE=r'\w+'
    t_ignore  = ' '

    def t_error(t):
        print("Illegal character '%s'" % t.value)
        t.lexer.skip(len(t.value))

    lexer = lex.lex()
    lexer.input(data)

    for tok in lexer:
        print(tok.type + ':', tok.value)
        

if __name__ == "__main__":
    data = 'SelEcT id, nome, salario frOm empregados WHere salario >= 820;'
    SqlLexer(data)