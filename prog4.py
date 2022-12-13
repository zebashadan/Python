def test(n):
    return[n+2*i for i in range(n)]
n = 2
print("number of piles:",n)
print("number of stones in each pile:")
print(test(n))