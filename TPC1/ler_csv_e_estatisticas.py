import re

def ler_csv(nome_csv):
    dicionario_dados=[]

    # Abre o arquivo para leitura
    with open(nome_csv, "rt", encoding='utf-8') as f:

        #Passar a primeira linha a frente
        f.readline()

        # Lê todas as linhas do arquivo
        linhas = f.readlines()

        #Separa os argumentos pelas virgulas e tirar o \n do fim
        for linha in linhas:
            linha_separada=linha.rstrip().split(",")

            # Cria um dicionário para armazenar os dados desta linha
            linha_dict = {
                'id': linha_separada[1],
                'data': linha_separada[2],
                'nome': linha_separada[3],
                'apelido': linha_separada[4],
                'idade': linha_separada[5],
                'genero': linha_separada[6],
                'morada': linha_separada[7],
                'modalidade': linha_separada[8],
                'clube': linha_separada[9],
                'email': linha_separada[10],
                'federado': linha_separada[11],
                'resultado': linha_separada[12]
            }
            # Adiciona o dicionário à lista de dicionários
            dicionario_dados.append(linha_dict)

    return dicionario_dados

def modalidades_desportivas(dicionario_dados):
    modalidades=[]
    for elem in dicionario_dados:
        if elem['modalidade'] not in modalidades:
            modalidades.append(elem['modalidade'])
    
    modalidades.sort()
    return modalidades

def percentagem_aptos(dicionario_dados):
    contador=0
    aptos=0
    for elem in dicionario_dados:
        contador+=1
        if elem['resultado']=='true':
            aptos+=1
    
    percentagem_aptos = int(((aptos/contador)*100)+0.5)
    return percentagem_aptos

def percentagem_inaptos(dicionario_dados):
    percentagem_inaptos=100-percentagem_aptos(dicionario_dados)
    return percentagem_inaptos

def distribuicao_idades(dicionario_dados):
    distribuicoes={}
    for elem in dicionario_dados:
        # Calcula o limite inferior do intervalo
        limite_inferior = (int(elem['idade']) // 5) * 5

        # Calcula o limite superior do intervalo
        limite_superior = limite_inferior + 4

        # Formata o intervalo como uma string
        escalao = f"[{limite_inferior}-{limite_superior}]"

        if escalao in distribuicoes.keys():
            distribuicoes[escalao]+=1
        else:
            distribuicoes[escalao]=1
        
    return distribuicoes



def main():
    dicionario_dados=ler_csv("emd.csv")

    print("Modalidades Desportivas:")
    print(modalidades_desportivas(dicionario_dados))
    print("\n")

    print("Percentagem Aptos:")
    print(percentagem_aptos(dicionario_dados))
    print("\n")

    print("Percentagem Inaptos:")
    print(percentagem_inaptos(dicionario_dados))
    print("\n")

    print("Distribuicoes:")
    print(distribuicao_idades(dicionario_dados))
    print("\n")

if __name__ == "__main__":
    main()