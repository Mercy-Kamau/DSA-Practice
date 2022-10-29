array = [20, 30, 40, 50,60]
target = 130
def two_sum(array:list, target:int) -> list:
    i = 0
    while i < len(array):
        k = i + 1
        while k < len(array):
            if array[i] + array[k] == target:
                return[i, k]
            k = k + 1
            i = i + 1
        return[-1, -1] #if there's no answer
result = two_sum(array, target)
print(result)






    #for i, num in enumerate(array):

#array = [1, 2, 3, 4, 5]
#two_sum()

