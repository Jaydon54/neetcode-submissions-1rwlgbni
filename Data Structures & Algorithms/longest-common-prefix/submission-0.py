class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = ""
        # iterate through characters of the first word
        for char_index in range(len(strs[0])):
            # compare this character with all other words
            for word_index in range(len(strs)):
                # check if word is shorter than index or character doesn't match
                if char_index >= len(strs[word_index]) or strs[word_index][char_index] != strs[0][char_index]:
                    return prefix
            prefix += strs[0][char_index]
        return prefix