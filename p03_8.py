import bisect

def pvalue(stat_num, input_list):
    sorted_list = sorted(input_list)
    index = bisect.bisect_left(sorted_list, stat_num)
    return 1 - (float(index) / len(sorted_list))
