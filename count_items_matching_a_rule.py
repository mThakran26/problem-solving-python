#Question: https://leetcode.com/problems/count-items-matching-a-rule/description/

# Solution:
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        match_count = 0
        for item in items:
            if (ruleKey == "type" and ruleValue == item[0]) or (ruleKey == "color" and ruleValue == item[1]) or (ruleKey == "name" and ruleValue == item[2]):
                match_count +=1

        return match_count	