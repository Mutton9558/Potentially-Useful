def longest_unique_substring(s: str) -> str:
    char_index = {}
    start = 0
    max_len = 0
    longest_substring = ""

    for i, char in enumerate(s):
      # checks if the character is in the dictionary and if its index is after the start of the substring
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = i
        current_len = i - start + 1

        if current_len > max_len:
            max_len = current_len
            longest_substring = s[start:i+1]

    return longest_substring

s = "teststring"
print(longest_unique_substring(s))
