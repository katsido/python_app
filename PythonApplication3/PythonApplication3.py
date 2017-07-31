
import mysql.connector 
from mysql.connector import errorcode
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
from functools import partial

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'python_app',
  'raise_on_warnings': True,
  'use_pure': False,
}


class Gra(Frame):
    '''
    def policz_rekordy(self):
        cnx = mysql.connector.connect(**config)
        cursor=cnx.cursor()
        query=("SELECT COUNT(*) FROM kanjii")
        cursor.execute(query)
        self.ile_w_bazie=cursor.fetchone()[0]
        cursor.close()
        cnx.close()
    '''

    def test(self):
        print("to jest test")

    def koniec_rozgrywki(self):
        messagebox.showinfo("Koniec", "Wynik Koncowy: "+str(self.menu.wynik_wartosc))

    def nowa_rozgrywka(self):
        self.menu.wynik_wartosc=0
        self.menu.update()
        self.nowe["state"]="normal"
        self.numer_pytania=0
        for i in range(self.ilosc_odpowiedzi):
            self.button[i]["text"]="???"
            self.button[i]["bg"]="white"
            self.button[i]["state"]="disable"
        self.pytanie["text"]="Pytanie nr "+str(self.numer_pytania)+" /10"
        self.pytanie2["text"]="???"

    def podpowiadaj(self):
        self.menu.wynik_wartosc=self.menu.wynik_wartosc-5
        self.menu.update()
        print (self.lista)
        self.podpowiedz["text"]=str(self.lista[self.poprawna_odpowiedz][2])
        self.menu.help["state"]="disable"

    def losuje_nowy_zestaw(self):
        self.menu.help["state"]="normal"
        self.numer_pytania=self.numer_pytania+1
        print ("losujenowy nowe znaki")
        self.poprawna_odpowiedz=random.randint(0,self.ilosc_odpowiedzi-1)
        print("poprawna odowiedz to "+str(self.poprawna_odpowiedz))
        self.podpowiedz["text"]=" "

        try:
            cnx = mysql.connector.connect(**config)
            cursor=cnx.cursor()
            query2=("SELECT unicode, nazwa,znaczenie FROM kanjii ORDER BY RAND() LIMIT 4")
            cursor.execute(query2)
            #lista=[]
            lista=cursor.fetchall()
            self.lista=lista
            print (lista)
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        else:
          cnx.close()

        #self.pytanie["text"]=str(lista[self.poprawna_odpowiedz][0])+"   "+str(lista[self.poprawna_odpowiedz][1])+"  "+lista[self.poprawna_odpowiedz][2]
        self.pytanie["text"]="Pytanie nr "+str(self.numer_pytania)+" /10"
        znak=int(lista[self.poprawna_odpowiedz][0])
        self.pytanie2["text"]=chr(znak)

        for i in range(self.ilosc_odpowiedzi):
            self.button[i]["text"]=lista[i][1]
            self.button[i]["bg"]="white"
            self.button[i]["state"]="normal"
        if self.numer_pytania>=10:
            self.nowe["state"]="disable"
    
    def wybrano_odpowiedz(self,number):
        self.menu.help["state"]="disable"
        self.podpowiedz["text"]=str(self.lista[self.poprawna_odpowiedz][2])
        print ("wybrano odpowiedz o nr "+str(number))
        for i in range(self.ilosc_odpowiedzi):
           self.button[i]["state"]="disable"
        if int(number)==int(self.poprawna_odpowiedz):
            self.button[number]["bg"]="green"
            print("OK +10 punktow")
            self.menu.wynik_wartosc=10+self.menu.wynik_wartosc
            self.menu.update()
        else:
            self.button[number]["bg"]="red"
            self.button[self.poprawna_odpowiedz]["bg"]="green"
            print("BLAD -10 punktow")
            self.menu.wynik_wartosc=self.menu.wynik_wartosc-10
            self.menu.update()
        if self.numer_pytania>=10:
            self.koniec_rozgrywki()

    def createWidgets(self):

        
        self.nowe = Button(self)
        self.nowe["text"] = "Nowa znaki",
        self.nowe["command"] = partial(self.losuje_nowy_zestaw)
        self.nowe.pack({"side": "left"})
        '''
        self.test = Button(self)
        self.test["text"] = "TEST",
        self.test["command"] = self.test
        self.test.pack({"side": "top"})
        '''
        self.pytanie=Label(self)
        self.pytanie["text"]="???"
        self.pytanie.pack({"side": "top"})

        self.pytanie2=Label(self)
        self.pytanie2["text"]="???"
        self.pytanie2["font"]="Verdana 20 bold"
        self.pytanie2.pack({"side": "top"})

        self.podpowiedz=Label(self)
        self.podpowiedz["text"]=" "
        self.podpowiedz["font"]="Verdana 10 bold"
        self.podpowiedz.pack({"side": "top"})

        self.button = []
        for i in range(self.ilosc_odpowiedzi):
            self.button.append(Button(self, text='Game '+str(i+1),bd=10,width=10, state="disable", command=partial(self.wybrano_odpowiedz, i)))
            self.button[i].pack({"side": "left"})



    def __init__(self, master=None):
        Frame.__init__(self, master)
        #master.minsize(width=333,height=333)
        self.lista=[]
        self.ilosc_odpowiedzi=4
        self.ile_w_bazie=0
        self.pytanie_rodzaj=0
        self.odpowiedz_rodzaj=2
        self.numer_pytania=0
        self.poprawna_odpowiedz=0
        self.pack()
        self.menu=None
        self.createWidgets()


