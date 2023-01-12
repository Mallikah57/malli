class solution:
    def lenght0fLastWord(self, s: str) -> int:
        s=s.strip()
        if s=="":
            return 0
        elif len(s.split())==1:
            return len(s)
        return len(s.split()[-1])
ob=solution()
print(ob.lenght0fLastWord("fly me to the moon"))
