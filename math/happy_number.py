class Solution:
    def isHappy(self, n: int) -> bool:
        ns = set()
        while True:
            ns.add(n)
            n = sum([int(i) * int(i) for i in str(n)])
            if n == 1:
                return True
            if n in ns:
                return False
