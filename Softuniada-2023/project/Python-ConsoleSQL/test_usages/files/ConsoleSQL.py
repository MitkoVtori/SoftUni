import os
import shutil
from colorama import Fore


def create_database(database, *args):
    '''
        Console command
        CREATE DATABASE DataBaseName
    '''

    try:

        os.mkdir(f"databases/{database}"), os.mkdir(f"databases/{database}/files"), os.mkdir(f"databases/{database}/tables")

    except FileExistsError:
        return Fore.LIGHTWHITE_EX + "Database already exists"

    return Fore.LIGHTWHITE_EX + f"Database \"{database}\" was created"


def use_database(database, *args):
    '''
        Console command
        USE DATABASE DataBaseName
    '''

    if os.path.exists(f"databases/{database}/"):
        return [Fore.LIGHTWHITE_EX + f"Currently working with database \"{database}\"", database]

    return f"Database \"{database}\" not found!"


def create_table(database, table, values, *args):
    '''
        Console command
        CREATE TABLE TableName(id: int, name: str, age: float, more...)
    '''

    if os.path.exists(f"databases/{database}/tables/{table}.txt"):
        return Fore.LIGHTWHITE_EX + f"Table already exists!"

    table = open(f"databases/{database}/tables/{table}.txt", "a+")
    table.write(f"{values}\n\n")
    table.close()

    return Fore.LIGHTWHITE_EX + f"Table \"{table.name.split('/')[-1][:-4]}\" was created!"


def add_content_to_table(database, table, *content):
    '''
        Console command

        ADD TableName VALUES (
        (id, name, age, more...)
        (id, name, age)
        );

    '''

    try:

        with open(f"databases/{database}/tables/{table}.txt", "r") as file:

            values = [line for line in file][0]
            values_dictionary = {}

            for item in values[1:-2].split(", "):

                key, value = item.split(": ")
                values_dictionary[key] = value

            with open(f"databases/{database}/tables/{table}.txt", "a+") as write_file:

                for content_list in content:

                    content_dict = {}

                    for index, item in enumerate(values_dictionary.keys()):

                        content_dict[item] = content_list[index]

                        if type(content_dict[item]) is int and values_dictionary[item] == "'int'" or \
                                type(content_dict[item]) is str and values_dictionary[item] == "'str'" or \
                                    type(content_dict[item]) is float and values_dictionary[item] == "'float'":
                                        continue

                        return f"item \"{item}\" is type \'{type(content_dict[item])}\' and it must be \'{values_dictionary[item]}\'"

                    write_file.write(f"{content_dict}\n")

    except Exception as e:
        raise e

    return Fore.LIGHTWHITE_EX + "Content added to table!"


def create_file(database, file_name):
    '''
        Console command
        CREATE FILE FileName
    '''

    if os.path.exists(f"databases/{database}/files/{file_name}.txt"):
        return Fore.LIGHTWHITE_EX + "File already exists"

    file = open(f"databases/{database}/files/{file_name}.txt", 'x')
    file.close()

    return Fore.LIGHTWHITE_EX + f"File \"{file_name}\" was created!"


def write_in_file(database, file, *content):
    '''
        Console command
        WRITE IN FileName:
        Something isn't right.

        Some Messages!
        content, content, content,

        content, content,
        content,
        content,
        content
        ;;;
    '''

    if os.path.exists(f"databases/{database}/files/{file}.txt"):
        with open(f"databases/{database}/files/{file}.txt", "a+") as f:
            for line in content:
                f.write(f"{line}\n")

        return Fore.LIGHTWHITE_EX + "Content added to file!"

    return Fore.LIGHTWHITE_EX + f"Database \"{database}\" or File \"{file}\" not found!"


