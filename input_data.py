tasks_dict = {1: {'deps': [], 'stat': ["pending", "in_progress", "done"], 'priority': 9},
              2: {'deps': [], 'stat': ["pending", "in_progress", "done"], 'priority': 0},
              3: {'deps': [], 'stat': ["pending", "in_progress", "done"], 'priority': 3},
              4: {'deps': [], 'stat': ["pending", "in_progress", "done"], 'priority': 1},
              5: {'deps': [1, 2, 3], 'stat': ["pending", "in_progress", "done"], 'priority': 5},
              6: {'deps': [], 'stat': ["pending", "in_progress", "done"], 'priority': 6},
              7: {'deps': [5, 6], 'stat': ["pending", "in_progress", "done"], 'priority': 8},
              8: {'deps': [6], 'stat': ["pending", "in_progress", "done"], 'priority': 8}
              }

tasks = list(tasks_dict.keys())

depending = set()   # {5, 7, 8}
for i in tasks:
    if len(tasks_dict[i]['deps']) != 0:
        depending.add(i)

influencing = set()     # {1, 2, 3, 5, 6}
for i in tasks:
    for j in tasks_dict[i]['deps']:
        influencing.add(j)
