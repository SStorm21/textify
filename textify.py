from tkinter import * 
import os.path
from tkinter import filedialog
from tkinter import messagebox
from customtkinter import CTkEntry,CTkButton
import pytesseract
from PIL import Image
import os
os.environ["TESSDATA_PREFIX"] = "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"
root = Tk()
root.title("textify v1.0"),root.geometry("751x574+550+200"),root.config(bg="#F6F5F2"),root.resizable(0,0)
icon = PhotoImage(file="texters\\Logo.png")
root.iconphoto(True, icon)

def IMO():
    file = filedialog.askopenfile(mode='r',filetypes=[('JPEG Files', '*.jpg')])
    if file:
        filepath = os.path.abspath(file.name)
        ImagePath.insert(0,filepath)
    pass
def execute():
            try:
                pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe" 
                save_path = savepath.get()
                file_path = ImagePath.get()  
                print(f"Using file path: {file_path}")
                print(f"Using save path: {save_path}")
                img = Image.open(file_path)
                text = pytesseract.pytesseract.image_to_string(img)
                if not save_path:
                    messagebox.showerror("Error", "Please enter a valid save path!")
                    return
                encoded_text = text.encode("utf-8")
                with open(save_path, "wb") as f:
                    f.write(encoded_text)
                messagebox.showinfo("Textify", "\nFile saved successfully!")
                ImagePath.delete(0, END)
                savepath.delete(0,END)
                lang.delete(0,END)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
def SAVE():    
        save = filedialog.asksaveasfile(filetypes = [('ALL Files', '*.txt')], defaultextension = ".txt") 
        if save:
            savePATH = os.path.abspath(save.name)
            savepath.insert(0,savePATH)
        pass    
image=PhotoImage(file=r"texters\\main.png")
img=image.subsample(x=1,y=1)
button=PhotoImage(file=r"texters\\BUTTON.png")
Bi=button.subsample(x=1,y=1)
search=PhotoImage(file=r"texters\\search.png")
s=search.subsample(x=1,y=1)
Save=PhotoImage(file=r"texters\\file.png")
file=Save.subsample(x=1,y=1)
Editscreen=Frame(root,height=575,width=752,bg="#F6F5F2")
EditFrame=Label(Editscreen,image=img)
Button1=Button(EditFrame,borderwidth=0,command=execute,activebackground="#F2CDD7",highlightthickness=0,image=Bi)
Button2=CTkButton(EditFrame,bg_color="#F27CD7",width=35,height=35,command=IMO,text="Image Path",image=s,hover_color="white",border_color="#F0EBE3",fg_color="#F241D8",corner_radius=12,font=("Sitka Subheading",12,"bold"),compound=RIGHT,border_width=2)  
Button3=CTkButton(EditFrame,bg_color="#F27CD7",width=35,height=35,text="search\nsave path",image=file,hover_color="white",border_color="#F0EBE3",fg_color="#F241D8",corner_radius=12,font=("Sitka Subheading",12,"bold"),compound=RIGHT,border_width=2,command=SAVE)
ImagePath=CTkEntry(EditFrame,width=350,height=50,bg_color="#F27CD7",fg_color="#F0EBE3",border_width=4,corner_radius=30,border_color="#F6F5F2",placeholder_text_color="#F27CD7",placeholder_text=".....",text_color="#F27CD7",font=("Sitka Subheading",20,"bold"))
savepath=CTkEntry(EditFrame,width=350,height=50,bg_color="#F27CD7",fg_color="#F0EBE3",border_width=4,corner_radius=30,border_color="#F6F5F2",placeholder_text_color="#F27CD7",placeholder_text=".....",text_color="#F27CD7",font=("Sitka Subheading",20,"bold"))
lang=CTkEntry(EditFrame,width=350,height=20,bg_color="#F27CD7",fg_color="#F0EBE3",border_width=4,corner_radius=30,border_color="#F6F5F2",placeholder_text_color="#F27CD7",placeholder_text="  english.. ",text_color="#F27CD7",font=("Sitka Subheading",20,"bold"))
Editscreen.pack(fill=BOTH)
EditFrame.place(x=1, y=-3)
Button1.place(x=543, y=484)#execute
Button2.place(x=510, y=250)  
Button3.place(x=510, y=350)
ImagePath.place(x=150, y=250)
savepath.place(x=150, y=350)
lang.place(x=200, y=438)
root.mainloop()