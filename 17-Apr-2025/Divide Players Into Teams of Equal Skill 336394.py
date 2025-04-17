# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # sort skills
        skill.sort()

        #pair least and greatest skill

        start = 0
        end = len(skill) - 1

        chemistry  = 0
        skill_strength = skill[start] + skill[end]

        while start < end:
            if skill_strength != skill[start] + skill[end]:
                return -1
            team = skill[start] * skill[end]
            chemistry += team
            start += 1
            end -= 1

        return chemistry

