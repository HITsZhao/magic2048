#!usr/bin/env python
#-*- encoding utf-8 -*-
#FileName:2048.py


from tkinter import *
import random
import tkinter.messagebox

dic_color = {0:'GhostWhite', 2:'AliceBlue', 4:'LightCyan', 8:'Khaki',16:'SandyBrown', \
             32:'Goldenrod',64:'Orange',128:'Maroon',256:'Tomato',512:'OrangeRed', \
             1024:'FireBrick',2048:'Red'}
    
str_data=[]
B_list = []

            
class Magic_2048(object): 
    def __init__(self,nRow = 3,nColomn = 3):
        self.matrix     = [[0 for y in range(nRow)] for x in range(nColomn)]
        self.Row        = nRow
        self.Colomn     = nColomn
        self.bMoved     = False
    
    def RowReverse(self,row):
        return list(reversed(row))

    def matrixReverse(self,mat):
        return list(map(self.RowReverse,mat))
    
    def matrixRowColReverse(self,mat):
        return list(map(list,zip(*mat)))
    
    def Movefilter(self,item):
        return item != 0
        
    def Move(self,row):
        newrow      = list(filter(self.Movefilter,row))
        newrow     += [0 for i in range(len(row) - len(newrow))]
        return newrow               
        
    def CalInListLeft(self,row):
        row = self.Move(row)[:]
        for i in range(len(row) - 1):
            if  row[i] != row[i + 1]:
                continue
            else:
                row[i]         = row[i] + row[i + 1]
                row[i + 1]     = 0             
        return row  
                 
    def magic(self,direction):
        randomPos = list()
        for i,row in enumerate(self.matrix):
            for j,item in enumerate(row):
                if item == 0:
                    randomPos.append((i,j))
        if len(randomPos) != 0:
            Pos = random.choice(randomPos)
            self.matrix[Pos[0]][Pos[1]] = 2   
           
        if direction == 0:#left
            self.matrix = list(map(self.CalInListLeft,self.matrix))[:]
        elif direction == 1:  #right
            self.matrix = list(self.matrixReverse(self.matrix))[:]
            self.matrix = list(map(self.CalInListLeft,self.matrix))[:]
            self.matrix = self.matrixReverse(self.matrix)[:]
        elif direction == 2:#up
            self.matrix = self.matrixRowColReverse(self.matrix)
            self.matrix = list(map(self.CalInListLeft,self.matrix))[:]
            self.matrix = self.matrixRowColReverse(self.matrix)[:]
        else:#down
            self.matrix = self.matrixRowColReverse(self.matrix)
            self.matrix = self.matrixReverse(self.matrix)[:]
            self.matrix = list(map(self.CalInListLeft,self.matrix))[:]
            self.matrix = self.matrixReverse(self.matrix)[:]
            self.matrix = self.matrixRowColReverse(self.matrix)[:]
        print(self.matrix)
        return True

    def Refresh(self):
        for i,row in enumerate(self.matrix):
            for j,item in enumerate(row):
                B_list[i*self.Colomn + j].configure(bg=dic_color[item])
                if item == 0:
                    str_data[i*self.Colomn + j].set("")
                    continue
                str_data[i*self.Colomn + j].set(str(item))

m = Magic_2048(4,4)

def key_event(event):
    derection_code = 0
 
    if event.keycode == 37:
        derection_code = 0
    if event.keycode == 39:
        derection_code = 1
    if event.keycode == 38:
        derection_code = 2
    if event.keycode == 40:
        derection_code = 3
        
    m.magic(derection_code)
    
    m.Refresh()   
             
            
def test():
    
    root = Tk(className = "2048")
    root.geometry("320x360")
    frame = Frame(root,borderwidth = 10)
    
    for i in range(m.Row):
        for j in range(m.Colomn):  
            str_data.append(StringVar())
            B_list.append(Button(frame, width=4, height=2, textvariable = str_data[i * m.Colomn + j]  ,font = ("Courier 20 bold roman"),bg=dic_color[0]))
            B_list[i*m.Colomn + j].grid(row=i,column=j)
    
    frame.bind('<KeyRelease>', key_event)
    frame.pack()
    frame.focus_set()
    root.mainloop()

    
if __name__ == '__main__':
    test()
    
            
            
            
        