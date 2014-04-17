#!/usr/bin/python
import Tkinter
import urllib2
from Tkinter import *

class share(Frame):
  
    def __init__(self, parent):
        
        Frame.__init__(self, parent, background = "grey")   
        self.parent = parent
        
        self.parent.title("Share Value Calculator")
        self.pack()
        self.centerWindow()
        self.cwd = StringVar(self.parent)
        self.dirfm = Frame(self.parent)
        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        self.label = Tkinter.Label(self.dirfm, text = 'Enter NASDAQ Symbol', font = 'Times -18 bold')
        self.label.pack()
        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        
        self.dirn = Entry(self.dirfm, width = 50, textvariable = self.cwd)
        self.dirn.bind('<Return>', self.value)
        self.dirn.pack()
        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        self.dirfm.pack()

        self.label = Label(self.dirfm, text = "")
        self.label.pack()
        self.difrm = Frame(self.parent)
        self.clear = Tkinter.Button(self.difrm, text = 'Clear', command = self.clear, bg = 'blue', fg = 'black', padx = 10)
        self.clear.pack(side = LEFT)
        self.quit = Tkinter.Button(self.difrm, text = 'Exit', command = self.parent.quit, bg = 'green', fg = 'black', padx = 10)
        self.quit.pack(side = LEFT)
        self.difrm.pack(expand = 0.5)

    def value(self, ev = None):
        symbol = self.cwd.get()
        self.label.config(text = "Calculating ...")
        self.label.update()
        try:
            a = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')
            b = float(a.read())
            if b == 0.00:
                result="The Nasdaq code entered is wrong"
                self.label.config(text = result)
                self.label.update()
            else:
                result="The current sharevalue of %s is %f" % (symbol, b)
                self.label.config(text = result)
                self.label.update()
        except:
            result="Check Your Internet Connection!"
            self.label.config(text = result)
            self.label.update()

    def centerWindow(self):
      
        w = 500
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def clear(self, ev = None):
        self.dirn.delete(0, Tkinter.END)
        self.label.config(text = " ")
        self.label.update()


def main():
    root = Tk()
    app = share(root)
    root.mainloop()  

if __name__ == '__main__':
    main() 