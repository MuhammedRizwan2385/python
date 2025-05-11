import tkinter
root=tkinter.Tk()
root.title("Area")
length_label=tkinter.Label(root,text="Enter the length")
length_label.pack()
length_entry=tkinter.Entry(root)
length_entry.pack()
breadth_label=tkinter.Label(root,text="Enter the breadth")
breadth_label.pack()
breadth_entry=tkinter.Entry(root)
breadth_entry.pack()
area_label=tkinter.Label(root,text="Area")
area_label.pack()
area_entry=tkinter.Entry(root)
area_entry.pack()

def button_clicked():
    length=int(length_entry.get())
    breadth=int(breadth_entry.get())
    area=length*breadth
    area_entry.insert(0,str(area))


def clear_button():
    length_entry.delete(0,tkinter.END)
    breadth_entry.delete(0,tkinter.END)
    area_entry.delete(0,tkinter.END)

submit_button=tkinter.Button(root,text="Submit",command=button_clicked)
submit_button.pack()
clear_button=tkinter.Button(root,text="clear",command=clear_button)
clear_button.pack()


root.mainloop()
