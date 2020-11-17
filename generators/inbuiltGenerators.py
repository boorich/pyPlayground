# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        # print(num)
        num += 1

sum_of_first_n = sum(firstn(100))
# list comprehension
doubles = [2 * n for n in range(50)]
print(doubles)
   
# same as the list comprehension above, but generator expression wrapped in a list-constructor
_doubles = list(2 * n for n in range(50))
print(_doubles)