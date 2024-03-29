class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + 65) + result
            # print("e", columnNumber)
            columnNumber //= 26
            # print(columnNumber)
        return result


# %% 
print(4 % 26)
print(111//26)

# %%
result =""

for i in range(1, 27):
    result +=  ">" +  result + ","

print(result)
# %%
