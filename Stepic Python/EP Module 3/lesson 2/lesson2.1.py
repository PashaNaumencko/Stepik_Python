def update_dictionary(d, key, value):
    print(key, value)
    if key in d.keys():
        d[key].append(value)
    elif 2 * key in d.keys():
        d[2 * key].append(value)
    else:
        d[2 * key] = [value]
x = {2: [3]}
print(x)
update_dictionary(x, 2, -5)
update_dictionary(x, 1, -1)
update_dictionary(x, 2, -2)
update_dictionary(x, 3, -3)
update_dictionary(x, 10, 15)
update_dictionary(x, 1, 2)
update_dictionary(x, 2, 3)
update_dictionary(x, 3, 4)
update_dictionary(x, 12, 3)
update_dictionary(x, 6, 5)
print(x)

