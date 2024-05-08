# %%
for i in range(10):
    print(i)
# %%



# %%
# %%
# %%
for i in range(10):
  print(i)
# %%
# %%
# %%
nums = [0, 1, 0, 3, 12]
zero_count = nums.count(0)
nums[:] = [num for num in nums if num != 0]
nums.extend([0] * zero_count)
print(nums)
# %%
# %%

arr = [1,2,3]
arr.extend([0]*9)
arr
# %%
# integer ro roman number
# convert roman number to integer
def romanToInt(s: str) -> int:
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    prev = 0
    for char in s:
        current = roman_to_int[char]
        if current > prev:
            result += current - 2 * prev
        else:
            result += current
        prev = current
    return result

# %%
# MCMXCIV