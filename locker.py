__author__ = 'tackettm'

# set upper bound for lockers
x = 100

# initialize the array to all false. False = close, True = open
lockers = [False for l in range(0, x)]

# loop 1 through upper bound
for i in range(1, x+1):
    # then, loop current index through upper bound, stepping by current index
    for j in range(i, x+1, i):
        # switch the locker
        lockers[j-1] = not lockers[j-1]

# print results
for l in range(0, x):
    print l+1, lockers[l]
