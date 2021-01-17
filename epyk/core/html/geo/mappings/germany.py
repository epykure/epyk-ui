
r = {'Baden-Württemberg': 'bw',
 'Bayern': 'by',
 'Berlin': 'be',
 'Brandenburg': 'bb',
 'Bremen': 'hb',
 'Hamburg': 'hh',
 'Hessen': 'he',
 'Mecklenburg-Vorpommern': 'mv',
 'Niedersachsen': 'ni',
 'Nordrhein-Westfalen': 'nw',
 'Rheinland-Pfalz': 'rp',
 'Saarland': 'sl',
 'Sachsen': 'sn',
 'Sachsen-Anhalt': 'st',
 'Schleswig-Holstein': 'sh',
 'Thüringen': 'th'}


if __name__ == "__main__":
  json_data = {}

  import pprint
  r_data = {}
  for k, v in json_data.items():
    r_data[v['name']] = k
  pprint.pprint(r_data)
