from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title("Image Rotator")
root.geometry("500x500")
root.configure(background="lightblue")

display_image = Label(root, bg="white", highlightthickness=5)
display_image.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path=""

def open_image(): 
    global img_path
    img_path = filedialog.askopenfilename(title="Open File", filetypes=[("Image Files", "*.jpg;*.jpg;*.png;*.txt")])
    print(img_path)
    img = ImageTk.PhotoImage(Image.open (img_path))
    display_image["image"] = img
    img.close()
    
def rotateImage():
    global img_path
    im = Image.open(img_path)
    rotated_img = im.rotate(180)
    img = ImageTk.PhotoImage(rotated_img)
    display_image["image"] = img
    img.close()
    
open_button=Button(root, text="Open Image", command=open_image)
open_button.place(relx=0.5, rely=0.9, anchor=CENTER)

open_button=Button(root, text="Rotate Image", command=rotateImage)
open_button.place(relx=0.5, rely=0.97, anchor=CENTER)
root.mainloop()