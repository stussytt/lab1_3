def count_common_elements(*lists):
    """
    Функция принимает N списков и возвращает количество одинаковых элементов в них.

    Args:
        *lists: произвольное количество списков

    Returns:
        int: количество элементов, присутствующих во всех списках
    """
    if not lists:
        return 0

    # Находим пересечение всех множеств
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))

    return len(common_elements)

# Пример использования
if __name__ == "__main__":
    # Тестовые примеры
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    list3 = [3, 4, 5, 6]

    result = count_common_elements(list1, list2, list3)
    print(f"Количество общих элементов: {result}")  # Должно быть 2 (3 и 4)
