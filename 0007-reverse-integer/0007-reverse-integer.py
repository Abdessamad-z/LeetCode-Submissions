class Solution:
    def reverse(self, x: int) -> int:
        c=False
        x=str(x)
        if x.startswith("-"):
            x=x[1:]
            c=True
        x=x[::-1]
        x=int(x)
        if c:
            x=-x
        if not -2**31 <= x <= 2**31 - 1:
            return 0
        return x