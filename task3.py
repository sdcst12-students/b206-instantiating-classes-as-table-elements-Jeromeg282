import random
import statistics
class NPC:
    stats = {
        'str' : 0,
        'int' : 0,
        'pie' : 0,
        'agi' : 0,
        'stm' : 0,
        'cha' : 0
          }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0

    def __init__(self):
        self.stats['str'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['int'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['pie'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['agi'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['stm'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['cha'] = sum(random.randint(1, 6) for _ in range(3))

        levelgen=random.choices([1,2,3,4], weights=[40,30,20,10][0])
        self.level=levelgen
        self.hp=random.randint(1,10) * self.level

        if random.random() <0.3:
            self.gold=random.randint(0,6)
        else:
            self.silver=random.randint(3, 12)
            if self.gold == 0 and random.random() < 0.75:
                self.copper=random.randint(4,20)

        self.wealth()
    def wealth(self):
        self.gold=0
        self.silver=0
        self.copper+=self.silver * 10
        self.copper+=self.gold * 10 * 10

        return
    
npcs = [NPC()for _ in range(100)]
levels= {level: sum(1 for npc in npcs if npc.level == level) for level in range(1,5)}
for level, count in levels.items():
    print(f"Level {level}: {count} NPCs")


hpval=[npc.hp for npc in npcs]
wealthval=[(npc.gold * 10 * 10) + (npc.silver * 10) + npc.copper for npc in npcs]
meancalc=statistics.mean(hpval)
sdcalc=statistics.stdev(hpval)

meanwealth=statistics.mean(wealthval)
sdcalcforwealth=statistics.stdev(wealthval)

print("\nStatistics for HP:")
print(f"Mean HP: {meancalc:.2f}")
print(f"Standard Deviation of HP: {sdcalcforwealth:.2f}")

print("\nStatistics for Wealth (in copper):")
print(f"Mean Wealth (in copper): {meanwealth:.2f}")
print(f"Standard Deviation of Wealth (in copper): {sdcalcforwealth:.2f}")

#Rules: 
# each primary stat is generated as 3 random dice rolls (random 1-6) (strength, intelligance, piety, agility, stamina, charm)
# distribution of level is 1: 40%, 2: 30%, 3: 20%, 4: 10%
# each npc gets random 1-10 hp per level
# each npc gets some random money
# 30% chance to have 0-6 gold
# 50% chance go have 3-12 silver
# if they had no gold, they have a 75% chance to have 4-20 copper
# each gold is worth 10 silver and each silver is worth 10 copper



