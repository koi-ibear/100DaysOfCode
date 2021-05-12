"""
Medium 524. Longest Word in Dictionary through Deleting

Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.


Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"

"""
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
        for w in dictionary:
            wp = 0 # reset w pointer
            lw = len(w)
            for l in s:
                if wp < lw and w[wp] == l:
                    wp += 1
                if wp == lw:
                    return w
        return ""
                  
"""
"needle in hay"
needle: w, the str u have to scan thru
hay: where u pick needle from

template:
set needle pointer = 0
for i in hay:
    if pointer not moved to end AND i == needle[pt]:
        move needle pt
    if pointer moved ot end:
        return True (needle in hay)
return False

"""