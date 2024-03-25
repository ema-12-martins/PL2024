T = {'+','-','*','/','!','?',')','('}


Expr -> Term Expr'

Expr' -> + Term Expr' 
        | - Term Expr'
        | ε

Term -> Factor Term'

Term' -> * Factor Term' 
        | / Factor Term' 
        | ε

Factor -> (Expr) 
        | Number

Number -> Digit Number' 
        | Digit

Number' -> Digit Number' |
         ε

Digit -> 0 
        | 1 
        | 2 
        | 3 
        | 4 
        | 5 
        | 6 
        | 7 
        | 8 
        | 9
