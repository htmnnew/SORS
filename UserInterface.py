from tkinter import *
from tkinter import filedialog
import DocumentSort


class MyInterface2:
    directory = ''
    def __init__(self, master):
        self.master = master
        master.title("SORS")

        # Label for title "SORS"
        self.SORSlbl = Label(master, text="SORS", bg="#D0D0D0", font="Helvetica 50")
        self.SORSlbl.place(x=13, y=6)

        # Label for app description
        self.AppLbl = Label(master, text="AN APP THAT SORTS YOUR CONTENT ", bg="#D0D0D0", font="Helvetica 15")
        self.AppLbl.place(x=5, y=80)

        # Image for Drag and Drop
        self.canvas = Canvas(master, width=237, height=237)
        self.canvas.pack()
        self.canvas.place(x=130, y=125)
        self.img = PhotoImage(file="drag.PPM")
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)

        # Button to Select Folder
        self.selectBtn = Button(master, text="SELECT FOLDER", bg="#4DC370", font="Helvetica 15",
                                command=self.selectFolder, borderwidth = 0)
        self.selectBtn.place(x=165, y=310)

        # Label to Select Folder (Shows directory when folder is selected)
        self.DirLbl = Label(master, text="CHOOSE A FOLDER TO SORT", font="Helvetica 20", width="30")
        self.DirLbl.place(x=0, y=390)

        # Empty Label
        self.BtnLbl2 = Label(master, text="I", bg="#4DC370", fg="#4DC370", font="Helvetica 40", width="8", borderwidth = 0)
        self.BtnLbl2.place(x=150, y=436)

        # Button to Sort ('command' should redirect to Sorting module)
        self.sortBtn = Button(master, text="SORT", bg="#4DC370", font="Helvetica 25", command=self.sort, borderwidth = 0)
        self.sortBtn.place(x=200, y=444)

    # Select Button Command

    def selectFolder(self):
        file_path = filedialog.askdirectory()
        File = "Directory: " + file_path
        self.DirLbl3 = Label(text=File, font="Helvetica 13", width="55", height="2")
        self.DirLbl3.place(x=0, y=390)
        self.directory += file_path

    #Sort Button Command - Executes to the the Document Sort to start the
    #process of sorting the files into there extension types
    def sort(self):
        #Close the start up screen and starts the process to sort the files
        if not self.directory is'':
            Window.destroy()
            DocumentSort.fileSplitter(self.directory)
        else:
            #Executes when no folder has been selected and the sort button has been clicked
            self.DirLbl4 = Label(text="Cannot Sort without a directory",  font="Helvetica 15", width="45", height="2")
            self.DirLbl4.place(x=0, y=390)


    # Sort Button Command (Should link to Sorting Module)

# Gui specifications
Window = Tk()
Window.geometry("500x500")
Window.configure(background="#D0D0D0")
MyFrame = MyInterface2(Window)
Window.resizable(0, 0)

#starts the main gui windown on the screen
# Displays
canvasLogo = Canvas(Window, width=105, height=75)
canvasLogo.pack()
canvasLogo.place(x=235, y=-3)
imgLogo = PhotoImage(file="SorsLogo.PPM")
canvasLogo.create_image(0, 0, anchor=NW, image=imgLogo)
Window.mainloop()