# Given an object/dictionary with keys and values that consist of both strings and integers, design
# an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
data = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}
# Your algorithm should return 41, the sum of the values 23 and 18.


def sum_object(data):

    total = 0

    for item in data:
        if type(data[item]) == int:

            total = total + data[item]

    return total


# print(sum_object(data))

# print(data.values())


array = [56, 349, 22, -54, 0, 5]


def sort_array(array):
    new_array = []
    for item in range():
        if array[item] > array[item + 1]:
            new_array[item] = array[item+1]
            new_array[item+1] = array[item]
        else:
            new_array.append[item]
            new_array.append[item + 1]
    return new_array


print(0b1111)
