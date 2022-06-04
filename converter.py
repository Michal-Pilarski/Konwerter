import tkinter as tk
from tkinter import ttk

window = tk.Tk() # tworzenie okna
window.title('Konwerter')

def convertToDec(num, type):
    num = reversed(num)
    lastDecNum = 0
    potega = 0
    for i in num:
        for j in range(len(hexArray)):
            if hexArray[j] == i:
                decNum = type ** potega
                potega += 1
                decNum *= j
                lastDecNum += decNum
    return lastDecNum

def convertFromDec(num, type):
    num = int(num)
    type = int(type)
    result = ''
    flag = True
    while flag:

        dividedNum = num / type

        dividedNum = int(dividedNum)
        rest = dividedNum * type
        rest = num - rest

        if rest > 9:
            rest = hexArray[rest]

        result += str(rest)

        num = dividedNum

        if dividedNum < type:
            if dividedNum > 9:
                dividedNum = hexArray[dividedNum]

            result += str(dividedNum)
            return result[::-1] # [::-1] to odwracanie tekstu
            flag = False

def getValue(): # rozpoznawanie systemów liczbowych, konwersja, zapobieganie niepożądanych danych
    value = entry.get()
    value = value.upper()
    ListValue1 = lista1.get()
    ListValue2 = lista2.get()
    OutputTextFlag = True


    for i in range(len(systems)): # rozpoznawanie systemów liczbowych
        if ListValue1 == systems[i]:
            ListValue1 = systemInt[i]

        if ListValue2 == systems[i]:
            ListValue2 = systemInt[i]


    for j in value: # zapobieganie wprowadzania błednych danych dla wybranego systemu 'zamien z'
        flag = False
        for k in range(0, ListValue1): # od 0 do liczby reprezentujacej wybrany system liczbowy
            if j == hexArray[k]:
                flag = True
        if flag == False:
            OutputTextFlag = False

    result = convertToDec(value, ListValue1) # konwersja
    result = convertFromDec(result, ListValue2)

    if result[0] == '0': # konwersja na np A dawała 0A więc uciąłem zero
        result = result[1:]

    if OutputTextFlag == True: # Wyświetlanie danych w labelu
        outputLabel['text'] = result
    else:
        outputLabel['text'] = 'Nieodpowiednie dane'

hexArray = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']

systems = ('Binarny', 'Trójkowy', 'Czwórkowy', 'Piątkowy', 'Szóstkowy', 'Siódemkowy',
           'Ósemkowy', 'Dziewiątkowy', 'Dziesiętny', 'Jedenastkowy', 'Dwunastkowy',
           'Trzynastkowy', 'Szesnastkowy', 'Dwudziestkowy')

systemInt = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 20]


window.geometry(f'{500}x{200}+{700}+{400}') # rozmiar okna + przesunięcie okna od lewego górnego rogu

ttk.Label(window, text="Konwerter dla systemów liczbowych").place(x=150, y=10)

entry = ttk.Entry(window)
entry.place(x=10,y=50)


lista1 = ttk.Combobox(window, values=systems, width=15)
lista1['state'] = 'readonly' # nie można wpisywać do listy
lista1.set('Zamień z')
lista1.place(x=160,y=50)

lista2 = ttk.Combobox(window, values=systems, width=15)
lista2['state'] = 'readonly' # nie można wpisywać do listy
lista2.set('Zamień na')
lista2.place(x=300,y=50)

ttk.Button(window, text='Konwertuj', command=getValue).place(x=10,y=100)

outputLabel = ttk.Label(window)
outputLabel.place(x=100, y=100)

tk.mainloop() # wywołanie pętli komunikatów
