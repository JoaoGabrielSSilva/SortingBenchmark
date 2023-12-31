# Importação das bibliotecas necessárias
from tkinter import * # Importa a biblioteca para criar a interface gráfica
from tkinter import ttk # Importa a biblioteca ttk para widgets temáticos
import random # Importa a biblioteca random para gerar números aleatórios
from bubbleSort import OrdenaBolha  # Importa uma função "OrdenaBolha" do outro arquivo (bubbleSort.py)
from quickSort import OrdenaRapidoPrincipal # Importa uma função "OrdenaBolha" do outro arquivo (bubbleSort.py)
from mergeSort import  OrdenaMescla # Importa uma função "OrdenaRapidoPrincipal" do outro arquivo (quickSort.py)
from bogoSort import bogoSort # Importa uma função "OrdenaMescla" do outro arquivo (mergeSort.py)
# Inicializa a janela principal
root = Tk()

# Configurações da janela
root.title('Visualização de Algoritmos de Ordenação') # Define o título da janela
root.maxsize(1300, 800) # Define o tamanho máximo da janela
root.config(bg='black') # Define a cor de fundo da janela como preto

# Variáveis
algoritmo_selecionado = StringVar() # Variável para armazenar o algoritmo selecionado
dados = [] # Armazena os dados a serem ordenados
quantPassos = IntVar() # Contador de passos
quantPassos.set(0) # Inicializa o contador com 0
dadosSalvos = [] # Armazena uma cópia dos dados para reiniciar a ordenação

# Função para desenhar os dados na interface
def desenharDados(dados, listaCores):
    canvas.delete("all") # Limpa o canvas
    alturaCanvas = 380
    larguraCanvas = 600
    larguraBarras = larguraCanvas / (len(dados) + 1)
    deslocamento = 10
    espacamento = 10
    dadosNormalizados = [i / max(dados) for i in dados]

    for i, altura in enumerate(dadosNormalizados):
        x0 = i * larguraBarras + deslocamento + espacamento
        y0 = alturaCanvas - altura * 340
        x1 = (i + 1) * larguraBarras + deslocamento
        y1 = alturaCanvas 
        canvas.create_rectangle(x0, y0, x1, y1, fill=listaCores[i]) # Cria um retângulo no canvas para representar cada elemento da lista
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(dados[i])) # Adiciona o valor de cada elemento como texto no retângulo
    root.update_idletasks() # Atualiza a interface

# Função para gerar dados aleatórios
def Gerar():
    global dados
    global dadosSalvos
    valMin = int(entradaMinimo.get())
    valMax = int(entradaMaximo.get())
    tamanho = int(entradaQuantidade.get())

    dados = []
    #Gera um valor aleatório na quantidade especificada
    for _ in range(tamanho):
        dados.append(random.randrange(valMin, valMax + 1))
    
    #Cada valor gerado é passado para a lista dadosSalvos para ter a possibilidade de reiniciar a ordenação
    for i in range(tamanho):
        dadosSalvos.append(dados[i])
    
    desenharDados(dados, ['yellow' for x in range(len(dados))])

#Função para reiniciar para a lista de dados inicial sem ordenação
def ReiniciarOrdenacao():
    global dadosSalvos
    global dados
    quantPassos.set(0)
    if not dados: return
    tamanho = int(entradaQuantidade.get())
    dados = []
    for _ in range(tamanho):
        dados.append(dadosSalvos[_])

    desenharDados(dados, ['yellow' for x in range(len(dados))])
    
# Função para iniciar o algoritmo de ordenação
def IniciarAlgoritmo():
    global dados
    if not dados: return

    #Escolha do algoritmo de ordenação
    if menuAlgoritmo.get() == 'Quick Sort':
        quantPassos.set(OrdenaRapidoPrincipal(dados, 0, len(dados) - 1, desenharDados, escalaVelocidade.get())) 
        # Chama a função de ordenação do Quick Sort e atualiza o contador de passos
    elif menuAlgoritmo.get() == 'Bubble Sort':
        quantPassos.set(OrdenaBolha(dados, desenharDados, escalaVelocidade.get())) 
        # Chama a função de ordenação do Bubble Sort e atualiza o contador de passos
    elif menuAlgoritmo.get() == 'Merge Sort':
        quantPassos.set(OrdenaMescla(dados, desenharDados, escalaVelocidade.get())) 
        # Chama a função de ordenação do Merge Sort e atualiza o contador de passos
    elif menuAlgoritmo.get() == 'Bogo Sort':
        quantPassos.set(bogoSort(dados, desenharDados, escalaVelocidade.get())) 
        # Chama a função de ordenação do Bogo Sort e atualiza o contador de passos
    desenharDados(dados, ['green' for x in range(len(dados))])
# Criação da interface
# frameInterface é a janela principal do programa
frameInterface = Frame(root, width=200, height=380, bg='grey')
frameInterface.grid(row=0, column=0, padx=5, pady=5)

#Canvas é a área onde as ordenações serão desenhadas
canvas = Canvas(root, width=700, height=380, bg='white')
canvas.grid(row=0, column=1, padx=5, pady=5)

# Parte da Interface do Usuário
# Parte com a seleção do tipo de algoritmo para ordenação
Label(frameInterface, text="Algoritmo: ", bg='grey').grid(row=0, column=0, padx=5, sticky=W)
menuAlgoritmo = ttk.Combobox(frameInterface, textvariable=algoritmo_selecionado, values=[
    'Bubble Sort','Quick Sort', 'Merge Sort', 'Bogo Sort' ])
menuAlgoritmo.grid(row=0, column=1, padx=5, pady=5)
menuAlgoritmo.current(0)

#Contador de Passos
Label(frameInterface, text="Passos: ", bg='grey').grid(row=1, column=0, padx=5, sticky=W)
Label(frameInterface, textvariable= quantPassos, bg='grey').grid(row=1, column=1, padx=5, sticky=W)

#Botão para reiniciar a ordenação
Button(frameInterface, text="Reset", command=ReiniciarOrdenacao, bg='red').grid(row=2, column=0, padx=5, pady=5)

# Campo de texto "Valor Mínimo"
entradaMinimo = Scale(frameInterface, from_=0, to=10, digits=2, resolution=1, orient=HORIZONTAL, label="Valor Mínimo")
entradaMinimo.grid(row=3, column=0, padx=5, pady=5)

# Campo de texto "Valor Máximo"
entradaMaximo = Scale(frameInterface, from_=10, to=100, digits=2, resolution=1, orient=HORIZONTAL, label="Valor Máximo")
entradaMaximo.grid(row=3, column=1, padx=5, pady=5)

#Velocidade
escalaVelocidade = Scale(frameInterface, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=VERTICAL, label='''Duração do Passo:(Em Segundos)''')
escalaVelocidade.grid(row=4, column=0, padx=5, pady=5)

# Campo de texto "Quantidade"
entradaQuantidade = Scale(frameInterface, from_=25, to=3, digits=2, resolution=1, orient=VERTICAL, label="Quantidade")
entradaQuantidade.grid(row=4, column=1, padx=5, pady=5)

#Botão para gerar um conjunto de dados
Button(frameInterface, text="Gerar", command=Gerar, bg='white').grid(row=5, column=0, padx=5, pady=5)

#Botão para iniciar a ordenação
Button(frameInterface, text="Iniciar", command=IniciarAlgoritmo, bg='green').grid(row=5, column=1, padx=5, pady=5)



root.mainloop()
