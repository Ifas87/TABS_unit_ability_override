import json
import tkinter
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import ttk
import os
import time


recordbook = {}


def overload(m):
    global recordbook
    filename = recordbook[m]

    with open(filename, encoding = 'utf-8') as file:
        things = json.loads(file.read())
        things["m_combatMoves"] = 0
        move1 = json.loads('{"m_modID": -1, "m_ID": 1998224969 }')
        move2 = json.loads('{"m_modID": -1, "m_ID": 702611234 }')
        biglist = [move1, move1, move1, move2, move1, move1]
        things["m_combatMoves"] = json.dumps(biglist)
        print(things, m, filename)
    

def generateFrames(folder_path, top):
    global recordbook
    
    for i, filename in enumerate(os.listdir(folder_path)):
        f = os.path.join(folder_path, filename)
        if os.path.isfile(f) and filename.lower().endswith('.unit'):
            print(f)
            with open(f, encoding = 'utf-8') as file:
                things = json.loads(file.read())
                recordbook[things["m_name"]] = f
                Button(top, text=things["m_name"], command= lambda m=things["m_name"]:overload(m), height=2, width=20).pack()


def main():

    root = Tk()
    container = Frame(root).pack()
    canvas = tkinter.Canvas(root)
    canvas.configure(scrollregion=canvas.bbox("all"))
    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.pack()
    canvas["yscrollcommand"] = scrollbar.set
    
    
    dirname = ''
    while dirname == '':
        #root.withdraw()
        dirname = askdirectory()
        generateFrames(dirname, canvas)

    root.geometry("180x250")
    root.mainloop()


if __name__=="__main__":
    main()
