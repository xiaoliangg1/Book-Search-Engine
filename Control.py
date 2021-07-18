# import urllib.request
# import View
# import model


# def open_url(url):
#     """Function change information return from url to usable data type."""
#     response = urllib.request.urlopen(url)
#     img = response.read()
#     response.close()
#     return img


# def user_search():
#     """Function that get information from url and print out the title of the
#     top five video title."""
#     x = View.view()
#     model.ISBN = x.run()
#     url = 'http://covers.openlibrary.org/b/isbn/' + model.ISBN + '-S.jpg'
#     model.picture = open_url(url)
#     model.picture = model.picture.decode('undefined')
#     print(model.picture)
#     print('0385472579')


# if __name__ == '__main__':
#     user_search()


"""Fix problem between Image and ImageTk. Create a new Tk window for book
cover. Change the book cover side to median. Change some code to MVC style.
This code required third party library Pillow to function."""


import View
import model


class control:
    def __init__(self):
        self.view = View.view()
        self.model = model.model()

    def user_search(self):
        """Function that get information from url and print out the title of the
        top five video title."""
        self.model.ISBN = self.view.run()
        url = 'http://covers.openlibrary.org/b/isbn/' + self.model.ISBN +\
              '-M.jpg'
        self.model.picture = self.model.open_url(url)
        self.view.display_picture(self.model.picture)


if __name__ == '__main__':
    x = control()
    x.user_search()
