import files.ConsoleSQL as CS

CS.create_database("testdatabase")
CS.create_file("testdatabase", "testfile")
CS.write_in_file("testdatabase", "testfile", "firstLine", "secondLine", "thirdLine", "fourthLine")
CS.delete_lines("testdatabase", "file", "testfile", 1)
[print(line) for line in CS.check_file_content("testdatabase", "testfile")]
lines = [line for line in open("databases/testdatabase/files/testfile.txt", "r")][:-1]
[print(line) for line in lines]
CS.drop_database("testdatabase")
