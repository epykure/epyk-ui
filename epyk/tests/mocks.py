
import random


def getSeries(count, size, negatives=0.1, missing=0.2):
  data = []
  #
  neg = size * [False]
  miss = size * [False]
  for s in range(size):
    data.append({"x": s, 'r': random.randint(0, 10), 'g': random.randint(0, 5)})
    for c in range(count):
      if miss[s]:
        continue

      data[-1][c] = random.randint(0, 10000) / 100 * (-1 if neg[s] else 1)
  return data


#
languages = [
  {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
  {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
  {"name": 'Python', 'type': 'script', 'rating': 9.12, 'change': 1.29},
  {"name": 'C++', 'type': 'code', 'rating': 6.13, 'change': -1.97},
  {"name": 'C#', 'type': 'code', 'rating': 4.29, 'change': 0.3},
  {"name": 'Visual Basic', 'type': 'script', 'rating': 4.18, 'change': -1.01},
  {"name": 'JavaScript', 'type': 'script', 'rating': 2.68, 'change': -0.01},
  {"name": 'PHP', 'type': 'script', 'rating': 2.49, 'change': 0},
  {"name": 'SQL', 'type': 'script', 'rating': 2.09, 'change': -0.47},
  {"name": 'R', 'type': 'script', 'rating': 1.85, 'change': 0.90},
]


#
popularity_2020 = [
  {'Language': 'Python', 'Rank': 1, 'Share': 30.8, 'Trend': 1.8},
  {'Language': 'Java', 'Rank': 2, 'Share': 16.79, 'Trend': -2.3},
  {'Language': 'JavaScript', 'Rank': 3, 'Share': 8.37, 'Trend': 0.3},
  {'Language': 'C#', 'Rank': 4, 'Share': 6.42, 'Trend': -0.9},
  {'Language': 'PHP', 'Rank': 5, 'Share': 5.92, 'Trend': -0.2},
  {'Language': 'C/C++', 'Rank': 6, 'Share': 5.78, 'Trend': -0.2},
  {'Language': 'R', 'Rank': 7, 'Share': 4.16, 'Trend': 0.4},
  {'Language': 'Objective-C', 'Rank': 8, 'Share': 3.57, 'Trend': 1},
  {'Language': 'Swift', 'Rank': 9, 'Share': 2.29, 'Trend': -0.2},
  {'Language': 'TypeScript', 'Rank': 10, 'Share': 1.84, 'Trend': 0},
  {'Language': 'Matlab', 'Rank': 11, 'Share': 1.65, 'Trend': -0.1},
  {'Language': 'Kotlin', 'Rank': 12, 'Share': 1.64, 'Trend': 0},
  {'Language': 'Go', 'Rank': 13, 'Share': 1.43, 'Trend': 0.2},
  {'Language': 'Ruby', 'Rank': 14, 'Share': 1.2, 'Trend': -0.2},
  {'Language': 'VBA', 'Rank': 15, 'Share': 1.11, 'Trend': -0.2},
  {'Language': 'Rust', 'Rank': 16, 'Share': 0.97, 'Trend': 0.3},
  {'Language': 'Scala', 'Rank': 17, 'Share': 0.87, 'Trend': -0.2},
  {'Language': 'Visual Basic', 'Rank': 18, 'Share': 0.78, 'Trend': -0.2},
  {'Language': 'Ada', 'Rank': 19, 'Share': 0.62, 'Trend': 0.3},
  {'Language': 'Lua', 'Rank': 20, 'Share': 0.58, 'Trend': 0.2},
  {'Language': 'Dart', 'Rank': 21, 'Share': 0.57, 'Trend': 0.2},
  {'Language': 'Perl', 'Rank': 22, 'Share': 0.47, 'Trend': -0.1},
  {'Language': 'Abap', 'Rank': 23, 'Share': 0.45, 'Trend': -0.1},
  {'Language': 'Groovy', 'Rank': 24, 'Share': 0.43, 'Trend': 0},
  {'Language': 'Julia', 'Rank': 25, 'Share': 0.41, 'Trend': 0.1},
  {'Language': 'Cobol', 'Rank': 26, 'Share': 0.32, 'Trend': 0},
  {'Language': 'Haskell', 'Rank': 27, 'Share': 0.29, 'Trend': 0},
  {'Language': 'Delphi', 'Rank': 28, 'Share': 0.27, 'Trend': 0}
]