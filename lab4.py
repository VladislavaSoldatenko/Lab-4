def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item = items[i - 1]
        for j in range(capacity + 1):
            if item['size'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item['size']] + item['points'])
            else:
                dp[i][j] = dp[i - 1][j]
    
    selected_items = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1]['size']
    
    return selected_items, dp[n][capacity]

items = [
    {'name': 'r', 'size': 3, 'points': 25},
    {'name': 'p', 'size': 2, 'points': 15},
    {'name': 'a', 'size': 2, 'points': 15},
    {'name': 'm', 'size': 2, 'points': 20},
    {'name': 'k', 'size': 1, 'points': 15},
    {'name': 'x', 'size': 3, 'points': 20},
    {'name': 't', 'size': 1, 'points': 25},
    {'name': 'f', 'size': 1, 'points': 15},
    {'name': 'd', 'size': 1, 'points': 10},
    {'name': 's', 'size': 2, 'points': 20},
    {'name': 'c', 'size': 2, 'points': 20},
]

capacity = 7  
required_item = {'name': 'i', 'size': 1, 'points': 5}  

selected_items, total_points = knapsack(items, capacity)

selected_items.append(required_item)
total_points += required_item['points']

if total_points < 20:
    print("Невозможно набрать минимальные очки выживания (20).")
else:
    inventory = [[''] * 4 for _ in range(2)]
    row, col = 0, 0
    for item in selected_items:
        for _ in range(item['size']):
            inventory[row][col] = f"[{item['name']}]"
            col += 1
            if col >= 4:
                col = 0
                row += 1
                if row >= 2:
                    break
        if row >= 2:
            break

    print("Выбранные предметы:")
    for row in inventory:
        print(",".join(row))
    print(f"Итоговые очки выживания: {total_points}")