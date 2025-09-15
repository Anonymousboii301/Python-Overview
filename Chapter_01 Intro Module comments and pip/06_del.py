# ✅ 3. del Statement
# The del keyword is used to delete a variable or an item from a list, dictionary, etc.

# 🔹 Deleting a Variable:


x = 100
del x
# print(x) → ❌ Error: x is not defined


# 🔹 Deleting List Elements:

nums = [10, 20, 30, 40]
del nums[2]
print(nums)  # [10, 20, 40]


# 🔹 Deleting Slices:

del nums[1:]   # deletes from index 1 to end
print(nums)    # [10]


# 🔹 Deleting Dictionary Keys:

person = {"name": "Batman", "age": 30}
del person["age"]
print(person)  # {'name': 'Batman'}