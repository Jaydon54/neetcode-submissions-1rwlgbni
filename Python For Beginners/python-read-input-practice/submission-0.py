def add_two_numbers() -> int:
    vals = input()
    vals_split = vals.split(",")
    vals_list = []
    for v in vals_split:
        vals_list.append(int(v))
    return sum(vals_list)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
