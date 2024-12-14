#product sum numbers
import math
def checkPS(lis):
    if sum(lis) == math.prod(lis):
        return True
    else: return False


def minPS(n):
    