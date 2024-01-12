class ReverseAString:
    def ___init___(self):
        pass

    def reverse_string(self, s):
        if s.__eq__(""):
            return ""
        newString = s[::-1]
        return newString

def test():
    pass

rev_str = ReverseAString()

print(rev_str.reverse_string(input("Type string to be reversed: ")))