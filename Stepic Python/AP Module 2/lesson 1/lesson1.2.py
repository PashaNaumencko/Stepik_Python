exceptions_dict = {}

def is_parent(parent, child):
    if parent in exceptions_dict[child]:
        return True
    else:
        for i in exceptions_dict[child]:
            if is_parent(parent, i):
                return True
        return False
def input_data():
    for n in range(int(input())):
        link = input().split(" : ")
        if len(link) == 1:
            exceptions_dict[link[0]] = []
        else:
            exceptions_dict[link[0]] = link[1].split()
            for i in link[1].split():
                if i not in exceptions_dict.keys():
                    exceptions_dict[i] = []
    exceptions_list = [input() for q in range(int(input()))]
    print(exceptions_dict)
    print(exceptions_list)
    counter = 0
    result_list = []
    for exception in exceptions_list[counter:]:
        for next_exception in exceptions_list[counter:]:
            #print(exception, "-->", next_exception)
            if is_parent(exception, next_exception) and next_exception not in result_list:
                result_list.append(next_exception)
        counter += 1
    print("\n".join([result_list[result_list.index(exception)] for exception in exceptions_list if exception in result_list]))
input_data()