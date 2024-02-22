# TPC2

**Autor:** Ema Maria Monteiro Martins

**Nº:** A97678

**Descrição do trabalho:**
Pretende-se fazer um conversor de Markdown para HTML.
Para o efeito, utilizou-se expressões regex para susbtituir as tags de Markdown para HTML, seguindo o seguinte padrao:

\*\*texto \*\* -> <b>texto</b>

--texto-- -> <b>texto</b>

\*texto \* -> <i>texto</i>

-texto- -> <i>texto</i>

\# texto -> &lt;h1&gt;texto&lt;/h1&gt;

\#### texto -> &lt;h4&gt;texto&lt;/h4&gt;

\[texto\]\(url\) -> &lt;a href=url&gt;texto&lt;/a&gt;

\!\[texto\]\(imagem\) -> &lt;img src=imagem alt=texto&gt;

As listas ordenadas ainda seguem o seguinte padrão:
1. texto1
2. texto2
3. texto3

~~~
<ol>
    <li>texto1</li>
    <li>texto2</li>
    <li>texto3</li>
</ol>
~~~




