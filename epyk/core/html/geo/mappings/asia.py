# Continent mappings
c = {'Afghanistan': 'af',
     'Bangladesh': 'bd',
     'Bhutan': 'bt',
     'Brunei Darussalam': 'bn',
     'Cambodia': 'kh',
     'China': 'cn',
     'India': 'in',
     'Indonesia': 'id',
     'Iran': 'ir',
     'Iraq': 'iq',
     'Israel': 'il',
     'Japan': 'jp',
     'Jordan': 'jo',
     'Kazakhstan': 'kz',
     'Kuwait': 'kw',
     'Kyrgyz Republic': 'kg',
     "Lao People's Democratic Republic": 'la',
     'Lebanon': 'lb',
     'Malaysia': 'my',
     'Maldives': 'mv',
     'Mongolia': 'mn',
     'Myanmar': 'mm',
     'Nepal': 'np',
     'North Korea': 'kp',
     'Oman': 'om',
     'Pakistan': 'pk',
     'Philippines': 'ph',
     'Qatar': 'qa',
     'Russian Federation': 'ru',
     'Saudi Arabia': 'sa',
     'South Korea': 'kr',
     'Sri Lanka': 'lk',
     'Syrian Arab Republic': 'sy',
     'Taiwan': 'tw',
     'Tajikistan': 'tj',
     'Thailand': 'th',
     'Timor-Leste': 'tl',
     'Turkey': 'tr',
     'Turkmenistan': 'tm',
     'United Arab Emirates': 'ae',
     'Uzbekistan': 'uz',
     'Vietnam': 'vn',
     'Yemen': 'ye'}


if __name__ == "__main__":
    json_data = {}

    import pprint

    r_data = {}
    for k, v in json_data.items():
        r_data[v['name']] = k
    pprint.pprint(r_data)
