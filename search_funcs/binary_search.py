def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid

    # якщо елемент не знайдений
    return -1


def binary_search_modified(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
    closest_max = None

    while low <= high:
        count += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            if closest_max is None or arr[mid] < closest_max:
                closest_max = arr[mid]

        # інакше x присутній на позиції і повертаємо його
        else:
            closest_max = arr[mid]
            break

    if closest_max is None and low < len(arr):
        closest_max = arr[low]

    return count, closest_max


if __name__ == "__main__":
    # arr = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 25, 28, 30]
    # index = binary_search(arr, 9)
    # print(index)

    arr_of_d = [0.1, 0.9, 1.5, 4.39, 5.001, 7]

    print(binary_search_modified(arr_of_d, 0.1))
    print(binary_search_modified(arr_of_d, 2.5))
    print(binary_search_modified(arr_of_d, 6))
