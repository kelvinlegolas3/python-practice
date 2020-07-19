def myfunc(s):
    result = ""
    for idx, sub in enumerate(s):
        if idx % 2 == 0:
            sub.upper()
        else:
            sub.lower()
        result = result + sub
    return result

myfunc("HOTDOG")