a = [1, 11, 21, 1211, 111221]


# look and say sequence
def next(times):
    arr = []
    start = "1"
    for x in range(times):
        c = 0
        output = ""
        arr.append(start)
        input = str(start)
        for i in range(len(input)):
            c += 1
            n = input[i]
            if i + 1 < len(input):
                if input[i] != input[i + 1]:
                    output += str(c) + n
                    c = 0
                continue
            output += str(c) + n
        start = output
    return arr


arr = next(31)
print(len(arr[30]))
