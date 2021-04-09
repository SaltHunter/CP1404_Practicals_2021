import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# On line 1 i see the number 10, the minium number i can see is 5, maximum of 20
# On Line 2 i see the number 5, Minimum number of 3, maximum of 20, cant produce a 4
# On Line 3 i see the number 5.241778794406521, Minimum Number of 2.5, maximum of 5.5

print(random.randint(0,101))