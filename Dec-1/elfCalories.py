import itertools

def bestElf(calories):
    totalCaloriesPerElf = [sum(elfCalories) for elfCalories in calories]
    return max(totalCaloriesPerElf)


def convertLinesToListOfInts(lines):
    return map(int, lines.splitlines())

def caloriesTextToList(caloriesText):
    caloriesPerElfStrings = caloriesText.split("\n\n")
    caloriesPerElfValues = [list(convertLinesToListOfInts(caloriesPerElf)) for caloriesPerElf in caloriesPerElfStrings]
    return caloriesPerElfValues

def main():
    with(open("calories.txt", "r") as caloriesFile):
        fullFileContent = caloriesFile.read()
        print(bestElf(caloriesTextToList(fullFileContent)))

if __name__ == "__main__":
    main()
