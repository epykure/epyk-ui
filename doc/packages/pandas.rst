Pandas
======

.. note:: Most of the components are expecting serializable objects so this is way we are using list of dictionary as a common
input source for components.

If you are using ``pandas`` in your script you can easily convert it to a valid input data by doing the below
for example::

    df = pd.DataFrame({
        "Animal": ["Mouse", "Rabbit", "Dog", "Tiger", "Elefant", "Wale"],
        "Weight [g]": [19, 3000, 40000, 200000, 6000000, 50000000]})

    line = page.ui.charts.apex.line(df.to_dict(orient="records"), y_columns=["Weight [g]"], x_axis="Animal")


This will create a records object using the method ``to_dict(orient="records")``