def check_table_content(database, table, *args):
    '''
        Console command
        GET ALL TableName
    '''

    if os.path.exists(f"databases/{database}/tables/{table}.txt"):
        file = open(f"databases/{database}/tables/{table}.txt", "r")

        return [Fore.LIGHTWHITE_EX + line for line in file][2:]

    print(Fore.LIGHTWHITE_EX + "Table not found!")
    return []


def check_file_content(database, file_name, *border):
    '''
        Console command
        GET FILE FileName
    '''

    if os.path.exists(f"databases/{database}/files/{file_name}.txt"):
        file = open(f"databases/{database}/files/{file_name}.txt", "r")

        return [Fore.LIGHTWHITE_EX + line for line in file]

    print(Fore.LIGHTWHITE_EX + "File not found!")
    return []


def delete_lines(database, path, file_name, *lines):
    '''
        Console command
        DEL TABLE/FILE FileName LINES firstline secondline seventhline
    '''

    if path == "table":

        if os.path.exists(f"databases/{database}/tables/{file_name}.txt"):

            file = [line[:-1] if line[-1] == '\n' else line for line in open(f"databases/{database}/tables/{file_name}.txt", "r")]

            for num, line in enumerate(lines):
                if 0 <= (line+1)-num < len(file):
                    file.pop((line+1)-num)

            os.remove(f"databases/{database}/tables/{file_name}.txt")
            f = open(f"databases/{database}/tables/{file_name}.txt", "a+")

            for line in file:
                f.write(f"{line}\n")

            f.close()

    elif path == "file":
        if os.path.exists(f"databases/{database}/files/{file_name}.txt"):

            file = [line[:-1] if line[-1] == '\n' else line for line in open(f"databases/{database}/files/{file_name}.txt", "r")]

            for num, line in enumerate(lines):
                if 0 <= (line - 1) - num < len(file):
                    file.pop((line - 1) - num)

            os.remove(f"databases/{database}/files/{file_name}.txt")
            f = open(f"databases/{database}/files/{file_name}.txt", "a+")

            for line in file:
                f.write(f"{line}\n")

            f.close()

    else:
        return Fore.LIGHTWHITE_EX + f"Invalid path name '{path}'"

    return Fore.LIGHTWHITE_EX + "lines removed!"


def drop_database(*databases):
    '''
        Console command

        One DataBase:
            FIRST WAY: DROP DB DataBaseName
            SECOND WAY: DROP DATABASE DataBaseName

        More Than One DataBases:
            FIRST WAY: DROP DBS FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
            SECOND WAY: DROP DATABASES FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
    '''

    for db in databases:
        if os.path.exists(f"databases/{db}/"):
            shutil.rmtree(f"databases/{db}/")

    return Fore.LIGHTWHITE_EX + "Database/s dropped!"


def drop_table(database, *tables):
    '''
        Console command

        One Table:
            DROP TABLE TableName

        More Than One Table:
            DROP TABLES FirstTableName SecondTableName ThirdTableName...
    '''

    for table in tables:
        if os.path.exists(f"databases/{database}/tables/{table}.txt"):
            os.remove(f"databases/{database}/tables/{table}.txt")

    return Fore.LIGHTWHITE_EX + "Table/s dropped!"


def delete_file(database, *files):
    '''
            Console command

            One File:
                DEL FILE FileName

            More Than One File:
                DEL FILES FirstFileName SecondFileName ThirdFileName...
        '''

    for file in files:
        if os.path.exists(f"databases/{database}/files/{file}.txt"):
            os.remove(f"databases/{database}/files/{file}.txt")

    return Fore.LIGHTWHITE_EX + "File/s deleted!"


def code_saver(user_input, code_file, new_line):
    '''
        Saves the code in the code file.
    '''

    file = open(f"src/{code_file}", "a+")
    file.write(f"{user_input}{new_line}")
    file.close()


