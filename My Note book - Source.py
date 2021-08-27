from tkinter import *

class MyNotebook:
    def __init__ (self,root):
        """ MyNotebook has been created by Kanwar Adnan. It's easy to access and
            customize, as it's written in python tkinter module.

                Example:
                    from tkinter import *
                    root = Tk()
                    frame = Frame(root)
                    frame.pack(expand = 1 , fill = BOTH)
                    
                    # Now creat MyNotebook object , make it on the desired frame
                    M1 = MyNotebook(frame)
                    
                    # Now make frames for the object , you should place
                    # new frames on mainframe of object.
                    page1 = Frame(M1.mainframe , bg = 'white')
                    page2 = Frame(M1.mainframe , bg = 'black')
                    
                    # Now add these frames to object
                    
                    M1.add(page1, 'Page 1')
                    M1.add(page2, 'Page 2')
                    
                    # No need to pack that object it's already packed
            
            Avaiable configurations : 
                                    activebackground,activeforeground,bg,bd,fg,
                                    fieldbackground,tabbg , focusbg """
        self.root = root
        self.tabs = []
        self.btns = []
        self.nbcolors = {'bg' : '#cdcdcd' , 'bd' : 1 , 'fg' : 'black' , 'fieldbackground' : 'darkgray' ,
                        'tabbg' : '#cdcdcd','activebackground':'#cdcdcd','activeforeground' : 'black'
                        }
        self.hovcolors = {'focusbg':'darkgray'} 
        self.tab = None
        self.hovcolor = None

        self.mainframe = Frame(self.root)
        self.header = Frame(self.root,bg=self.nbcolors['fieldbackground'])
        self.header.pack(side = TOP , fill = X)
        self.mainframe.pack(expand = 1 , fill = BOTH)

    def add(self,frame,text):
        """ Adds the current tab to the notebook. """
        self.button = Button(self.header , width = 10 , text = text ,
                            command = lambda : self.showtab(self.tabs.index(frame)))
        self.button.grid(row = 0 , column = len(self.tabs))
        self.tabs.append(frame)
        self.btns.append(self.button)

        self.button.bind("<Enter>",lambda e :self.focusIn(e,frame))
        self.button.bind("<Button-1>",lambda e :self.FocusIn(e,frame))
        self.button.bind("<Leave>",lambda e :self.focusOut(e,frame))

        self.default()

    def focusIn(self,event,frame):
        """ Changes the color of tab when mouse's cursor enters. """
        self.hovcolor = self.btns[self.tabs.index(frame)]['bg']
        self.btns[self.tabs.index(frame)].config(bg=self.hovcolors['focusbg'])

    def FocusIn(self,event,frame):
        """ Changes the the color of tab when it's pressed. """
        self.hovcolor = self.nbcolors['tabbg']
        self.btns[self.tabs.index(frame)].config(bg=self.hovcolors['focusbg'])

    def focusOut(self,event,frame):
        """ Makes Tab color as it was before focusIn. """
        self.btns[self.tabs.index(frame)].config(bg=self.hovcolor)

    def default(self):
        """ Set's the default tab to be displayed. """
        self.showtab(0)

    def display(self,frame):
        """ This function is used to display tab to the GUI. """
        self.hide()
        frame.pack(expand = 1 , fill = BOTH)
        self.tab = self.tabs.index(frame)
        self.config(**self.nbcolors)

    def hide(self):
        """ Hides all the tabs , so you can change the tabs easily. """
        for i in self.tabs:
            i.pack_forget()

    def showtab(self,index):
        """ This function checks whether the required tab should be displayed or not.
            It's just a part of display function."""
        if index > (len(self.tabs)-1):
            self.display(self.tabs[0])
            index = 0
        else:
            self.display(self.tabs[index])
        self.ordertab()
        self.btns[index].config(bg=self.nbcolors['tabbg'])

    def currenttab(self):
        """ Returns the current active tab index. """
        return self.tab

    def ordertab(self):
        """ Re arranges the tabs. """
        self.addtab(self.tab)

    def nexttab(self):
        """ Switches to the next tab. """
        self.showtab(self.tab+1)
        self.ordertab()

    def prevtab(self):
        """ Switches to previous tab. """
        self.showtab(self.tab-1)
        self.ordertab()
 
    def removetab(self,index):
        """ Hides a desired tab """
        self.btns[index].grid_forget()

    def addtab(self,index):
        """ Re-places a desired hidden tab """
        self.btns[index].grid(row = 0 , column = index)

    def config(self,fieldbackground=None,focusbg=None,tabbg=None,*args,**kwargs):
        """ This method is used to configure notebook object.
            Avaiable configurations : activebackground, activeforeground , bg , bd
                                    , fg , fieldbackground , tabbg , focusbg
        
            Color options:
            bg      : Changes the background color of tabs.
            fg      : Changes the foreground color of tabs.
            tabbg   : Changes the active tab color.
            focusbg : Change the the color tab when it's being hoverd. 
            activebackground : Changes the background color of tab when it's pressed.
            activeforeground : Changes the foreground color of tab when it's pressed.
            fieldbackground : Changes the color of header, where tabs are displayed.

            And all the other configuration options of Buttons can be used as well.

            Usage:
                MyNotebookobject.config(bg='white' , fg = 'black')

                                    """
            
        self.nbcolors.update(**kwargs)
        if focusbg:
            self.hovcolors['focusbg']=focusbg
        for i in self.btns:
            i.config(*args,**kwargs)

        if fieldbackground:
            self.nbcolors['fieldbackground'] = fieldbackground
            self.header.config(bg=fieldbackground)

        if tabbg:
            self.nbcolors['tabbg'] = tabbg

root = Tk()
from tkinter import *
frame = Frame(root)
frame.pack(expand = 1 , fill = BOTH)

# Now creat MyNotebook object , make it on the desired frame
M1 = MyNotebook(frame)
# Now make frames for the object , you should place new frames on mainframe of object
page1 = Frame(M1.mainframe , bg = 'white')
page2 = Frame(M1.mainframe , bg = 'black')
# Now add these frames to object

M1.add(page1, 'Page 1')
M1.add(page2, 'Page 2')

for i in range(30):
    Label(page1, text = f'Content no {i} for Page 1',bg = 'white').pack()
    Label(page2, text = f'Content no {i} for Page 2',bg = 'black' , fg = 'white' ).pack()
root.mainloop()