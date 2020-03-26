from tkinter import *
import re
import autocomplete_test

root = Tk()
entry = autocomplete_test.AutocompleteEntry(autocomplete_test.autocompleteList, root, listboxLength=6, width=32, matchesFunction=autocomplete_test.matches)
entry.grid(row=0, column=0)    
Button(text='Python').grid(column=0)
Button(text='Tkinter').grid(column=0)
Button(text='Regular Expressions').grid(column=0)
Button(text='Fixed bugs').grid(column=0)
Button(text='New features').grid(column=0)
Button(text='Check code comments').grid(column=0)
root.mainloop()