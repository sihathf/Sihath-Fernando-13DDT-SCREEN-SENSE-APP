from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("13DDT Project")
root.configure(bg="white")

words2 = StringVar()
words3 = StringVar()
#fix logo
#image1 = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\images\logoses-removebg-preview.png")
##label_logo = Label(root, image=image1, bg='white')
#label_logo.grid(row=5, column=0)

frame1 = Frame(root, bg="white")
frame1.grid(row=0, column=0)

label_welcome= Label(frame1, text= "Welcome", fg ="black", font=('cooper black', 15), bg = "white")
label_welcome.grid()

side_image = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\images\loginsidepage-removebg-preview.png")
side_image = side_image.subsample(2) 

image2 = Label(frame1, image= side_image, bg='white')
image2.grid()


frame2 = Frame(root, bg="white")
frame2.grid(row=0, column=1)


label_signin = Label(frame2, text="Sign in:", fg ="black", font=('cooper black', 15), bg = "white")
label_signin.grid()

label_username = Label(frame2, text="Username", fg ="black", font=('cooper black', 15), bg = "white")
label_username.grid()

username_entry = Entry(frame2, textvariable=words2, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground = 'white')
username_entry.grid()   

username_line = Canvas(frame2, width=150, height=2.0, bg="#bdb9b1", highlightthickness=0)
username_line.grid()

label_password = Label(frame2, text="password ", fg ="black", font=('cooper black', 15), bg = "white")
label_password.grid()

password_entry = Entry(frame2, textvariable=words3, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground = 'white')
password_entry.grid()

password_line = Canvas(frame2, width=150, height=2.0, bg="#bdb9b1", highlightthickness=0)
password_line.grid()

click_btn= PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project v1\images\Login-Button-PNG-Image-File-removebg-preview.png")
click_btn = click_btn.subsample(6)

button= Button(frame2, image=click_btn,borderwidth=0)
button.grid()

button_forgotpassword = Button(frame2, text="Forgot Password?", bg="white", font=('cooper black', 15, 'underline'), relief= "flat")
button_forgotpassword.grid()

root.mainloop()
