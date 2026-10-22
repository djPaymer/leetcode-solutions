# 242. Valid Anagram

[Problem on LeetCode](https://leetcode.com/problems/valid-anagram/)

Given two strings `s` and `t`, check whether `t` is an anagram of `s`, i.e. it contains exactly the same characters with the same counts, possibly in a different order.

Example: `s = "anagram"`, `t = "nagaram"` → `true`.

## Approach

1. If the lengths differ, they can't be anagrams.
2. Count the characters of `s` in a hash map (`Counter`).
3. Go through `t` and decrement the count for each character. If a count drops below zero, `t` has a character that `s` doesn't have enough of, so return `false`.

Since the lengths are equal, no negative count means all counts end at zero, so the answer is `true`.

A shorter alternative is `Counter(s) == Counter(t)`.

## Complexity

- Time: O(n)
- Space: O(k), where k is the number of distinct characters (O(1) for lowercase English letters)
