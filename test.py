import lib

def test_count_elements():
    assert lib.count_elements([1, 2, 3], [2, 3, 4]) == 2
    assert lib.count_elements([1, 2], [3, 4]) == 0
    assert lib.count_elements([1, 2, 3], [1, 2, 3], [2, 3, 4]) == 2

if __name__ == "__main__":
    test_count_elements()
    print("Все тесты пройдены")
