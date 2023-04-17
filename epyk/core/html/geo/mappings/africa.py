# Continent mappings
c = {'Algeria': 'dz',
     'Angola': 'ao',
     'Benin': 'bj',
     'Botswana': 'bw',
     'Burkina Faso': 'bf',
     'Burundi': 'bi',
     'Cameroon': 'cm',
     'Central African Republic': 'cf',
     'Chad': 'td',
     'Congo': 'cd',
     "Cote d'Ivoire": 'ci',
     'Djibouti': 'dj',
     'Egypt': 'eg',
     'Equatorial Guinea': 'gq',
     'Eritrea': 'er',
     'Ethiopia': 'et',
     'Gabon': 'ga',
     'Gambia': 'gm',
     'Ghana': 'gh',
     'Guinea': 'gn',
     'Guinea-Bissau': 'gw',
     'Kenya': 'ke',
     'Lesotho': 'ls',
     'Liberia': 'lr',
     'Libya': 'ly',
     'Madagascar': 'mg',
     'Malawi': 'mw',
     'Mali': 'ml',
     'Mauritania': 'mr',
     'Morocco': 'ma',
     'Mozambique': 'mz',
     'Namibia': 'na',
     'Niger': 'ne',
     'Nigeria': 'ng',
     'Rwanda': 'rw',
     'Senegal': 'sn',
     'Sierra Leone': 'sl',
     'Somalia': 'so',
     'South Africa': 'za',
     'Sudan': 'sd',
     'Swaziland': 'sz',
     'Tanzania': 'tz',
     'Togo': 'tg',
     'Tunisia': 'tn',
     'Uganda': 'ug',
     'Zambia': 'zm',
     'Zimbabwe': 'zw'}


if __name__ == "__main__":
    json_data = {}

    import pprint

    r_data = {}
    for k, v in json_data.items():
        r_data[v['name']] = k
    pprint.pprint(r_data)
