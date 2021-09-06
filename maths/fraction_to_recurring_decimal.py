class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        positive = (numerator < 0) is (denominator < 0)
        sign = '' if positive else '-'
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer, reminder = divmod(numerator, denominator)
        if reminder == 0:
            if integer == 0:
                return "0"
            return sign + str(integer)
        integer = sign + str(integer)

        reminders = dict()
        decimal = ''
        i = 0
        while reminder != 0 and reminder not in reminders:
            reminders[reminder] = i
            n, reminder = divmod(reminder * 10, denominator)
            decimal += str(n)
            i += 1

        if reminder in reminders:
            i = reminders[reminder]
            return integer + '.' + decimal[:i] + '(' + decimal[i:] + ')'
        else:
            return integer + '.' + decimal
