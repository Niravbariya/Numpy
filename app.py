nums = [25,12,36,95,14]
print(nums)

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

print(nums[2:])
print(nums[1:])


print(nums[-1])
print(nums[-5])



names = ['navin','kiran','john']
print(names)

values = [9.5,'Navin',25]
print(values)

print(values[0])
print(values[1])
print(values[2])




mil = [nums,names]
print(mil)

nums.append(45)
nums.append(56)
print(nums)


nums.insert(1,77)
print(nums)


nums.remove(14)
print(nums)

nums.pop(1)
print(nums)

nums.pop(5)
print(nums)


nums.pop()
nums.pop()
print(nums)


arr = [45,90,56,89]


# used for deleting multiple numbers
# del arr[-4:]
# print(arr)



arr.extend([23,34,78])
print(arr)

arr.sort()
print(arr)
