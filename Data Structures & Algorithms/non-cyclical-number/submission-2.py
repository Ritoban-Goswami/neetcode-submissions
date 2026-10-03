class Solution:
    def isHappy(self, n: int) -> bool:
        tortoise = n
        hare = self.getNext(n)

        while hare != 1 and tortoise != hare:
            tortoise = self.getNext(tortoise)
            hare = self.getNext(self.getNext(hare))

        return hare == 1

    def getNext(self, n: int) -> int:
        totalSum = 0

        while n > 0:
            n, d = divmod(n, 10)
            totalSum += d**2
        
        return totalSum