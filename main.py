from typing import List
import ast

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

# EXPECTS THE EXACT FORMAT THAT WAS IN THE EXAMPLE
user_input = input("Input: ")

parts = user_input.split(", target = ")
nums = ast.literal_eval(parts[0].replace("nums = ", ""))
target = int(parts[1])

print("Output:", twoSum(nums, target))