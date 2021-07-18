# import tkinter as t

# """I can not get tkinter running in a class, which is the problem I
# have here."""

# class view():
#     def __init__(self):
#         self.window1 = t.Tk()
#         self.user_input = t.Entry(self.window1)
#         self.input = None

#     def run(self):
#         text = t.Label(self.window1, text="Input book ISBN:")
#         button = t.Button(self.window1, text='Confirm',
#         command=self.get_input)

#         text.grid(row=0)
#         self.user_input.grid(row=0, column=1)
#         button.grid(row=1)

#         self.window1.mainloop()

#         return self.input

#     def get_input(self):
#         self.input = self.user_input.get()
#         self.window1.quit()

#     def display_picture(self):
#         pass

# if __name__ == '__main__':
#     x = view()
#     x.run()

"""Fix problem between Image and ImageTk. Create a new Tk window for book
cover. Change the book cover side to median. Change some code to MVC style.
This code required third party library Pillow to function."""

import tkinter as t
from PIL import ImageTk


class view():
    def __init__(self):
        self.window1 = t.Tk()
        self.window2 = None
        self.user_input = t.Entry(self.window1)
        self.input = None

    def run(self):
        text = t.Label(self.window1, text="Input book ISBN:")
        button = t.Button(self.window1, text='Confirm',
                          command=self.get_input)

        text.grid(row=0)
        self.user_input.grid(row=0, column=1)
        button.grid(row=1)

        self.window1.mainloop()

        return self.input

    def get_input(self):
        self.input = self.user_input.get()
        self.window1.destroy()

    def display_picture(self, img):
        self.window2 = t.Tk()

        img = ImageTk.PhotoImage(img)

        t.Label(self.window2, image=img).pack()

        button = t.Button(self.window2, text="Quit",
                          command=self.window2.destroy)
        button.pack()

        self.window2.mainloop()
