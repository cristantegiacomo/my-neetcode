class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# 5 4 60 800 900 8
# A              B

# Alice all'inizio decide se scegliere la sequenza 5 60 900 oppure 4 800 8
# Fa la somma vede quale delle 2 è più alta e decide se partire a sx o a dx
# se Alice parte da sx avrà PER FORZA 5 60 900
# se Alice parte da dx avrà PER FORZA 4 800 8