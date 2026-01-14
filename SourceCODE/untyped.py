def myreduce(f, lst, init):
    result = init
    for i in range(len(lst)):
        result = f(result, lst[i])
    return result

def wider(cw, ci):
    return max(cw, len(ci))

myreduce(wider, [[1], [2, 3], [4]], 2)
myreduce(wider, ["apple", "banana", "orange"], 5)
myreduce(wider, [1, 2, 3, 4], 0)
