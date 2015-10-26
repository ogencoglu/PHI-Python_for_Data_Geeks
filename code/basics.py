# Basics - part 1

import numpy as np

my_list = [1,4,5,7,33]
print(len(my_list))

my_list[0]

my_list[0:2]

my_list[1:]

my_list[-1]

my_list2 = [my_list, [6,5,4,3,2]]

a = np.random.rand(3,4)
a[0]
a[:,2]

# copy / deepcopy
colours1 = ["red", "green"]
colours2 = colours1
colours2[1] = "blue"
