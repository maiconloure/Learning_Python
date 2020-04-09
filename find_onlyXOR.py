def find_unique(array1):  # Return the only element not duplicated
    missing = 0

    for number in array1:
        print(missing, ' - ', number)
        missing ^= number

    print(missing, ' - ', number)
    return missing


if __name__ == "__main__":
    array = [1, 9, 1, 9, 5, 6, 7, 8, 7, 8, 6]
    second_array = [1, 1, 2, 4, 5, 6, 5, 4, 6]

    print(f'find_unique({array}) --> ', find_unique(array))
    print()
    print(f'find_unique({second_array}) --> ', find_unique(second_array))