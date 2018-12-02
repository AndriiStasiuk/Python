def task5(arr):
    res = []
    for i in arr:
        if (type(i) == list or type(i) == tuple):
            task5(i)
        else:
            res.append(i)
    return res
