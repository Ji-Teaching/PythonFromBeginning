from p03_1 import startsWith

def listStartsWith(string_list, substr_list):
    index_list = []
    for i in range(len(string_list)):
        if startsWith(string_list[i], substr_list):
            index_list.append(i)
    return index_list
