def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, size, value = items[i - 1]
        for j in range(capacity + 1):
            if size <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - size] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]

def get_selected_items(items, capacity, dp):
    n = len(items)
    j = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1][1]

    return selected_items

def arrange_inventory(selected_items):
    inventory = [[' ' for _ in range(4)] for _ in range(2)]
    row, col = 0, 0

    for item in selected_items:
        name, size, _ = item
        for _ in range(size):
            if col >= 4:
                row += 1
                col = 0
            if row >= 2:
                break
            inventory[row][col] = name[0] 
            col += 1

    return inventory

def find_all_combinations(items, capacity, dp):
    n = len(items)
    j = capacity
    combinations = []

    def backtrack(i, j, path):
        if i == 0 or j == 0:
            if j == 0:
                combinations.append(path)
            return
        if dp[i][j] == dp[i - 1][j]:
            backtrack(i - 1, j, path)
        if j >= items[i - 1][1] and dp[i][j] == dp[i - 1][j - items[i - 1][1]] + items[i - 1][2]:
            backtrack(i - 1, j - items[i - 1][1], path + [items[i - 1]])

    backtrack(n, capacity, [])
    return combinations

def main():
    items = [
        ('rifle', 3, 25),
        ('pistol', 2, 15),
        ('ammo', 2, 15),
        ('medkit', 2, 20),
        ('inhaler', 1, 5),
        ('knife', 1, 15),
        ('axe', 3, 20),
        ('talisman', 1, 25),
        ('flask', 1, 15),
        ('antidot', 1, 10),
        ('supplies', 2, 20),
        ('crossbow', 2, 20)
    ]

    inhaler = ('inhaler', 1, 5)
    items.remove(inhaler)

    capacity = 6

    dp = [[0] * (capacity + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        name, size, value = items[i - 1]
        for j in range(capacity + 1):
            if size <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - size] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    combinations = find_all_combinations(items, capacity, dp)

    for combo in combinations:
        combo.append(inhaler)

    for combo in combinations:
        total_value = sum(item[2] for item in combo) + 20  
        print(f"Итоговые очки выживания: {total_value}")
        print("Инвентарь:")
        inventory = arrange_inventory(combo)
        for row in inventory:
            print("[" + "],[".join(row) + "]")
        print()

if __name__ == "__main__":
    main()