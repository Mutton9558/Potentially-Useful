class Solution():
    def query(self):
        num = int(input("Enter a number greater than zero: "))
        self.num = num

    def isEven(self):
        if (self.num < 0):
            print("Invalid Number, please re-enter.")
            return 1
        else:
            if (self.num % 2 == 0):
                if self.num == 0:
                    print("The entered number is zero, please re-enter.")
                    return 1
                else:
                    print("even")
                    return 0
            else:
                print("odd")
                return 0

pp = Solution()
pp.query()
while pp.isEven() == 1:
    pp.query()
