class Solution:
    def say(self, s: str) -> str:
        if len(s) == 1:
            return "1" + s
        prev = s[0]
        counter = 1
        result = ""
        for ch in s[1:]:
            if ch == prev:
                counter += 1
            else:
                result += str(counter) + prev
                prev = ch
                counter = 1
        result += str(counter) + prev
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n-1))
