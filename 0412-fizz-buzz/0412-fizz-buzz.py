class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numbers = []
        pattern = ""
        for i in range(1, n + 1): 
            pattern = str(i)
            if i % 3 == 0:
                pattern = "Fizz"
            if i % 5 == 0:
                pattern = "Buzz"
            if i % 3 == 0 and i % 5 == 0:
                pattern = "FizzBuzz"
            numbers.append(pattern)
        return numbers
        
        