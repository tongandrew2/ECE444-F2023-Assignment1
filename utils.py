class utils:
    def reversed(self, a):
        if isinstance(a, int) == False:
            return "Incorrect input; not an integer"

        reversed_num = 0
        while a != 0:
            temp = a % 10
            reversed_num = reversed_num * 10 + temp
            a //= 10
        return reversed_num
    def formatter(self, a):
        if isinstance(a, int) == False:
            return "Incorrect input; not an integer"
        return bin(a), oct(a)