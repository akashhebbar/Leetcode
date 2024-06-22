class SampleGenerator:
    def generator_method(self):
        for i in range(0, 1):
            yield i


obj = SampleGenerator()

try:
    ans = obj.generator_method()
    print(next(ans))
    print(next(ans))
except StopIteration as e:
    print("Exception occured ", e)
