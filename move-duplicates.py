import csv

with open("C:/Users/israel.carvalho/duplicates.csv", "r", newline='', encoding='UTF-8') as csv_file:
    reader = list(csv.reader(csv_file, delimiter=",", lineterminator="\n"))
    lines = range(1, len(reader))
    index = 1
    column = 1
    count = 0
    file_location = ""

    for i in lines:
        for column_index in range(1, len(reader[index])):
            file_location = reader[index][column]
            print(file_location)
            column += 1
            count += 1
        column = 1
        index += 1
    print(f"Quantidade total de arquivos (original + cópias): {count + (len(reader) - 1)}")
    print(f"Quantidade de arquivos duplicados: {count}")
