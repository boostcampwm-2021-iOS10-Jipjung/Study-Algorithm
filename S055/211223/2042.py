class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        splited = s.split(" ")
        priv = -1
        for element in splited:
            if element.isdecimal():
                if int(element) > priv:
                    priv = int(element)
                else:
                    return False
        return True