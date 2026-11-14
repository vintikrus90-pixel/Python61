db_is_available = False

print(db_is_available)
print(type(db_is_available))

db_is_available = True

print(db_is_available)

print(bool(90))
print(bool('abn'))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(None))

print(90 > 9)
print('Long string' > 'Short')
print([1, 2, 3] == [1, 2, 3])
print({'a': 1, 'b': 2})

int_num = 9
float_num = 9.2

print(int_num + float_num)


bool_val = True
int_val = 8

print(int_val + bool_val)

int_num = 9
float_num = 9.2
print(float_num + int_num)

bool_val = False
int_val = 8
print(int_val + bool_val)

int_num = 9
float_num = 9.2
print(float_num * int_num)

int_num = 90
float_num = 9.2
print(float_num.__rmul__(int_num))

int_num = 9
float_num = 9.2
print(int_num.__mul__(float_num))

int_num = 9
str_val = 'abn'

print(str_val * int_num)

empty_list = []
print(len(empty_list))

my_fruits = ['apple', 'banana', 'orange']
print(len(my_fruits))

posts_ids = [45, 67, 777, 89]
print(len(posts_ids))

user_inputs = [True, 'Andrey', '=)', 89.9]
print(len(user_inputs))

posts_ids = [45, 67, 777, 89]

posts_ids[1] = 999
posts_ids[2] = 999

print(posts_ids)




