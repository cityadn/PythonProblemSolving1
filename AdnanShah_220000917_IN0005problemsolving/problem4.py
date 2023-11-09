def sort(candies):
    candies.sort()
    return candies


def sum_of_candies(candies, extra_candies, last_element):
    for i in range(0, len(candies)):
        if (candies[i] + extra_candies) >= last_element:
          return "True"
        else:
          return "False"


candies = []
child_num = int(input("Enter number of Kids:\n"))
for i in range(0, child_num):
    candy_num = int(input("Enter number of candy for person {}:\n".format(i + 1)))
    candies.append(candy_num)
extra_candies = int(input("How many extra candies are there?\n"))
sort(candies)
last_element = candies.pop()
candies.append(last_element)
print(sum_of_candies(candies, extra_candies, last_element))
