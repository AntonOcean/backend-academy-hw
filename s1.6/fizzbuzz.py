class FizzBuzz:
    def fizz_buzz(self, value):
        if self.is_multiple(value, 3):
            if self.is_multiple(value, 5):
                return "FizzBuzz"
            return "Fizz"
        if self.is_multiple(value, 5):
            return "Buzz"
        return str(value)

    def is_multiple(self, value, mod):
        return (value % mod) == 0
