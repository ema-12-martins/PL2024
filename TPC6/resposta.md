
# Definição da gramática
~~~
T = {VARIAVEL,SINAL,NUM,'!','?','=','(',')'}

N = {Problema, Expressao, Expressao2, Conta}

S = Problema

P = {

(p1) Problema -> '!' Expressao
(p2)          | '?' VARIAVEL
(p3)          | VARIAVEL '=' Expressao

(p4)  Expressao -> Conta Expressao2
(p5)            | '(' Expressao ')' Expressao2
(p6)            | NUM

(p7)  Expressao2 -> SINAL Expressao
(p8)             | &

(p9) Conta -> NUM SINAL NUM
}
~~~

# LAs
~~~
LA(p1) = {'!'}
LA(p2) = {'?'}
LA(p3) = {'VARIAVEL'}
LA(p4) = {NUM}
LA(p5) = {'('}
LA(p6) = {NUM}
LA(p7) = {SINAL}
LA(p8) = {'$'}
LA(p9) = {NUM}
~~~
