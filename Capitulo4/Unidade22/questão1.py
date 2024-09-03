import re

# Documento HTML
html_document = """
<html>
<body>
<h1>Olá, Mundo!</h1>
<p>Estamos aprendendo a arte da codificação
com a linguagem de programação Python.
Aqui estamos aprendendo...</p>
<ul>
<li>Estruturas de Dados,</li>
<li>Algoritmos,</li>
<li>e Pensamento Computacional,
eventualmente.</li>
</ul>
</body>
</html>
"""

# Expressão regular para capturar o conteúdo entre as tags HTML
pattern = re.compile(r'<.*?>(.*?)</.*?>', re.DOTALL)
matches = pattern.findall(html_document)

# Exibir o conteúdo extraído
for match in matches:
    print(match.strip())