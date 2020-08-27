from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
import os

movies_selected = False

#this function allows the user to select movies to be merged
def fileOpen():
    global movie_files
    global movies_selected
    movie_files = filedialog.askopenfilenames(parent=main, title='Choose a file')
    if len(movie_files) < 2:
        messagebox.showerror(title="need more", message="Select more than one video file")
    else:
        file = open("temp.txt", "w") #create a temp file to store a list of the selected files
        for x in movie_files: #write the file in a format that ffmpeg can use
            file.write("file " + "'" + x + "'\n")
        file.close()
        fileselect_text.set("File selected = True")
        movies_selected = True

#this function actually merges the selected files
def videoMerge():
    merge_check = False
    # check if there is a temp file (meaning video's where selected)
    try:
        file = open('temp.txt', 'r')
        file.close()
        merge_check = True
    except FileNotFoundError:
        merge_check = False

#if check was passed
    if merge_check:
        #check if an optional username was entered
        if name_var.get() != "(optional)":
            lenth = len(name_var.get())
            name = name_var.get()
            temp = lenth - 4
            #check if custom name provided includes a valed file extention, if not add one
            if name[temp:999] != ".mp4":
                name_temp = name_var.get() + ".mp4"
            else:
                name_temp = name_var.get()
        else:#if no custom name was provided, call the new video output.mp4
            name_temp = "output.mp4"
        #this command instructs ffmpeg to merge the selected vidoes
        os.system("ffmpeg -f concat -safe 0 -nostdin -i temp.txt -c:a aac " + name_temp)
        #this command instructs windows to delete the temp file
        os.popen("del temp.txt")
        fileselect_text.set("Merge complete")
    else: #if check wasn't passed
        messagebox.showerror(title="select movies", message="Select 2 or more videos")

def listfiles():
    global movie_files
    global fileselect_text

    if movies_selected:
        if len(movie_files) > 1:
            display_selected = tk.Tk(screenName="Selected Videos")
            display_selected.title("Selected Videos")
            for x in movie_files:
                tk.Label(display_selected, text=x).pack()
        else:
            messagebox.showerror(title="need more", message="Must select more than one movie")
    else:
        messagebox.showerror(title="slect movie", message="Please select movies to merge")


main = tk.Tk()
main.title("MovieSmasher 1.0")

select_label = tk.Label(main, text="select files").grid(row=0, column=0)
file_button = tk.Button(main, text="Open", command=fileOpen).grid(row=0, column=1)
fileselect_text = tk.StringVar()
fileselect_text.set("File selected = False")
selected_files = tk.Label(main, textvariable=fileselect_text).grid(row=1, column=0)
list_button = tk.Button(main, text="List selected video's", command=listfiles).grid(row=1, column=1)
name_label = tk.Label(main, text="Pick a file name").grid(row=2, column=0)
name_var = tk.StringVar()
name_entry = tk.Entry(main, textvariable=name_var).grid(row=2, column=1)
name_var.set("(optional)")
merge_button = tk.Button(main, text="Merge", command=videoMerge).grid(row=3, columnspan=2)

main.update_idletasks()
tk.mainloop()
