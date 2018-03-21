def listSlice (data_list, int_list):
    adRet = []
    for i in range (len(int_list)):
        adRet.append(data_list[int_list[i]])
    return adRet
