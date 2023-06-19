from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("13DDT Project")
root.configure(bg="white")


#image = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project\images\logoses-removebg-preview.png")
#label2 = Label(root, image=image, bg='white')
#label2.grid(row=0, column=0)
image_top = PhotoImage(file=r"images\hometitle.PNG")
imagetop = image_top.subsample(2)

labeltop = Label(root, image=imagetop, bg='white')
labeltop.grid(row = 0, column= 0)


click_btn= PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project v1\images\track.PNG")
click_btn = click_btn.subsample(1)

button= Button(root, image=click_btn,borderwidth=5)
button.grid(row=6, column=0, padx=10, pady=5)

click_btn2= PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project v1\images\data.PNG")
click_btn2 = click_btn2.subsample(1)

button2= Button(root, image=click_btn2,borderwidth=5)
button2.grid(row=12, column=0, padx=10, pady=5)

click_btn3= PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project v1\images\info.PNG")
click_btn3 = click_btn3.subsample(1)

button3= Button(root, image=click_btn3,borderwidth=5)
button3.grid(row=18, column=0, padx=10, pady=5)


image_bottom = PhotoImage(file=r"C:\Users\Sihath Fernando\Downloads\Sihath Fernando 13DDT Project v1\images\Pro-Rank-Tracker-New-Features-Rankings-Discovery-Keyword-Suggestions.png")
imagefooter = image_bottom.subsample(3)

labelfooter = Label(root, image=imagefooter, bg='white')
labelfooter.grid(row = 20, column= 0)











root.mainloop()
