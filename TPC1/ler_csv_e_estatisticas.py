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
    
    #Imprimir as modalidades desportivas
    print("..........Modalidades...........")
    for modalidade in modalidades:
        print(f"-{modalidade}")

def calcula_percentagem_aptos(dicionario_dados):
    contador=0
    aptos=0
    for elem in dicionario_dados:
        contador+=1
        if elem['resultado']=='true':
            aptos+=1
    
    percentagem_aptos = int(((aptos/contador)*100)+0.5)
    return percentagem_aptos

def percentagem_aptos(dicionario_dados):

    #Percentagem de aptos
    print(".......Percentagem de aptos.......")
    print(calcula_percentagem_aptos(dicionario_dados))

def percentagem_inaptos(dicionario_dados):
    percentagem_inaptos=100-calcula_percentagem_aptos(dicionario_dados)
    
    #Percentagem de inaptos
    print(".......Percentagem de inaptos.......")
    print(percentagem_inaptos)

def distribuicao_idades(dicionario_dados):
    distribuicoes={}
    contador=0

    for elem in dicionario_dados:
        contador+=1

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

    #Ordenar alfabeticamente e depois imprimir
    keys_dist=list(distribuicoes.keys())
    keys_dist.sort()

    print(".....Distribuicao de idades dos atletas.....")
    for k in keys_dist:
        percentagem = (distribuicoes[k] / contador) * 100
        print(f"{k}: {distribuicoes[k]} ({percentagem:.2f}%)")



def main():
    dicionario_dados=ler_csv("emd.csv")
    
    #Estatisticas
    modalidades_desportivas(dicionario_dados)
    print("\n")
    percentagem_aptos(dicionario_dados)
    print("\n")
    percentagem_inaptos(dicionario_dados)
    print("\n")
    distribuicao_idades(dicionario_dados)

if __name__ == "__main__":
    main()