import itertools

def bestElf(calories):
    totalCaloriesPerElf = [sum(elfCalories) for elfCalories in calories]
    return max(totalCaloriesPerElf)


def caloriesSumFirstThreeElves(calories):
    totalCaloriesPerElf = [sum(elfCalories) for elfCalories in calories]
    firstThreeElves = sorted(totalCaloriesPerElf, reverse=True)[:3]
    return sum(firstThreeElves)


def convertLinesToListOfInts(lines):
    return map(int, lines.splitlines())


def caloriesTextToList(caloriesText):
    caloriesPerElfStrings = caloriesText.split("\n\n")
    caloriesPerElfValues = [list(convertLinesToListOfInts(caloriesPerElf)) for caloriesPerElf in caloriesPerElfStrings]
    return caloriesPerElfValues


def main():
    with(open("calories.txt", "r") as caloriesFile):
        fullFileContent = caloriesFile.read()
        caloriesList = caloriesTextToList(fullFileContent)
        print(bestElf(caloriesList))
        print(caloriesSumFirstThreeElves(caloriesList))


if __name__ == "__main__":
    main()
