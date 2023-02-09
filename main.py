def get_line():
    s=list(input('Введите данные: ').split())
    return (int(s[0]), s[1], s[2], int(s[3]), int(s[4]), int(s[5]))

def insert():
    line=input('Введите данные: ').split(',')
    if line not in data:
        data.append(line)

def print_data():
    m=max([len(i) for i in columns])
    for i in columns:
        print(str(i).ljust(m+1, ' '), end='')
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m+1, ' '), end='')
        print()

def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns))
        for line in data:
            line=[str(i) for i in line]
            file.write(','.join(line))

def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append(line)
    return columns, data

global data, columns

#columns, data = read_from_file('data.csv')
#print(data)
#insert(get_line())
#print_data()
#write_to_file('data.csv')

columns=('id', 'name', 'lastname', 'age', 'height', 'weight')
data = [
    (1, 'Ivan', 'Ivanov', 14, 160, 50),
    (2, 'Sasha', 'Sidorov', 15, 210, 40),
    (3, 'Masha', 'Poradina', 30, 178, 70),
    (4, 'Timur', 'Korolev', 44, 160, 120)
]

#columns, data = read_from_file('data.csv')

write_to_file('data.csv')



