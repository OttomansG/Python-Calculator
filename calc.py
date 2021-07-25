from tkinter import *

hesap = Tk()

hesap.title("Hesap Makinesi")

hesap.geometry("390x450+400+100")

hesap.resizable(False,False)


result = 0

########### Fonksiyonlar  ###############

def numaraGiris(x):
    if ekran_kutusu.get() == "0":
        ekran_kutusu.delete(0,'end')
        ekran_kutusu.insert(0,str(x))
    else:
        length = len(ekran_kutusu.get())
        ekran_kutusu.insert(length,str(x))
        
def operatorGir(x):
    if ekran_kutusu.get()!="0":
        length = len(ekran_kutusu.get())
        ekran_kutusu.insert(length,btn_op[x]['text'])
        
        
def temizleFonk():
    ekran_kutusu.delete(0,END)
    ekran_kutusu.insert(0,"0")

def silFonk():
    length = len(ekran_kutusu.get())
    print(length)
    ekran_kutusu.delete(length-1,'end')
    if length == 1:
           ekran_kutusu.insert(0,"0")
        

def esittirFonk():
    content = ekran_kutusu.get()
    result = eval(content)
    ekran_kutusu.delete(0,END)
    ekran_kutusu.insert(0,str(result))
    


########### Sayı girişine İlişkin  ###########

ekran_kutusu = Entry(font = "Arial 25 bold", width=18, bg="#e6f7fa", bd=11, justify = RIGHT)

ekran_kutusu.insert(0,"0")

ekran_kutusu.place(x=20,y=10)


############ Sayı Butonlarına İlişkin ##############

btn_number = []

for i in range(10):
    btn_number.append(Button(width=4,text=str(i),font="Times 15 bold",bd=5, command = lambda x=i: numaraGiris(x)))
    
btn_text=1

for k in range(0,3):
    for j in range(0,3):
        btn_number[btn_text].place(x=25+j*90, y=90+k*70)
        btn_text +=1

############ Operatörlere ilişkin ##############

btn_op = []

for i in range(4):
    btn_op.append(Button(width=5,font='Times 15 bold', bd=5, command=lambda x=i:operatorGir(x)))
    
btn_op[0]['text']="+"
btn_op[1]['text']="-"
btn_op[2]['text']="*"
btn_op[3]['text']="/"

for l in range(4):
    btn_op[l].place(x=290,y=90+l*70)


############ Diğer Butonları ##############

btn_zero = Button(width=19,text="0",font='Times 15 bold', bd=5, command=lambda x=0:numaraGiris(x))

btn_zero.place(x=25,y=300)


btn_clear = Button(width=5, text='C', font='times 15 bold', bd=5, command=temizleFonk)

btn_clear.place(x=290,y=370)

btn_nokta =  Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x=".":numaraGiris(x))

btn_nokta.place(x=205,y=370)


btn_esit = Button(width=4, text='=', font='times 15 bold', bd=5, command=esittirFonk)

btn_esit.place(x=115,y=370)


btn_sil = Button(width=4, text='←', font='times 14 bold', bd=5, command=silFonk)

btn_sil.place(x=25,y=370)






hesap.mainloop()