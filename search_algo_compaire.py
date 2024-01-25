import timeit

from search_funcs.kpm_search import kmp_search
from search_funcs.boyer_moore_search import boyer_moore_search
from search_funcs.rabin_karp_search import rabin_karp_search


def outter_table_template(data):
    print(
        f"\n{'algorithm':<20} | {'time for exist str':<25} | {'time for fake str':<25}"
    )
    print(f"{'-'*20:<20} | {'-'*25:<25} | {'-'*25:<25}")

    for item in data:
        print(
            f"{item['title']:<20} | {item['time_exist']:<25} | {item['time_fake']:<25}"
        )


if __name__ == "__main__":
    lorem = "Lorem ipsum dolor"
    search_algorithms = [
        {
            "title": "Boyer-Moore",
            "method": boyer_moore_search,
        },
        {
            "title": "Knuth-Morris-Pratt",
            "method": kmp_search,
        },
        {
            "title": "Rabin-Karp",
            "method": rabin_karp_search,
        },
    ]

    # article 1
    with open("./article_1.txt", "r") as file:
        article_text = file.read()

    target = "Двійковий або логарифмічний пошук"

    for algo in search_algorithms:
        algo["time_exist"] = timeit.timeit(
            lambda: algo["method"](article_text, target), number=10
        )

        algo["time_fake"] = timeit.timeit(
            lambda: algo["method"](article_text, lorem), number=10
        )

    outter_table_template(search_algorithms)

    # article 2
    with open("./article_2.txt", "r", encoding="cp1251") as file:
        article_text = file.read()

    target = "linked list"

    for algo in search_algorithms:
        algo["time_exist"] = timeit.timeit(
            lambda: algo["method"](article_text, target), number=10
        )

        algo["time_fake"] = timeit.timeit(
            lambda: algo["method"](article_text, lorem), number=10
        )

    outter_table_template(search_algorithms)
