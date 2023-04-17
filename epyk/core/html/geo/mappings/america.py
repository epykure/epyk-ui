n_c = {'Bahamas': 'bs',
       'Barbados': 'bb',
       'Belize': 'bz',
       'Canada': 'ca',
       'Costa Rica': 'cr',
       'Cuba': 'cu',
       'Dominican Republic': 'do',
       'El Salvador': 'sv',
       'Greenland': 'gl',
       'Guatemala': 'gt',
       'Haiti': 'ht',
       'Honduras': 'hn',
       'Jamaica': 'jm',
       'Mexico': 'mx',
       'Nicaragua': 'ni',
       'Panama': 'pa',
       'Trinidad and Tobago': 'tt',
       'United States of America': 'us'}

s_c = {'Argentina': 'ar',
       'Bolivia': 'bo',
       'Brazil': 'br',
       'Chile': 'cl',
       'Colombia': 'co',
       'Ecuador': 'ec',
       'Falkland Islands': 'fk',
       'French Guiana': 'gf',
       'Guyana': 'gy',
       'Paraguay': 'py',
       'Peru': 'pe',
       'Suriname': 'sr',
       'Uruguay': 'uy',
       'Venezuela': 've'}


if __name__ == "__main__":
    json_data = {}

    import pprint

    r_data = {}
    for k, v in json_data.items():
        r_data[v['name']] = k
    pprint.pprint(r_data)
