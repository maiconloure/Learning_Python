def find_unique(array):
    counter = {}

    for number in array:
        counter[number] = counter.get(number, 0) + 1

    for number, count in counter.items():
        if count == 1:
            return number


if __name__ == "__main__":
    array = [1, 9, 1, 9, 5, 6, 7, 8, 7, 8, 6]
    second_array = [1, 1, 2, 4, 5, 6, 5, 4, 6]

    print(f'find_unique({array}) --> ', find_unique(array))
    print(f'find_unique({second_array}) --> ', find_unique(second_array))