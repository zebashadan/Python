def test(list):
    return all(i in range(1000) and abs(i-j)>=10 for i in list for j in list if i!=j) and len(set(list))==100
nums = list(range(0,1000,10))
print("original list:")
print(nums)
print("check whether the list contain hundred integers")