pandas_datareader
=================

.. note:: Most of the components are expecting serializable objects so this is way we are using list of dictionary as a common
input source for components.

If you are using ``pandas_datareader`` in your script you can easily convert it to a valid input data by doing the below
for example::

    start = pd.to_datetime('2020-02-04')
    end = pd.to_datetime('today')

    tesla_df = data.DataReader('TSLA', 'yahoo', start, end)

    columns = ['Close', 'Open', 'Volume']
    records = []
    for rec in tesla_df[columns].to_records():
      records.append(dict(zip(['Date'] + columns, rec)))
      records[-1]['Date'] = pd.to_datetime(records[-1]['Date']).strftime('%Y-%m-%d')

This will create a records object using the method ``to_records()``
