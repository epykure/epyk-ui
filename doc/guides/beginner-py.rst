Python beginner
===============

1. Install Python

To get this done got online on the `Python website <https://www.python.org/downloads/>`_ and download the lastest version available.

2. Install Eypk

.. note::

    Before this step you might want to install a virtual environment to not change your main Python setup.

To get Epyk install then::

    pip install epyk

This will download the most recent version from the centralised `Pypi repository <https://pypi.org/project/epyk/>`_

3. Create a project repository

With Epyk you will be able to generate from your data web pages.
To do so you will need to have a dedicated project and folder in which all the scripts to be transpiled are stored.

**It is also from this folder that all the CLI feature will be run**

4. Generate a demo script

Epyk provides a demo script to illustrate how its works.
This script is quite small but it provide good examples of components and interactivity.
To get it from your project, open a console and run the below command line::

    epyk.exe demo

Once this run you should see a file epyk_demo.py.

5. Get the web page

Then still in your folder run the below command line to get the web page automatically generated from your python code::

    epyk.exe transpile


5. Change the script

Now you can amend the script by for example changing ``mocks.popularity_2020`` to use your data instead.
Usually data in Epyk are lis of dictionaries, namely::

    my_data = [
        {"key1": "value1", "key2": "value2"},
        {"key1": "value1", "key2": "value2"},
        ....
    ]

But if you are using Pandas to simplify the data transformation you can easily get this object from any Pandas dataframe::

    my_df.to_dict(orient="records")

.. seealso::

    If you do not know where to start and not sure which data to use you can also have a look at this package
    ``pandas_datareader``. It will allow you to retrieve quite a lot of data to play with
