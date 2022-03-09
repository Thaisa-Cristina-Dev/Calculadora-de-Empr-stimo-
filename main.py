from tkinter import*
from tkinter import scrolledtext
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox

from PIL import ImageTk, Image
import datetime
from datetime import timedelta 

################# tkcalendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date


################# cores ###############

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

################# criando janela ###############

janela = Tk ()
janela.title ("")
janela.geometry('1000x404')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body


################# Frames ####################

frame_Esquerda = Frame(janela,width=300, height=403,bg=co1, relief="flat")
frame_Esquerda.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)

frame_Meio = Frame(janela,width=700, height=403,bg=co1, relief="flat")
frame_Meio.grid(row=0, column=1, pady=1, padx=1, sticky=NSEW)

img_app = Image.open('icon.png')
img_app = img_app.resize((50, 50), Image.ANTIALIAS)
img_app = ImageTk.PhotoImage(img_app)
app_logo = Label(frame_Esquerda, text="Calculadora de Empréstimo         ", image=img_app, compound=LEFT,relief="flat", anchor=NW, font=('verdana 11 bold'), bg=co4, fg=co1)
app_logo.place(x=10,y=0)



dados = [] 

def calcular_emprestimo(loan, mes, juros):
    monthlyPay = loan * (juros * (1 + juros) ** mes / ((1 + juros) ** mes - 1))
    #print(-round(numpy.pmt(juros, mes, loan), 2))
    payment = monthlyPay
    month = 1
    monthlyInterest = juros * loan
    principal = payment - monthlyInterest
    balance = loan - principal
    total_interest_paid = 0
 
    d=int(27)
    m=int(2)
    y=int(2022)
    
    while balance > 0:
        monthlyInterest = juros * balance
        principal = payment - monthlyInterest
        balance = balance - principal
        month += 1
        total_interest_paid += monthlyInterest

        if balance <= 0:
            balance = 0
        
        gDate = datetime.datetime(y, m, d) 
        pv = gDate + timedelta(days = 30) 
        dia_do_pagamento =pv.strftime('%Y-%m-%d')
        
        d = int(pv.strftime('%d'))
        m = int(pv.strftime('%m'))
        y = int(pv.strftime('%Y'))
        
        temp = [month, dia_do_pagamento,principal, monthlyInterest,  payment,balance ]
        dados.append(temp)
    
    
    juros = "Os juros totais pagos serão: ${0:,.2f}".format((payment * month) - loan)
    total = "O principal total pago será:  ${0:,.2f}".format(loan)
    
    print(juros)
    
    
    l_valor_juros = Label(frame_Esquerda, text=str(juros), height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_valor_juros.place(x=10, y=320)
    
    l_valor_pago = Label(frame_Esquerda, text=str(total), height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_valor_pago.place(x=10, y=340)
    
    
    mostrar()
    

# funcao para obter os valores a partir das entrys
# e no fim ira passar esses valores para a funcao que faz Calculo de Empréstimo 
def calcular():
    ############################## Inputs ##############################
    valor = float(e_valor.get())
    anos = float(e_anos.get())
    juros = float(e_juros.get())
    juros = juros / 12 / 100
    mes = anos * 12

    # Chamar a calculadora
    calcular_emprestimo(valor, mes, juros)

l_valor = Label(frame_Esquerda, text="Valor da emprestimo", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=75)
l_valor = Label(frame_Esquerda, text="$", height=1,anchor=NW, font=('Ivy 20 bold'), bg=co1, fg=co6)
l_valor.place(x=10, y=100)
e_valor = Entry(frame_Esquerda, width=13,font=('Ivy 15'), justify='center',relief="raised", highlightthickness=1)
e_valor.place(x=30, y=105)


l_juros = Label(frame_Esquerda, text="Taxa de juros", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_juros.place(x=10, y=150)
l_juros = Label(frame_Esquerda, text="%", height=1,anchor=NW, font=('Ivy 20 bold'), bg=co1, fg=co6)
l_juros.place(x=10, y=180)
e_juros = Entry(frame_Esquerda, width=12,font=('Ivy 15'), justify='center',relief="raised", highlightthickness=1)
e_juros.place(x=42, y=185)


l_anos = Label(frame_Esquerda, text="Período de Empréstimo", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_anos.place(x=10, y=225)
l_juros = Label(frame_Esquerda, text="(anos)", height=1,anchor=NW, font=('Ivy 20 bold'), bg=co1, fg=co6)
l_juros.place(x=10, y=250)
e_anos = Entry(frame_Esquerda, width=7,font=('Ivy 15'), justify='center',relief="raised", highlightthickness=1)
e_anos.place(x=98, y=255)


b_confirmar = Button(frame_Esquerda,command=calcular, text="Calcular", width=30, height=1, bg=co2, fg=co1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=10, y=374)


################# frame tree ####################

# funcao para mostrar
def mostrar():

    # creating a treeview with dual scrollbars
    list_header = ['No','Data',  'Juros pagos','Capital pago','Pagamento mensal', 'Saldo restante']

    df_list = dados
    
    global tree

    tree = ttk.Treeview(frame_Meio, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(
        frame_Meio, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        frame_Meio, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_Meio.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[30,100,140,140,140,150]
    n=0

    for col in list_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in df_list:
        tree.insert('', 'end', values=item)
        
mostrar()   


janela.mainloop ()