
import mysql.connector 
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
    def policz_rekordy(self):
        cnx = mysql.connector.connect(**config)
        cursor=cnx.cursor()
        query=("SELECT COUNT(*) FROM kanjii")
        cursor.execute(query)
        self.ile_w_bazie=cursor.fetchone()[0]
        cursor.close()
        cnx.close()

    def losuje_nowy_zestaw(self,number):
        print ("losujenowy nowe zadanie")
        print (number)
        cnx = mysql.connector.connect(**config)
        cursor=cnx.cursor()

        #query=("SELECT ID, unicode, nazwa,znaczenie FROM kanjii")
        query2=("SELECT unicode, nazwa,znaczenie FROM kanjii ORDER BY RAND() LIMIT 4")
        cursor.execute(query2)
        """
        for (ID, unicode, nazwa,znaczenie) in cursor:
          print("{}, {}, {}, {}".format(
            ID, unicode, nazwa,znaczenie))
        """
        #for (unicode, nazwa,znaczenie) in cursor:
        #  print("{},{}, {},".format(unicode, nazwa,znaczenie))

        lista=[]
        lista=cursor.fetchall()
        print (lista)
        cursor.close()
        cnx.close()

        self.poprawna_odpowiedz=random.randint(0,self.ilosc_odpowiedzi-1)
        print("poprawna odowiedz to"+str(self.poprawna_odpowiedz))

        #self.pytanie["text"]=str(lista[self.poprawna_odpowiedz][0])+"   "+str(lista[self.poprawna_odpowiedz][1])+"  "+lista[self.poprawna_odpowiedz][2]
        znak=int(lista[self.poprawna_odpowiedz][0])
        #unicode_char = u"\u2713" 
        self.pytanie2["text"]=chr(znak)

        for i in range(self.ilosc_odpowiedzi):
            self.button[i]["text"]=lista[i][1]
            self.button[i]["bg"]="white"
            self.button[i]["state"]="normal"
    
    def wybrano_odpowiedz(self,number):
        print ("wybrano odpowiedz o nr "+str(number))
        for i in range(self.ilosc_odpowiedzi):
           self.button[i]["state"]="disable"
        if int(number)==int(self.poprawna_odpowiedz):
            self.button[number]["bg"]="green"
            print("OK")
        else:
            self.button[number]["bg"]="red"
            self.button[self.poprawna_odpowiedz]["bg"]="green"
            print("BLAD")

    def createWidgets(self):

        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Nowa znaki",
        
        self.hi_there["command"] = partial(self.losuje_nowy_zestaw, 7)
        self.hi_there.pack({"side": "left"})

        self.test = Button(self)
        self.test["text"] = "TEST",
        self.test["command"] = self.policz_rekordy
        self.test.pack({"side": "top"})

        self.pytanie=Label(self)
        self.pytanie["text"]="???"
        self.pytanie.pack({"side": "top"})

        self.pytanie2=Label(self)
        self.pytanie2["text"]="???"
        self.pytanie2["font"]="Verdana 20 bold"
        self.pytanie2.pack({"side": "top"})


        """
        self.odp[self.ilosc_odpowiedzi]=Button(self)
        
        for x in range(0,3):
            #self.odp[x] = Button(self)
            self.odp[x]["text"] = "Nowa znaki",
            self.odp[x]["command"] = self.losuje_nowy_zestaw
        self.odp.pack({"side": "left"})
        
        """
        self.button = []
        for i in range(self.ilosc_odpowiedzi):
            self.button.append(Button(self, text='Game '+str(i+1),bd=10,width=10, command=partial(self.wybrano_odpowiedz, i)))
       
            self.button[i].pack({"side": "left"})



    def __init__(self, master=None):
        Frame.__init__(self, master)
        #master.minsize(width=333,height=333)
        self.lista={}
        self.ilosc_odpowiedzi=4
        self.ile_w_bazie=0
        self.pytanie_rodzaj=0
        self.odpowiedz_rodzaj=2
        self.poprawna_odpowiedz=0
        self.pack()
        self.createWidgets()


class Menu(Frame):
    def say_hi(self):
        print ("hi there, everyone!")
    def opctions(self):
        print ("opcje")
    def create_window(self):
        window=root.Toplevel(self)

    def finish(self):
        print ("zakonczyc gre")

    def createWidgets(self):

        self.czas=Label(self)
        self.czas["text"]="czasomierz:"+str(self.czas_wartosc)
        self.czas.pack({"side": "top"})

        self.wynik=Label(self)
        self.wynik["text"]="wynik: "+str(self.wynik_wartosc)
        self.wynik.pack({"side": "top"})


        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "top"})
      
        self.ustawienia = Button(self)
        self.ustawienia["text"] = "Options"
        self.ustawienia["command"] = self.create_window
        self.ustawienia.pack({"side": "top"})
        


        self.koniec_rozgrywki = Button(self)
        self.koniec_rozgrywki["text"] = "Zakoncz rozgrywke"
        #self.koniec_rozgrywki["bg"] = "red"
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
        self.podpowiedzi_wartosc=4
        self.pack()
        self.createWidgets()


root = Tk()
root.title("aplikacja")
root.geometry("600x300+100+100")


m1 = PanedWindow( orient=VERTICAL)
m1.pack(fill=BOTH, expand=1)

m2 = PanedWindow(m1 ,bg="white",height=500)
m1.add(m2)

aaa = Label(m1, text="button pane",bg="blue")
m1.add(aaa)

right = Menu(master=root)
m2.add(right)

top = Gra(master=root)
m2.add(top)

m1.mainloop()
root.destroy()
