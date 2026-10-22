# 1. Two Sum

[Problem on LeetCode](https://leetcode.com/problems/two-sum/)

Find the indices of two numbers in an array that add up to `target`. Exactly one solution exists, and the same element can't be used twice.

Example: `nums = [2, 7, 11, 15]`, `target = 9` → `[0, 1]`.

## Approach

Iterate through the array, storing seen values and their indices in a hash map. For each `x`, check whether `target - x` is already in the map.

## Complexity

- Time: O(n)
- Space: O(n)
