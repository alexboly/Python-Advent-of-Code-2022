def bestElf(calories):
    totalCaloriesPerElf = [sum(elfCalories) for elfCalories in calories]
    return max(totalCaloriesPerElf)

def main():
    print(bestElf(calories))

if __name__ == "__main__":
    main()
