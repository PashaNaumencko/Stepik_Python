'''
classes = {}
def search_parent(parent, child):
    if parent in classes[child] or parent == child:
        print("First cond")
        return True
    else:
        print("Second cond")
        #print("i:", i)
        return any([search_parent(parent, i) for i in classes[child]])
def input_data():
    for n in range(int(input())):
        link = input().split(" : ")
        if len(link) == 1:
            classes[link[0]] = []
        else:
            classes[link[0]] = link[1].split()
            for i in link[1].split():
                if i not in classes.keys():
                    classes[i] = []
    print(classes)
    for q in range(int(input())):
        request = input().split()
        print("Yes" if search_parent(request[0], request[1]) else "No")
input_data()
'''

classes = {}
def search_parent(parent, child):
    if parent in classes[child] or parent == child:
        return "Yes"
    else:
        for i in classes[child]:
            if search_parent(parent, i) == "Yes":
                return "Yes"
        return "No"
def input_data():
    for n in range(int(input())):
        link = input().split(" : ")
        if len(link) == 1:
            classes[link[0]] = []
        else:
            classes[link[0]] = link[1].split()
            for i in link[1].split():
                if i not in classes.keys():
                    classes[i] = []
    print(classes)
    for q in range(int(input())):
        request = input().split()
        print(search_parent(request[0], request[1]))
input_data()

