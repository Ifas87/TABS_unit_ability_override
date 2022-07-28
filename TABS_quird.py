import json
import tkinter
from tkinter import Tk
from tkinter import Button
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import ttk
import os


def overload(x, filename):
    print(x, filename)
    move1 = json.loads('{"m_modID": -1, "m_ID": 1998224969 }')
    move2 = json.loads('{"m_modID": -1, "m_ID": 702611234 }')
    biglist = [move1, move1, move1, move2, move1, move1]
    x["m_combatMoves"] = json.dumps(biglist)
    

def generateFrames(folder_path, top):

    """
    Button(win, text="Button-1",height= 5, width=10).pack()
    Button(win, text="Button-2",height=8, width=15).pack()
    Button(win, text= "Button-3",height=10, width=30).pack()
    """
    
    for filename in os.listdir(folder_path):
        f = os.path.join(folder_path, filename)
        print(f)
        if os.path.isfile(f):
            with open(f, encoding = 'utf-8') as file:
                things = json.loads(file.read())
                Button(top, text=things["m_name"], command= lambda:overload(things, filename), height=83, width=180).pack()
                


def main():

    root = Tk()
    container = ttk.Frame(root)
    canvas = tkinter.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    
    dirname = ''
    while dirname == '':
        #root.withdraw()
        dirname = askdirectory()
        generateFrames(dirname, root)

    root.geometry("180x250")
    root.mainloop()    

    """
    with open(filename, encoding = 'utf-8') as file:
        things = json.loads(file.read())
        things["m_combatMoves"] = 0
        overload(things)
        print(things)
    print("here")
    root.geometry("180x250")
    root.mainloop()
    """


if __name__=="__main__":
    main()
