# Coding Examples Repository

Welcome to my coding examples repository! Below, you'll find three code snippets that demonstrate my coding skills. Each snippet addresses a different level of difficulty.

## Questions

### Easy

**Problem:** Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is defined as a maximal substring consisting of non-space characters only.

**Examples:**

1. **Input:** `s = "Hello World"`  
   **Output:** `5`  
   **Explanation:** The last word is "World" with length 5.

2. **Input:** `s = "   fly me   to   the moon  "`  
   **Output:** `4`  
   **Explanation:** The last word is "moon" with length 4.

3. **Input:** `s = "luffy is still joyboy"`  
   **Output:** `6`  
   **Explanation:** The last word is "joyboy" with length 6.

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

### Medium

**Problem:** Given an integer array of size `n`, find all elements that appear more than ⌊n/3⌋ times.

**Examples:**

1. **Input:** `nums = [3,2,3]`  
   **Output:** `[3]`

2. **Input:** `nums = [1]`  
   **Output:** `[1]`

3. **Input:** `nums = [1,2]`  
   **Output:** `[1,2]`

**Constraints:**

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

### Hard

**Problem:** Given an integer `n`, count the total number of digit `1` appearing in all non-negative integers less than or equal to `n`.

**Examples:**

1. **Input:** `n = 13`  
   **Output:** `6`

2. **Input:** `n = 0`  
   **Output:** `0`

**Constraints:**

- `0 <= n <= 10^9`
