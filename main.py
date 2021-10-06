from input_data import tasks_dict
from the_first_task import some_tasks
from the_second_task import some_tasks_by_priority, sorted_tasks_dict


if __name__ == '__main__':
    obj_1 = some_tasks(tasks_dict)
    print('first_option:', obj_1.first_option())

    obj_2 = some_tasks_by_priority(sorted_tasks_dict)
    print('first_option:', obj_2.second_option())
