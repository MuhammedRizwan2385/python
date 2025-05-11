import tkinter
root=tkinter.Tk()
root.title("Age")
DOB_label=tkinter.Label(root,text="Enter the DOB")
DOB_label.pack()
DOB_textbox=tkinter.Entry(root)
DOB_textbox.pack()
age_label=tkinter.Label(root,text="Age")
age_label.pack()
age_textbox=tkinter.Entry(root)
age_textbox.pack()
def button_clicked():
    x=DOB_textbox.get()
    y=2025-int(x)
    age_textbox.insert(0,str(y))
    
def clear_button():
    age_textbox.delete(0,tkinter.END)
    DOB_textbox.delete(0,tkinter.END)

submit_button=tkinter.Button(root,text="Submit",command=button_clicked)
submit_button.pack()

clear_button=tkinter.Button(root,text="clear",command=clear_button)
clear_button.pack()






root.mainloop()
