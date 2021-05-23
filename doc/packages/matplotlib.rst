Matplotlib
==========

- Documentation: https://matplotlib.org/
- pypi alias: ``matplotlib``
- Package Type: Python


---------------------

Using a simple image component::

    import epyk as pk

    import numpy as np
    import matplotlib.pyplot as plt

    page = pk.Page()

    x = np.arange(0, 15, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

    img1 = page.ui.img(width=(50, "%"))
    img1.from_plot(plt)
    img1.style.css.display = "inline-block"

Using animated image::

    img1 = page.ui.images.animated("", text="This is a comment", title="Title", width=(49, "%"), url="#")
    img1.from_plot(plt)
    img1.style.css.borders()
    img1.style.css.display = "inline-block"

Using the carousel::

    page = pk.Page()

    import numpy as np
    import matplotlib.pyplot as plt

    carousel = page.ui.images.carousel()

    for i in range(10):
      x = np.arange(0, i * 5, 0.1)
      y = np.sin(x)
      plt.plot(x, y)
      carousel.add_plot(plt, width=(220, 'px'))

    carousel.set_nav_dots()

Using an external package slideshow::

    page = pk.Page()

    import numpy as np
    import matplotlib.pyplot as plt

    slideshow = page.ui.slideshow()

    for i in range(10):
      x = np.arange(0, i * 5, 0.1)
      y = np.sin(x)
      plt.plot(x, y)
      slideshow.add_plot(plt, width=(220, 'px'))

