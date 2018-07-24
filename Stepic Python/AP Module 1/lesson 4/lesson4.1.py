dictionary = {}
def create(namesp, parent):
    global dictionary
    dictionary[namesp] = [parent]
def add(namesp, var):
    global dictionary
    dictionary[namesp].append(var)
def get(namesp, var):
    global dictionary
    if var in dictionary[namesp][1:]:
        return namesp
    elif dictionary[namesp][0] is None:
        return None
    else:
        return get(dictionary[namesp][0], var)
def exec_command():
    create("global", None)
    for i in range(int(input())):
        cmd, namesp, args = input().split()
        if cmd == "create":
            create(namesp, args)
        elif cmd == "add":
            add(namesp, args)
        elif cmd == "get":
            print(get(namesp, args))
exec_command()