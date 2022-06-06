import webbrowser

# função de Pesquisa no Site da Americanas
def pesquisa_americanas(p1,p2,p3):
    url = "https://www.americanas.com.br/busca/{}-{}-{}".format(p1,p2,p3)
    webbrowser.open(url)

# Função de pesquisa no site da Kabum
def pesquisa_Kabum(p1,p2,p3):
    url = "https://www.kabum.com.br/busca?query={}+{}+{}".format(p1,p2,p3)
    webbrowser.open(url)

# Função de pesquisa no site da Google
def pesquisa_google(p1,p2,p3):
    url = "https://www.google.com/search?q={}+{}+{}".format(p1,p2,p3)
    webbrowser.open(url)

# Função de pesquisa no site da Mercado Livre
def pesquisa_mercado_livre(p1,p2,p3):
    url = "https://lista.mercadolivre.com.br/{}-{}-{}".format(p1,p2,p3)
    webbrowser.open(url)

# Função de pesquisa no site da Amazon

def pesquisa_amazon(p1, p2, p3):
    url = "https://www.amazon.com.br/s?k={}+{}+{}".format(p1, p2, p3)
    webbrowser.open(url)

