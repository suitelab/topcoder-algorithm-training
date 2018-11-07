class KiwiJuiceEasy:
    def the_pouring(self, capacities, bottles, from_id, to_id):
        for i in range(len(from_id)):
            # 기존 주스(bottles[to_id[i]]) : min(from + to 주스, 기존 주스 병의 용량)
            # 옮길 주스(bottles[from_id[i]]) : (from + to 주스) - 기존 주스
            sum = bottles[from_id[i]] + bottles[to_id[i]]
            bottles[to_id[i]] = min(sum, capacities[to_id[i]])
            bottles[from_id[i]] = sum - bottles[to_id[i]]

        return bottles


my_class = KiwiJuiceEasy()

# Case# 0
capacities = [20, 20]
bottles = [5, 8]
from_id = [0]
to_id = [1]
labels = [0, 13]
returns = my_class.the_pouring(capacities, bottles, from_id, to_id)
print(returns, returns == labels)

# Case# 1
capacities = [10, 10]
bottles = [5, 8]
from_id = [0]
to_id = [1]
labels = [3, 10]
returns = my_class.the_pouring(capacities, bottles, from_id, to_id)
print(returns, returns == labels)

# Case# 2
capacities = [30, 20, 10]
bottles = [10, 5, 5]
from_id = [0, 1, 2]
to_id = [1, 2, 0]
labels = [10, 10, 0]
returns = my_class.the_pouring(capacities, bottles, from_id, to_id)
print(returns, returns == labels)

# Case# 3
capacities = [14, 35, 86, 58, 25, 62]
bottles = [6, 34, 27, 38, 9, 60]
from_id = [1, 2, 4, 5, 3, 3, 1, 0]
to_id = [0, 1, 2, 4, 2, 5, 3, 1]
labels = [0, 14, 65, 35, 25, 35]
returns = my_class.the_pouring(capacities, bottles, from_id, to_id)
print(returns, returns == labels)

# Case# 4
capacities = [700000, 800000, 900000, 1000000]
bottles = [478478, 478478, 478478, 478478]
from_id = [2, 3, 2, 0, 1]
to_id = [0, 1, 1, 3, 2]
labels = [0, 156956, 900000, 856956]
returns = my_class.the_pouring(capacities, bottles, from_id, to_id)
print(returns, returns == labels)
