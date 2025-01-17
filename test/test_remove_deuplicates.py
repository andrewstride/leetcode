from src.remove_duplicates import remove_duplicate_ints
import random


def test_returns_int():
    assert isinstance(remove_duplicate_ints([1, 2, 3]), int)


def test_small_ex():
    input_list = [1, 1, 2, 3]
    assert remove_duplicate_ints(input_list) == 3
    assert input_list[:3] == [1, 2, 3]


def test_large_ex():
    input_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 6]
    assert remove_duplicate_ints(input_list) == 6
    assert input_list[:6] == [1, 2, 3, 4, 5, 6]


def test_generate_multiple_tests():
    # run 100 random tests
    for _ in range(100):
        # generate list of random length and integers
        rand_length = random.randint(1, 100)
        rand_list = []
        for _ in range(rand_length):
            rand_list.append(random.randint(1, 100))
        # sort list into non-descending order
        rand_list.sort()
        # create list of unique integers
        unique = []
        for num in rand_list:
            if num not in unique:
                unique.append(num)
        # assert function returns number of unique integers (k)
        assert remove_duplicate_ints(rand_list) == len(unique)
        # assert first k integers are in non-descending order
        assert rand_list[: len(unique)] == sorted(unique)
