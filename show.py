# %% 
from arrayHash import Solution

solution = Solution()
print(solution.lengthOfLongestSubstring('abc'))
''' 
The `lengthOfLongestSubstring` function has a time 
complexity of O(n) and a space complexity of O(min(n, m)) because set() . 
'''

# %%


arr = [1000,1,3,7,8,-99,1000]
for i in range(len(arr)):
  if i > 0  and arr[i] == arr[i-1]:
    continue
# %%

# Step 1: Working with an array (list)
my_array = [1, 2, 3, 4, 5]  # Creating an array
my_array.append(6)  # Appending an element
print("Array after appending 6:", my_array)

# Accessing elements
print("First element:", my_array[0])  # Access the first element
print("Last element:", my_array[-1])  # Access the last element

# Slicing
print("First three elements:", my_array[:3])  # Get the first three elements

# Step 2: Working with hashing (dictionary)
# Let's count the occurrence of each element in the array
element_count = {}  # Creating a dictionary for hashing

for element in my_array:
    if element in element_count:  # Check if the element is already in the dictionary
        element_count[element] += 1  # Increment the count
    else:
        element_count[element] = 1  # Add the element with a count of 1

print("Element occurrence count:", element_count)

# %%
