def binary_search_modified(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    #
    iterations = 0
    upper_border = None

    while low <= high:
        iterations += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            if upper_border is None or arr[mid] < upper_border:
                upper_border = arr[mid]

        # інакше x присутній на позиції і повертаємо його
        else:
            upper_border = arr[mid]
            break

    if upper_border is None and low < len(arr):
        upper_border = arr[low]

    return iterations, upper_border


if __name__ == "__main__":
    arr_of_d = [0.1, 0.9, 2.5, 4.39, 5.001, 6.5, 7]

    print(binary_search_modified(arr_of_d, 0.9))  # (2, 0.9)
    print(binary_search_modified(arr_of_d, 7))  # (3, 7)
    print(binary_search_modified(arr_of_d, 6))  # (3, 6.5)
    print(binary_search_modified(arr_of_d, -1))  # (3, 0.1)
    print(binary_search_modified(arr_of_d, 9))  # (3, None)
