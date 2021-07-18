"""Fix problem between Image and ImageTk. Create a new Tk window for book
cover. Change the book cover side to median. Change some code to MVC style.
This code required third party library Pillow to function."""

import urllib.request
from PIL import Image


class model:
    def __init__(self):
        self.title = ''
        self.ISBN = ''
        self.picture = ''

    def open_url(self, url):
        """Function change information return from url to usable data type."""
        response = urllib.request.urlopen(url)
        img = response
        img = Image.open(img)
        response.close()
        return img
