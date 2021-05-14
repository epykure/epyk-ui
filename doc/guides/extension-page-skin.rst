Page skins
==========

There is also a notion of skin to the page to add nice backgrounds to your page.
All the skins are accessible from the ``page.skins`` property

Currently few skins are available::

    def rains(self, width=(100, '%'), height=(100, '%'), options=None, profile=None)

    def winter(self, width=(100, '%'), height=(100, '%'), options=None, profile=None)

    def matrix(self, width=(100, '%'), height=(100, '%'), options=None, profile=None)

    def fireworks(self, width=(100, '%'), height=(100, '%'), options=None, profile=None)

    def lights(self, width=(100, '%'), height=(100, '%'), options=None, profile=None

For example the below lines will add a Matrix style to your page::

    page = pk.Page()

    page.skins.matrix()
    page.ui.div("This is a text")

By transpiling the file with the below command you get a nice HTML page with the code inside::

    epyk.exe transpile -s=N

This could be a easy and nice way to adapt and change your web site based on the season :).


