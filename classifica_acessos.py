#Abordagem Inicial:
# 1. Separar os dados em grupos para treinos e testes
#88.9% de taxa de acerto

from dados import carregar_acessos
X,Y = carregar_acessos()

treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]



from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d ==0]
total_de_elementos = len(teste_marcacoes)
total_de_acertos  = len(acertos)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(total_de_elementos)
print(taxa_de_acerto)