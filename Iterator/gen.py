def getDtata():
    for i in range(10):
        yield i


ans = getDtata()
print(next(ans))
print(next(ans))
print(next(ans))
