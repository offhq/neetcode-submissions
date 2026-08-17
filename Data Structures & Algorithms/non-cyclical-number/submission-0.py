class Solution:
    def isHappy(self, n: int) -> bool:
        htbl = set()
        while True:
            suma = 0
            while n > 0:
                suma += (n%10)**2
                n //= 10
            n = suma
            if n in htbl:
                return False
            
            elif n == 1:
                return True
            htbl.add(n)
        