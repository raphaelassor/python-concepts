nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_nums = [n + 5 for n in nums]
print(new_nums)

new_nums = [n * 2 for n in range(1, 5)]
print(new_nums)

print('\n CONDITIONAL SEQUENCING\n')

new_nums=[n**2 for n in nums if n%2==0]
print(new_nums)

names=["ben","tom","gabriel","raphael"]
capitalized_names=[name.upper() for name in names]
print(capitalized_names)

short_names=[name for name in names if len(name)<5]
print(short_names)

