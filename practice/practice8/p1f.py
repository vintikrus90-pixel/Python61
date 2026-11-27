with open('example.txt', 'w') as file:
    file.write('hello world')

with open('example.txt', 'r') as file:
    print(file.read())