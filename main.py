from _sum import _sum, riskscore
from _sum import _sum, liquidity_score

if __name__ == '__main__':
    print("running main")
    print("the sum is ", _sum(20, 8))
    print("riskscore is", riskscore(10))
    print("liquidity score", liquidity_score(30))
