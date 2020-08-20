# import ffmpeg
from tkinter import filedialog
import tkinter as tk
import os

def fileOpen():
    global movie_files
    movie_files = filedialog.askopenfilenames(parent=main, title='Choose a file')
    file = open("temp.txt", "w")
    for x in movie_files:
        file.write("file " + "'" + x + "'\n")
    file.close()
    fileselect_text.set("File selected = True")

def videoMerge():
    if name_var.get() != "(optional)":
        lenth = len(name_var.get())
        name = name_var.get()
        temp = lenth - 4
        print(name[temp:999])
        if name[temp:999] != ".mp4":
            name_temp = name_var.get() + ".mp4"
        else:
            name_temp = name_var.get()
    else:
        name_temp = "output.mp4"
    os.system("ffmpeg -f concat -safe 0 -nostdin -i temp.txt -c:a aac " + name_temp)
    os.popen("del temp.txt")
    fileselect_text.set("Merge complete")


main = tk.Tk()

select_label = tk.Label(main, text="select files").grid(row=0, column=0)
file_button = tk.Button(main, text="Open", command=fileOpen).grid(row=0, column=1)
fileselect_text = tk.StringVar()
fileselect_text.set("File selected = False")
selected_files = tk.Label(main, textvariable=fileselect_text).grid(row=1, column=0)
name_label = tk.Label(main, text="Pick a file name").grid(row=2, column=0)
name_var = tk.StringVar()
name_entry = tk.Entry(main, textvariable=name_var).grid(row=2, column=1)
name_var.set("(optional)")
merge_button = tk.Button(main, text="Merge", command=videoMerge).grid(row=3, columnspan=2)

main.update_idletasks()
tk.mainloop()
