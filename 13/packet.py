from functools import total_ordering

class Packet:
    def __init__(self, content) -> None:
        self.content = content

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, type(self)) and self.content == __o.content

    def __lt__(self, __o) -> bool:
        return isinstance(__o, Packet) and self.compare(self.content, __o.content)

    def __str__(self) -> str:
        return str(self.content)

    def compare(self, left, right):

        leftIsInt = isinstance(left, int)
        rightIsInt = isinstance(right, int)

        if leftIsInt and rightIsInt:
            valid = right - left
            if valid > 0:
                return True
            elif valid < 0:
                return False
            else:
                return None
        
        elif leftIsInt:
            left = [left]
        
        elif rightIsInt:
            right = [right]

        lenLeft = len(left)
        for i, val in enumerate(right):
            if i < lenLeft:
                valid = self.compare(left[i],val)
                if valid != None:
                    return valid
            else:
                return True
                
        
        if lenLeft > len(right):
            return False
        else:
            return None
