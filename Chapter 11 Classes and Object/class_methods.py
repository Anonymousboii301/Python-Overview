class Math:
    def square(self, x):  # instance method
        return x * x

    @classmethod
    def cube(cls, x):     # class method
        return x ** 3

    @staticmethod
    def add(a, b):        # static method
        return a + b

m = Math()
print(m.square(4))     # 16
print(Math.cube(3))    # 27
print(Math.add(5, 7))  # 12
