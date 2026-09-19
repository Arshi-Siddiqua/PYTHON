def fractional_knapsack(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    total_value = 0

    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break

    return total_value

weights = [10, 57, 20, 30]
values = [60, 100, 120, 400]
capacity = 90

result = fractional_knapsack(weights, values, capacity)
print("Maximum value:", result)