class Menu(Frame):
    def zaczynaj(self):
        print ("hi there, everyone!")
        self.gra.nowa_rozgrywka()
    def podpowiadaj(self):
        self.gra.podpowiadaj()
    def create_window(self):
        window=root.Toplevel(self)
    def update(self):
        self.czas["text"]="czasomierz:"+str(self.czas_wartosc)
        self.wynik["text"]="wynik: "+str(self.wynik_wartosc)
    def finish(self):
        print ("zakonczyc gre")
        self.gra.nowa_rozgrywka()

    def createWidgets(self):

        self.czas=Label(self)
        self.czas["text"]="czasomierz:"+str(self.czas_wartosc)
        self.czas.pack({"side": "top"})

        self.wynik=Label(self)
        self.wynik["text"]="wynik: "+str(self.wynik_wartosc)
        self.wynik.pack({"side": "top"})


        self.hi_there = Button(self)
        self.hi_there["text"] = "Nowa_rozgrywka"
        self.hi_there["command"] = self.zaczynaj
        self.hi_there.pack({"side": "top"})
      
        self.help = Button(self)
        self.help["text"] = "Podpowiedz"
        self.help["command"] = self.podpowiadaj
        self.help.pack({"side": "top"})
        

        self.koniec_rozgrywki = Button(self)
        self.koniec_rozgrywki["text"] = "Zakoncz rozgrywke"
        self.koniec_rozgrywki["command"] = self.finish
        self.koniec_rozgrywki.pack({"side": "top"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "Exit"
        self.QUIT["font"]="Verdana 20 bold"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "top"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.czas_wartosc=0.0
        self.wynik_wartosc=0
        self.ile_rekordow=0
        self.gra=None
        self.podpowiedzi_wartosc=4
        self.pack()
        self.createWidgets()


root = Tk()
root.title("aplikacja")
root.geometry("600x300+100+100")


m1 = PanedWindow( orient=VERTICAL)
m1.pack(fill=BOTH, expand=1)

m2 = PanedWindow(m1 ,bg="white",height=250)
m1.add(m2)

aaa = Label(m1, text="31 lipca 2017, autor :katsid",bg="blue")
m1.add(aaa)

right = Menu(master=root)
m2.add(right)

top = Gra(master=root)
m2.add(top)

top.menu=right
right.gra=top

m1.mainloop()
root.destroy()
