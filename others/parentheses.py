class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = []

        for c in s:
            if c in parentheses:
                stack.append(parentheses[c])
            else:
                if not stack or c != stack.pop():
                    return False
        if stack:
            return False
        return True


class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return s == ''