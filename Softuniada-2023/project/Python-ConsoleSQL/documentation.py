from colorama import Fore


def documentation():
    return Fore.GREEN + f'''
Current Functionalities:

- Creating DataBase
- Using/Changing DataBase
- Creating Tables, Files and Queues
- Writing in Tables and Files
- Adding elements to Queues
- Checking the content of Tables, Files and Queues
- Deleting content from Tables, Files and Queues
- Deleting DataBases, Tables, Files and Queues

- Can be used in python files.
- Saves all the code in File.


{Fore.MAGENTA + "All commands can be in upper or lower case!"}

{Fore.GREEN + "1.How to create DataBase:"}
  - At first, you'll be asked to use or create database, 
    - if you choose to create database, it'll just ask you for the name.
  - Otherwise, if you want to create database while working,
    - Use the current command: CREATE DATABASE DataBaseName

2.How to use/change database:
 - At first, you'll be asked to use or create database, 
    - if you choose to use database, it'll just ask you for the name.
 - Otherwise, if you want to change the database you're working with,
    - Use the current command: USE DATABASE DataBaseName

3.How to create a table and save information in it:
 - To create a table, you need to use the main keywords "CREATE TABLE",
    - And then, the name of the table, containing information about the storage,
        - Example: TableName(id: int, name: str)
    - Console command: CREATE TABLE TableName(id: int, name: str, age: float, more...)
 - To write in table, you can see this Example:

        {Fore.CYAN + "ADD TableName VALUES ("}
        (id, name, age, more...)
        (id, name, age)
        );

{Fore.GREEN + "4.How to create file and write in it:"}
 - To create a file, use the following command: CREATE FILE FileName
 - To write in file, you need to start with the keywords "WRITE IN FileName:",
    - And then, write whatever you want on every new line.
    - To stop writing, you need to use ";;;".
 - Write Example:

        {Fore.CYAN + "WRITE IN FileName:"}
        Something isn't right.

        Some Messages!
        content, content, content,

        content, content,
        content,
        content,
        content
        ;;;

{Fore.GREEN + "5.How to create Queue:"}
 - To create queue, you must use one of the following commands:

        {Fore.MAGENTA + "CREATE QUEUE QueueName"}

        or

        CREATE QUE QueueName

        or

        CREATE Q QueueName

 {Fore.RED + '"NOTE!" You cannot remove any element from queue, every time you try to remove element, it will remove only the first one!'}

{Fore.GREEN + "6.How to add elements to queue:"}
 - To add elements in THE END of the queue, you should use this command:
    
    {Fore.LIGHTMAGENTA_EX + "ADD TO QueueName firstItem secondItem thirdItem"}

{Fore.GREEN + "7.How to remove element from queue:"}
 - Use this command:
 
    REMOVE FROM QueueName
 
 {Fore.RED + '"NOTE!" You can only remove the first element in the queue!'}

{Fore.GREEN + "8.How to see the content of my Tables, Files and Queues:"}
 - Use this command for Tables: GET ALL TableName
 - Use this command for Files: GET FILE FileName
 - Use this command for Queues: GET QueueName

9.How to delete content from files/tables:
 - Use this command for Tables: DEL TABLE TableName LINES firstline secondline seventhline
 - Use this command for Files: DEL FILE FileName LINES firstline secondline seventhline

10.How to delete DataBases, Tables, Files and Queues:
 - Delete DataBase/s:

    {Fore.MAGENTA + "One DataBase:"}
        FIRST WAY: DROP DB DataBaseName
        SECOND WAY: DROP DATABASE DataBaseName

    More Than One DataBases:
        FIRST WAY: DROP DBS FirstDataBaseName SecondDataBaseName ThirdDataBaseName...
        SECOND WAY: DROP DATABASES FirstDataBaseName SecondDataBaseName ThirdDataBaseName...

 {Fore.GREEN + "- Delete Tables:"}

    {Fore.MAGENTA + "One Table:"}
        DROP TABLE TableName

    More Than One Table:
        DROP TABLES FirstTableName SecondTableName ThirdTableName...

 {Fore.GREEN + "- Delete Files:"}

     {Fore.MAGENTA + "One File:"}
        DEL FILE FileName

     More Than One File:
        DEL FILES FirstFileName SecondFileName ThirdFileName...

 {Fore.GREEN + "- Delete Queues:"}
 
    {Fore.MAGENTA + "One Queue:"}
        DEL QUEUE QueueName

    More Than One Queue:
        DEL QUEUES FirstQueueName SecondQueueName ThirdQueueName...


{Fore.LIGHTGREEN_EX + "11.How to use the ConsoleSQL in Python code?"}
 - You can simply, just import the ConsoleSQL file and call the functions.
 For example, see the test_usages/ folder.

{Fore.LIGHTGREEN_EX + "12.How to save the code?"}
 - The code is saving by itself in the chosen at the beginning by you file, to change the file
 you must stop the program and rerun it. The file can be found in the same directory "src/filename"


Submit issues and questions here: https://github.com/MitkoVtori/Python-ConsoleSQL/issues/new

'''