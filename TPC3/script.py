import re
import sys

def main():
    conteudo = sys.stdin.read()
    divisao = re.split(r'=|on|off', conteudo, flags=re.IGNORECASE | re.DOTALL)
    divisorios = re.findall(r'on|off|=', conteudo, flags=re.IGNORECASE | re.DOTALL)
    print(divisao)
    print(divisorios)

    i=0
    soma=0
    estado="on"
    estado_anterior="on"
    while i<len(divisao):
        if(estado=="on"):
            soma+=sum(map(int,re.findall(r'[+\-]?\d+',divisao[i])))
            estado_anterior=="on"
        elif(estado=="="):
            print(soma)
            if(estado_anterior=="on"):
                soma+=sum(map(int,re.findall(r'[+\-]?\d+',divisao[i])))
        elif(estado=="off"):
            estado_anterior=="off"

        if(i<len(divisorios)):
            estado=divisorios[i]
        i+=1

if __name__ == "__main__":
    main()