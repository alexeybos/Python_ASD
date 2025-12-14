class BitDictionary():
    def __init__(self, key_size):
        self.STORAGE_CAPACITY = 15
        self.key_size = key_size
        self.size = 0
        self.baskets = self._prepare_baskets(key_size)

    # Алгоритм (ключ типа "0101111001101000")
    # берем ключ, берем первые 4 бита - массив из 15 баcкетов
    # следующие 4 бита - адресация внутри баскета
    # следующие 4 бита - адресация внутри следующего баскета...
    def _prepare_baskets(self, remaining_bits: int) -> list:
        if remaining_bits <= 4:
            # массив для хранения значений
            return [None] * self.STORAGE_CAPACITY

        # Промежуточный уровень - массив указателей на следующие уровни
        basket = [None] * self.STORAGE_CAPACITY
        for i in range(self.STORAGE_CAPACITY):
            basket[i] = self._prepare_baskets(remaining_bits - 4)
        return basket

    def put(self, key: str, value) -> None:
        if self._is_key_size_invalid(key):
            raise ValueError(f"Key size should be {self.key_size}")

        i_key = int(key, 2)

        # Находим нужную корзину
        basket = self._get_basket(i_key)

        # Вычисляем индекс в корзине со значениями
        index = (i_key >> (self.key_size - 4)) & self.STORAGE_CAPACITY

        # Если ячейка была пустой, увеличиваем размер
        if basket[index] is None:
            self.size += 1

        # Сохраняем значение
        basket[index] = value

    def get(self, key: str):
        if self._is_key_size_invalid(key):
            return None

        i_key = int(key, 2)
        basket = self._get_basket(i_key)
        index = (i_key >> (self.key_size - 4)) & self.STORAGE_CAPACITY

        return basket[index]

    def _get_basket(self, i_key: int) -> list:
        mask = self.STORAGE_CAPACITY
        basket = self.baskets

        # Смещаем ключ до тех пор, пока не дойдем до листового уровня
        shift = self.key_size - 4
        while shift > 0:
            # Получаем индекс на текущем уровне
            index = (i_key >> shift) & mask
            basket = basket[index]
            shift -= 4

        return basket

    def delete(self, key: str) -> bool:
        if self._is_key_size_invalid(key):
            return False

        i_key = int(key, 2)
        basket = self._get_basket(i_key)
        index = (i_key >> (self.key_size - 4)) & self.STORAGE_CAPACITY

        if basket[index] is not None:
            basket[index] = None
            self.size -= 1
            return True # удален

        return False # не найден

    def _is_key_size_invalid(self, key: str) -> bool:
        """Проверка корректности размера ключа."""
        return len(key) != self.key_size

    def is_key(self, key: str) -> bool:
        """Проверка наличия ключа в словаре."""
        return self.get(key) is not None