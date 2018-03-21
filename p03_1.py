def startsWith(string, substr_list):
    for i in range (len(substr_list)):
        if string.find(substr_list[i]) == 0:
            return True
    return False
