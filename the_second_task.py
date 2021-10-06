from input_data import tasks_dict, depending

# from tasks_dict will create sorted_tasks_dict sorted by priority
sorted_list = []
tasks_by_priority = []
sorted_tasks_dict = {}
for x in tasks_dict:
    sorted_list.append([x, tasks_dict[x]['priority']])
sorted_list.sort(key=lambda x: x[1], reverse=True)
for i in sorted_list:
    sorted_tasks_dict[i[0]] = tasks_dict[i[0]]
    tasks_by_priority.append(i[0])


class some_tasks_by_priority:
    def __init__(self, sorted_tasks_dict: dict):
        self.x = x
        self.sorted_tasks_dict = sorted_tasks_dict

    def sorting_tasks_by_priority(self, x):
        ans = []
        for i in tasks_by_priority:
            if i in x:
                ans.append(i)
        return ans


# separating for depending - that depends on others
    # , and influencing - be course ot which depending exist.
    depending = []      # [7, 8, 5]
    # influencing = []    # [1, 6, 3, 5, 2]
    deps = set()
    for i in sorted_tasks_dict.keys():
        if i not in depending and len(sorted_tasks_dict[i]['deps']) != 0:
            depending.append(i)
        for j in sorted_tasks_dict[i]['deps']:
            deps.add(j)
    # for k in sorted_tasks_dict.keys():
        # if k in deps:
        #     influencing.append(k)
    deps = list(deps)    # [1, 2, 3, 5, 6]

# Here will work only for the height of the tree <= 3, will need to add a reccurece of the same while here n times,
# where n is the height of the tree

    def second_option(self):
            order = []
            for i in self.sorted_tasks_dict.keys():
                while i not in order:
                    if i not in depending or all(item in order for item in self.sorted_tasks_dict[i]['deps']) is True:
                        order.append(i)
                    else:
                        while all(item in order for item in self.sorted_tasks_dict[i]['deps']) is not True:
                            for j in self.sorting_tasks_by_priority(self.sorted_tasks_dict[i]['deps']):
                                if j in order:
                                    pass
                                elif j not in depending or (all(item in order for item in self.sorted_tasks_dict[j]['deps']) is True):
                                    order.append(j)
                                else:
                                    while all(item in order for item in self.sorted_tasks_dict[j]['deps']) is not True:
                                        for k in self.sorting_tasks_by_priority(self.sorted_tasks_dict[j]['deps']):
                                            if k in order:
                                                pass
                                            elif k not in depending or all(item in order for item in self.sorted_tasks_dict[k]['deps']) is True:
                                                order.append(k)
            return order
