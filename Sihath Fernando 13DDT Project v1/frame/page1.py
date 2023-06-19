from tkinter import *
from tkinter import ttk


root = Tk()
root.title("13DDT Project")
root.configure(bg="white")

#canvas = Canvas(root, width=600, height=300, highlightthickness=0)
#canvas.grid()   

# photo as a background but it needs working code under:
# background = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\logoses-removebg-preview.png")
#background_label = Label(root,image = background)
# background_label.place(x=0, y=0, relwidth = 1 , relheight = 1)


image = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\images\logoses-removebg-preview.png")
image = image.subsample(4)
label2 = Label(root, image=image, bg='white')
label2.grid(row=0, column=0)

frame1 = ttk.Frame(root)
frame1.grid(row=1, column=0)


Label_creatacc = Label(frame1, text = "Create an Account", font=('cooper black', 18), bg='white')
Label_creatacc.grid(row = 1, columnspan=5)


words1 = StringVar()
words2 = StringVar()
words3 = StringVar()
words4 = StringVar()


frame2 = Frame(root, bg="white")
frame2.grid(row=3, column=0)

label_email = Label(frame2, text="Email:", fg ="black", font=('cooper black', 15), bg = "white")
label_email.grid(row = 3, column= 0 )


email_entry = Entry(frame2, textvariable=words1, width=12, font=('Arial 15'))
email_entry.grid(row = 3, column= 1, padx=10, pady=10)

label_username = Label(frame2, text ="Username:", font=('cooper black', 15), bg = "white")
label_username.grid(row = 4, column= 0)
 
username_entry = Entry(frame2, textvariable=words2, width=12, font=('Arial 15'))
username_entry.grid(row = 4, column= 1, padx=10, pady=10)

label_password = Label(frame2, text="Password:", font=('cooper black', 15), bg = "white")
label_password.grid(row = 5, column= 0)

password_entry = Entry(frame2, textvariable=words3, width=12, font=('Arial 15'), )
password_entry.grid(row = 5, column= 1, padx=10, pady=10)

label_password_confirm = Label(frame2, text="Confirm Password:", font=('cooper black', 15), bg = "white")
label_password_confirm.grid(row = 6, column= 0)

password_confirm_entry = Entry(frame2, textvariable=words4, width=12, font=('Arial 15' ), )
password_confirm_entry.grid(row = 6, column= 1, padx=10, pady=10)





click_btn= PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\images\Sign-Up-Button-Blue.png")
click_btn = click_btn.subsample(6)
button= Button(root, image=click_btn,borderwidth=0)
button.grid(row = 4, column = 0, pady=30)

image_bottom = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\images\footer2.png")
imagefooter = image_bottom.subsample(2)

labelfooter = Label(root, image=imagefooter, bg='white')
labelfooter.grid(row = 6, column= 0)











root.mainloop()
