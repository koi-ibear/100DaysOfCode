"""
Medium 299. Bulls and Cows


You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"
Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"

"""
class Solution:
    # def getHint(self, secret: str, guess: str) -> str:
    # """
    # 5% time 83& mem
    # """
    #     from collections import Counter
    #     cntr = dict(Counter(secret))
    #     bull = cow = 0
    #     for i in range(len(secret)):
    #         if secret[i] == guess[i]:
    #             bull += 1
    #             if cntr[guess[i]] < 1:
    #                 cow -= 1
    #             else:
    #                 cntr[guess[i]] -= 1
    #         elif guess[i] in cntr:
    #             if cntr[guess[i]] > 0:
    #                 cow += 1
    #                 cntr[guess[i]] += -1
    #     return str(bull)+'A'+str(cow)+'B'
    
    def getHint(self, secret: str, guess: str) -> str:
    # """
    # 48% time 30& mem
    # """
        bull = cow = 0
        cnt_s = {}
        cnt_g = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                cnt_s[secret[i]] = cnt_s.get(secret[i], 0) + 1
                cnt_g[guess[i]] = cnt_g.get(guess[i], 0) + 1
        for s in cnt_s:
            cow += min(cnt_s[s], cnt_g.get(s, 0))
        return str(bull)+'A'+str(cow)+'B'