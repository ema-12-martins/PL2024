import re
import sys


def main(path):
    #Cabecalho inicial do HTML
    html='''
    <!DOCTYPE htlm>
    <html>
    <head>
        <title>EngWeb2024</title>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: Arial, sans-serif;
            }
        </style>
    </head>
    <body>

    '''

    with open(path, 'r') as arquivo:
        conteudo = arquivo.read()

        #Titulos
        conteudo = re.sub(r"#{6}(.*)\n", r"<h6>\1</h6>", conteudo)
        conteudo = re.sub(r"#{5}(.*)\n", r"<h5>\1</h5>", conteudo)
        conteudo = re.sub(r"#{4}(.*)\n", r"<h4>\1</h4>", conteudo)
        conteudo = re.sub(r"#{3}(.*)\n", r"<h3>\1</h3>", conteudo)
        conteudo = re.sub(r"#{2}(.*)\n", r"<h2>\1</h2>", conteudo)
        conteudo = re.sub(r"#(.*)\n", r"<h1>\1</h1>", conteudo)

        #Italicos e Bolds
        conteudo = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", conteudo, flags=re.DOTALL) #Para fazer com que o . a qualquer caracter, inclusive o \n
        conteudo = re.sub(r"--(.*?)--", r"<b>\1</b>", conteudo, flags=re.DOTALL) #O ? serve para ver o menor possivel para substituir, nao indo verificar a expressao seguinte
        conteudo = re.sub(r"\*(.*?)\*", r"<i>\1</i>", conteudo, flags=re.DOTALL) 
        conteudo = re.sub(r"-(.*?)-", r"<i>\1</i>", conteudo, flags=re.DOTALL) 

        #Imagens
        conteudo = re.sub(r"\!\[(.*?)\]\((.*?)\)",  r"<img src='\2' alt='\1'>", conteudo, flags=re.DOTALL) 

        #Links
        conteudo = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", conteudo, flags=re.DOTALL) 

        #Listas
        conteudo = re.sub(r"^\d+\. (.*)", r"<li>\1</li>", conteudo, flags=re.MULTILINE)
        conteudo = f"<ol>{conteudo}</ol>"
        
        #Paragrafos
        conteudo = re.sub(r"\n\n", r"</p><p>", conteudo, flags=re.DOTALL) 
        print(conteudo)

        #Para terminar a pagina principal
        conteudo+="</ul>"
        conteudo+="</body>"
        conteudo+="</html>"

        #Para criar a pagina propriamente dita
        file = open(f"conversor_md_html.html","w",encoding="utf-8")
        file.write(conteudo)
        file.close()

    

if __name__ == "__main__":
    main(sys.argv[1])