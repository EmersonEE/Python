all = "Emerson Aldair Pérez Rivera"

first_name = all.split()[0]
# last_name = all.split()[-1]
last_name = all.split()[-2]
new_name = all.split()[0:-2]
new_name = first_name + " "+ last_name
print(new_name)