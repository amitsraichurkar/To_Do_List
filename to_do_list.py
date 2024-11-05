title_ = '''
To-Do List

    python: v3.12

    code version: 1.0.0
    creation date: 05-11-2024 (dd-mm-yyyy)
    created by: Amit Raichurkar 

    SCOPE: 
        To generate and upate the To-do list in termnial.
        Also, to store the list once updated in text file ("to_do_list.txt")
'''

import os
from datetime import datetime
from pathlib import Path

def add_task(to_do_lst: list) -> None:
    '''Add task to the list'''

    task_status: str = 'o'
    task_time: str = datetime.now().strftime("%d/%m/%Y %H:%M")
    task_title: str = input('Provide Title for the task: ')
    # task_description: str = input('Describe the task:\n')
    
    # to_do_lst.append({'status':task_status,'time':task_time,'title':task_title,'description':task_description})
    to_do_lst.append({'status':task_status,'time':task_time,'title':task_title})

    return


def remove_task(to_do_lst: list) -> None:
    '''Remove/delete a task from the to_do_lst'''
    task_id: int = int(input('Enter Task ID to remove: '))
    del to_do_lst[task_id-1]

    return


def update_task(to_do_lst: list) -> None:
    '''Update a task for title, description or status'''

    id_: int = int(input('Enter Task ID to update: '))
    task_id: int = id_ - 1
    key_dict = {0:'status', 1: 'title'}

    pt_: int = int(input(f'What do you want to update {[f'{k}:{v}' for k,v in key_dict.items()]}: '))
    
    key_ = key_dict.get(pt_,None)
    if key_ is None:
        input(f'invalid option: {pt_}! Press <Enter> to continue')
        return
    print(f'''{id_}:{to_do_lst[task_id][key_]}''')

    to_do_lst[task_id][key_] = input('''Enter the update -> \n''')
    to_do_lst[task_id]['time'] = datetime.now().strftime("%d/%m/%Y %H:%M")

    return


def display_tasks(to_do_lst:list)->None:
    '''Display the to_do_lst data'''

    # print('''|-----------------------------------------------------------------------------------------|''')
    # print('''|-Status-|--ID----|--Time--------------|--Title-------------------------------------------|''')
    # print('''|-----------------------------------------------------------------------------------------|''')
    print(f'''|{"-"*8}+{"-"*8}+{"-"*20}+{"-"*50}|''')
    print(f'''|-Status-|--ID{"-"*4}|--Time{"-"*14}|--Title{"-"*43}|''')
    print(f'''|{"-"*8}+{"-"*8}+{"-"*20}+{"-"*50}|''')

    if to_do_lst:
        for i,itm in enumerate(to_do_lst):

            #f'''|{"-"*8}|{"-"*8}|{"-"*20}|{"-"*50}|'''
            # [task_status,task_time,task_title,task_description]
            print(f'''|{itm['status']:^8}|{i+1:^8}|{itm['time']:^20}|{itm['title']:<50.50}|''')

    else:
        i = '?'
        itm = list('?'*4)
        print(f'''|{itm[0]:^8}|{i:^8}|{itm[1]:^20}|{itm[2]:<50}|''')

    return


def display_task(to_do_lst:list)->None:
    '''Show description of a task'''
    check = 1
    while check==1:
        try:
            id_ = int(input('Enter a task ID to show task description: '))
            # print(f'[{to_do_lst[id_-1]['status']}] Title: {to_do_lst[id_-1]['title']} \n{to_do_lst[id_-1]['description']}')
            print(f'[{to_do_lst[id_-1]['status']}] Title: {to_do_lst[id_-1]['title']}')
            input('Press <enter> to continue...')
            break
        except BaseException as err:
            print(f'<ERROR>{err}')
            check = int(input('Enter 1 to re-try and 0 to exit: '))
    return


def read_to_do_file(file_path:Path)->list:
    '''read the to_do_list file and populate the to_do_lst'''
    to_do_lst = list()
    if file_path.exists():
        with open(file_path,'r') as file_:
            lines_ = file_.readlines()
            keys_ = ['status','_','time','title','description']
            for ln in lines_[1:]:
                dict_ = {k:v.strip() for k,v in zip(keys_,ln.split('|'))}
                to_do_lst.append(dict_)

    return to_do_lst


def store_to_do_lst(to_do_lst: list, file_path: Path)->None:
    '''Store to_do_lst in a file'''
    with open(file_path,'w') as _file:
        _file.write(f'''-Status-|--ID{"-"*4}|--Time{"-"*14}|--Title{"-"*43}\n''')
        for i,itm in enumerate(to_do_lst):
            line_ = f'''{itm['status']:^8}|{i+1:^8}|{itm['time']:^20}|{itm['title']:<50}\n'''
            _file.write(line_)
    return


if __name__ == '__main__':

    print(title_)

    file_path = Path('to_do_list.txt')
    to_do_lst = read_to_do_file(file_path)

    while True:
        display_tasks(to_do_lst)
        action_ = input('[a: add_task, r: remove_task, u: update_task, d:task_description, e:exit]: ')
        if action_ == 'e':
            store_to_do_lst(to_do_lst, file_path)
            os.system('cls' if os.name=='nt' else 'clear')
            break
        
        dict_action = {
            'a': add_task, 'r': remove_task,
            'u': update_task, 'd':display_task
        }
        dict_action.get(action_,display_tasks)(to_do_lst)
        store_to_do_lst(to_do_lst, file_path)
        os.system('cls' if os.name=='nt' else 'clear')
