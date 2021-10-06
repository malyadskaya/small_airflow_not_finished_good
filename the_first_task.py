from input_data import tasks, depending, influencing


class some_tasks:
    def __init__(self, just_dict: dict):
        self.just_dict = just_dict

    def first_option(self):
        updated_tasks = list(self.just_dict.keys())
        to_do_order = []
        for t in updated_tasks:
            if t not in depending and t not in influencing:
                to_do_order.append(t)
        for t in tasks:
            if t not in to_do_order and t not in depending:
                to_do_order.append(t)
        for t in depending:
            if all(item in to_do_order for item in self.just_dict[t]['deps']) is True:
                to_do_order.append(t)
        return to_do_order
