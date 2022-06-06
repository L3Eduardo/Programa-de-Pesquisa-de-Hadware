from tkinter import*
from tkinter import ttkttk
from Funcoes_gerais import*

janela = Tk()

#Título da Janela
janela.title('Ferramenta de Pesquisa')
janela.geometry("300x300")
janela.config(background = '#0E7535')
janela.resizable(False, False)

# Label de descrição,tipo e marca.
label_descricao = Label(text="Descrição do Material")
label_descricao.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.08)
###
label_tipo_unidade = Label(text="Equipamento")
label_tipo_unidade.place(relx=0.09, rely=0.3, relwidth=0.3, relheight=0.08)
###
label_quant = Label(text="Marca do equipamento")
label_quant.place(relx=0.02, rely=0.45, relwidth=0.45, relheight=0.08)
###
label_pesquisa = Label(text="Formas de Pesquisa")
label_pesquisa.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.08)

#  Entrada; Descrição, tipo e Marca.
entry_descricao = Entry()
entry_descricao.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.08)
###
lista_tipos = ["RAM","SSD","HD", "Placa de Video","Cooler","Processador","Placa Mãe","Fonte de Alimentação" ]
#
selecionar_tipo = ttk.Combobox(values=lista_tipos)
selecionar_tipo.place(relx=0.42, rely=0.3, relwidth=0.4, relheight=0.08)
###
entry_marca = Entry()
entry_marca.place(relx=0.5, rely=0.45, relwidth=0.45, relheight=0.08)

## Botões de Pesquisar

#  Botão de Pesquisa do Google
botao_1 = Button(text="Google", command =lambda: [pesquisa_google(p1=entry_descricao.get(),p2=selecionar_tipo.get(),p3=entry_marca.get())])
botao_1.place(relx=0.16, rely=0.69, relwidth=0.2, relheight=0.1)
#  Botao de Pesquisa da Americanas
botao_2 = Button(text="Amaricanas", command =lambda: [pesquisa_americanas(p1=entry_descricao.get(),p2=selecionar_tipo.get(),p3=entry_marca.get())])
botao_2.place(relx=0.2, rely=0.85, relwidth=0.3, relheight=0.1)
#  Botao de Pesquisa da Kabum
botao_3 = Button(text="Kabum", command =lambda: [pesquisa_Kabum(p1=entry_descricao.get(),p2=selecionar_tipo.get(),p3=entry_marca.get())])
botao_3.place(relx=0.7, rely=0.69, relwidth=0.2, relheight=0.1)
#  Botao de Pesquisa da Mercado Livre
botao_4 = Button(text="Mercado Livre", command =lambda: [pesquisa_mercado_livre(p1=entry_descricao.get(),p2=selecionar_tipo.get(),p3=entry_marca.get())])
botao_4.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)
#  Botao de Pesquisa da Amazon
botao_5 = Button(text="Amazon", command =lambda: [pesquisa_amazon(p1=entry_descricao.get(),p2=selecionar_tipo.get(),p3=entry_marca.get())])
botao_5.place(relx=0.43, rely=0.69, relwidth=0.2, relheight=0.1)


janela.mainloop()