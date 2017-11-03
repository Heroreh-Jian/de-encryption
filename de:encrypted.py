from tkinter import *
from tkinter import messagebox as tkMB
from tkinter import filedialog as tkFD
from tkinter import font as tkFont
# import os for os related functions
import os

# encryption library for getting encryption values
encryptLib = {
    "a": "!",
    "b": "@",
    "c": "6",
    "d": "$",
    "e": "%",
    "f": "^",
    "g": "&",
    "h": "*",
    "i": "(",
    "j": ")",
    "k": "+",
    "l": "?",
    "m": "/",
    "n": "<",
    "o": ">",
    "p": "4",
    "q": "2",
    "r": "P",
    "s": ",",
    "t": "=",
    "u": "_",
    "v": "j",
    "w": "~",
    "x": "0",
    "y": "|",
    "z": ".",
    " ": "a",
    ".": "b",
    ",": "^^"
}

# decryption library which reverses key-and-value pairs in the encrypt lib
decryptLib = dict(zip(encryptLib.values(), encryptLib.keys()))

root = Tk()  # creates the window
root.geometry("800x800+300+300")
root.title("JC Notepad")

# labels that present below left right above of menu bar
label1 = Label(root, bg="#C0FF3E", height=1, width=600)
label1.pack(side=BOTTOM, expand=NO, fill=X)

label2 = Label(root, bg="#C0FF3E", height=600, width=2)
label2.pack(side=LEFT, expand=NO, fill=Y)

label3 = Label(root, bg="#C0FF3E", height=600, width=2)
label3.pack(side=RIGHT, expand=NO, fill=Y)

label4 = Label(root, bg="#C0FF3E", height=5, width=600)
label4.pack(side=TOP, expand=NO, fill=X)

# the text area in our GUI
textPad = Text(root, undo=TRUE, bg="#FFF0F5", padx=13, pady=13)
textPad.pack(expand=YES, fill=BOTH)

# title for our text area
titlebar = Label(label4, bg="#C0FF3E", text="SECRET GARDEN")
titlebar.pack(side=TOP, expand=NO, fill=None)

# ==== menu bar functions ======
# the open function - open an exisiting text file
def open_file():
    global filename
    filename = tkFD.askopenfilename(defaultextension=".txt")
    if filename == '':
        filename = NONE
    else:  # open a file and list the file name as the window's title
        root.title(os.path.basename(filename) + "- JC Notepad")
        fh = open(filename, 'r')
        textPad.insert(1.0, fh.read())
        fh.close()


# the exit function - it will quit the text editor
def exit_editor(event=None):
    if tkMB.askokcancel("Close", "Oh no! You are leaving?!\n\nPlease \
make sure you save the file before you check out!"):
        root.destroy()

def retrieve_input():
    all_text = textPad.get(1.0, 'end-1c')
    # get all texts and remove the newline at the end of text content
    return all_text

# the save function - it saves the file user created / edited on our notepad
def save_file():
    global filename
    try:
        f = open(filename, 'w')
        text = retrieve_input()
        f.write(text)
        f.close()
    except:
        pass

# encryption function for texts in our text pad
def encrypt_text():
    global encryptResult
    encryptResult = ""
    text = retrieve_input()
    for letter in text:
        if letter in encryptLib:
            # if the letter is in our encryption library, we do the encryption
            encryptResult += encryptLib[letter]
        else:
            # the letter is Not found in our library, skip the encryption
            encryptResult += letter

    textPad.delete(1.0, END)
    textPad.insert(1.0, encryptResult)

# decryption function
def decrypt_text():
    global decryptResult
    decryptResult = ""
    text = retrieve_input()
    for letter in text:
        if letter in decryptLib:
            # if the letter is in our encryption library, we do the decryption
            decryptResult += decryptLib[letter]
        else:
            # the letter is Not found in our library, skip the decryption
            decryptResult += letter

    textPad.delete(1.0, END)
    textPad.insert(1.0, decryptResult)

# the about information
def about():
    tkMB.showinfo("About this GUI", "Below is the saying down in Phantom Ranch \
I want to share with your when i did Rim to Rim hiking in Oct, 2016:\
\n \n 'After your first experience backpacking in the Grand Canyon \
you will be left with one of two reactions: either you will never \
hike again in your life, or you will find that your life up to this \
moment has been meaningless, and you will be forever enslaved by \
thoughts of returning to this torturous paradise.'\n \nI feel the \
same way for learning python: You Like It or Hate It!")

# assignment's author information
def about_author():
    tkMB.showinfo("Author", "This GUI is designed by Jian Yu and \
Cathy Huang with the help of Dr. Richard Riehle's handouts and \
Burkhard A. Meier's book titled Python GUI Programming Cookbook")

# work log for this assignment
def about_worklog():
    tkMB.showinfo("Work Log", "*This GUI was originally created \
on 10-25-2016 at 7:21PM PST.\n\n*This GUI was modified on 10-26-2016 \
at 4:14pm PST.\n\n* This GUI was further modified on 10-26-2016 \
at 10:10pm PST")

# copyright info
def about_copyright():
    tkMB.showinfo("Copyright", "Copyright @ Jian Yu and Cathy Huang\
2016. All rights reserved.")

# help info
def help():
    tkMB.showwarning("Help", "Please contact Jian Yu or Cathy Huang\
@jian.yu1208@gmail.com if you eed any assistance with this GUI.")

# my font dictionary
myFont = tkFont.Font(family="Times New Roman", size=16)

# font changing function
def fontTimes():
    textPad.configure(font=myFont)

def fontHelvetica():
    myFont.configure(family="Helvetica")
    textPad.configure(font=myFont)

def fontBold():
    myFont.configure(weight=tkFont.BOLD)
    textPad.configure(font=myFont)

def fontItalic():
    myFont.configure(slant=tkFont.ITALIC)
    textPad.configure(font=myFont)

# click the buttons for encryption/decryption
encryptButton = Button(label1, text="Encryption", activebackground="red",
                       fg="black",command=encrypt_text)
encryptButton.pack(padx=28, side=LEFT)
encryptButton = Button(label1, text="Decryption",activebackground="red",
                       fg="black", command=decrypt_text)
encryptButton.pack(padx=10, side=LEFT)

menubar = Menu(root)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About GUI", command=about)
aboutmenu.add_command(label="Author", command=about_author)
aboutmenu.add_command(label="Work Log", command=about_worklog)
aboutmenu.add_command(label="Copyright", command=about_copyright)
menubar.add_cascade(label="About", menu=aboutmenu)

editmenu = Menu(menubar, tearoff=0)

# create a submenu for fonts
fontmenu = Menu(editmenu, tearoff=0)
fontmenu.add_command(label="Font- Times New Roman", command=fontTimes)
fontmenu.add_command(label="Font- Helvetica", command=fontHelvetica)
fontmenu.add_command(label="Bold", command=fontBold)
fontmenu.add_command(label="Italic", command=fontItalic)
editmenu.add_cascade(label="Font", menu=fontmenu, underline=0)

menubar.add_cascade(label="Edit", menu=editmenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", accelerator="Command+O", command=open_file)
filemenu.add_command(label="Save", accelerator="Command+S", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Command+W",
                     command=exit_editor)
# it's common to use hot key Command+W to close a window
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="JC Notepad Help", accelerator="Command+H",
                     command=help)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