def run_program():

    while True:
        db = input(Fore.LIGHTWHITE_EX + "create or use database: ")

        if db == 'create':
            create_db = input(Fore.LIGHTWHITE_EX + "database name: ")
            create_database(create_db)
            d = use_database(create_db)
            break

        elif db == "use":
            d = use_database(input(Fore.LIGHTWHITE_EX + "database name: "))[-1]
            break

    database = d

    while True:
        file = input(Fore.LIGHTWHITE_EX + "Create or choose file where to save the code from your console experience:\n")

        if not os.path.exists(f"src/{file}.txt"):
            f = open(f"src/{file}.txt", "x")
            f.close()

        if file:
            break

    file = f"{file}.txt"

    while True:

        operation_code = input()

        if operation_code == "END":
            break

        operation = operation_code.lower().split()

        code_saver(operation_code, file, '\n')

        if len(operation) >= 3:
            if operation[-1]:

                if operation[:-1] == ["create", "database"]:
                    print(create_database(operation[-1]))

                elif operation[:-1] == ["use", "database"]:

                    db = use_database(operation[-1])
                    print(db[0])
                    database = db[-1]

                elif operation[:2] == ["create", "table"]:

                    table_name = ' '.join(operation[2:])[:' '.join(operation[2:]).index("(")]
                    values = ' '.join(operation[2:])[' '.join(operation[2:]).index("(")+1:' '.join(operation[2:]).index(")")]
                    values_tuple = values.split(", ")
                    values_dict = {}

                    for items in values_tuple:

                        key, value = items.split(": ")
                        values_dict[key] = value

                    print(create_table(database, table_name, values_dict))

                elif operation[0] == "add" and operation[-2] == "values":

                    table = operation[1]

                    if operation[-1] == "(":

                        lst_values = []
                        item = input()

                        while item != ");":

                            code_saver(item, file, '\n')
                            items = item[1:-1].split(", ")

                            for index in range(len(items)):

                                if len(items[index].split(".")) == 2:
                                    if items[index].split(".")[0].isdigit() and items[index].split(".")[1].isdigit():
                                        items[index] = float(items[index])

                                elif items[index].isdigit():
                                    items[index] = int(items[index])

                            lst_values.append(items)
                            item = input()

                        code_saver(item, file, '\n\n\n')
                        print(add_content_to_table(database, table, *lst_values))

                elif operation[:-1] == ["create", "file"]:
                    print(create_file(database, operation[-1]))

                elif operation[:-1] == ["write", "in"]:

                    content = []
                    text = input()

                    while text[-3:] != ";;;":

                        code_saver(text, file, '\n')
                        content.append(text)
                        text = input()

                    if operation[-1][-1] == ':':
                        print(write_in_file(database, operation[-1][:-1], *content))

                    else:
                        print(write_in_file(database, operation[-1], *content))

                    code_saver(text[-3:], file, '\n\n\n')

                elif operation[0] == "get" and operation[1] == "all":

                    lines = check_table_content(database, operation[-1])
                    print()
                    [print(line) for line in lines]

                elif operation[:-1] == ["get", "file"]:

                    lines = check_file_content(database, operation[-1])
                    print()
                    [print(line) for line in lines]

                elif len(operation) >= 5:
                    if operation[0] == "del" and operation[3] == "lines":
                        try:

                            print(delete_lines(database, operation[1], operation[2], *[int(l) for l in operation[4:]]))

                        except ValueError:
                            print("line must be integer")

                elif operation[:-1] == ["drop", "db"] or operation[:-1] == ["drop", "database"] or operation[:2] == \
                    ["drop", "dbs"] or operation[:2] == ["drop", "databases"]:

                    dbs = operation[2:]
                    print(drop_database(*dbs))

                elif operation[:2] == ["drop", "table"] or operation[:2] == ["drop", "tables"]:
                    print(drop_table(database, *operation[2:]))

                elif operation[:2] == ["del", "file"] or operation[:2] == ["del", "files"]:
                    if "lines" not in operation:
                        print(delete_file(database, *operation[2:]))

