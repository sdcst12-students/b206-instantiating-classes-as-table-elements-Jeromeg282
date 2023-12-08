import random
import statistics
#Rules: 
#each primary stat is generated as 3 random dice rolls (random 1-6) (strength, intelligance, piety, agility, stamina, charm)
# distribution of level is 1: 40%, 2: 30%, 3: 20%, 4: 10%
#each npc gets random 1-10 hp per level
# each npc gets some random money
# 30% chance to have 0-6 gold
# 50% chance go have 3-12 silver
# if they had no gold, they have a 75% chance to have 4-20 copper
# each gold is worth 10 silver and each silver is worth 10 copper
class NPC:
    stats = {'str': 0, 'int': 0, 'pie': 0, 'agi': 0, 'stm': 0, 'cha': 0}
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0

    def __init__(self):
        self.generate_stats()
        self.generate_level()
        self.generate_hp()
        self.generate_wealth()

    def generate_stats(self):
        self.stats['str'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['int'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['pie'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['agi'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['stm'] = sum(random.randint(1, 6) for _ in range(3))
        self.stats['cha'] = sum(random.randint(1, 6) for _ in range(3))

    def generate_level(self):
        self.level = random.choices([1, 2, 3, 4], weights=[40, 30, 20, 10])[0]

    def generate_hp(self):
        self.hp = random.randint(1, 10) * self.level

    def generate_wealth(self):
        if random.random() < 0.3:
            self.gold = random.randint(0, 6)
        elif random.random() < 0.5:
            self.silver = random.randint(3, 12)
        elif random.random() < 0.75:
            self.copper = random.randint(4, 20)

    def get_total_wealth(self):
        return self.gold * 10 * 10 + self.silver * 10 + self.copper

npcs = [NPC() for _ in range(100)]

level_distribution = {1: 0, 2: 0, 3: 0, 4: 0}
for npc in npcs:
    level_distribution[npc.level] += 1

print("Distribution of NPCs by Level:")
for level, count in level_distribution.items():
    print(f"Level {level}: {count} NPCs")

hp_values = [npc.hp for npc in npcs]
wealth_values = [npc.get_total_wealth() for npc in npcs]

print("\nMean and Standard Deviation for HP:")
print(f"Mean: {round(statistics.mean(hp_values), 2)}")
print(f"Standard Deviation: {round(statistics.stdev(hp_values), 2)}")

print("\nMean and Standard Deviation for Wealth (in copper):")
print(f"Mean: {round(statistics.mean(wealth_values), 2)}")
print(f"Standard Deviation: {round(statistics.stdev(wealth_values), 2)}")