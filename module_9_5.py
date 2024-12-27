# Определяем пользовательское исключение
class StepValueError(ValueError):
    pass  # Класс остается пустым, так как наследование достаточно

# Определяем класс Iterator
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:  # Проверяем, равен ли шаг 0
            raise StepValueError('шаг не может быть равен 0')  # Выбрасываем исключение, если шаг равен 0
        self.start = start  # Начальное значение
        self.stop = stop  # Конечное значение
        self.step = step  # Шаг итерации
        self.pointer = start  # Указатель на текущее значение

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем указатель на начальное значение
        return self  # Возвращаем сам объект итератора

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Завершаем итерацию, если указатель вышел за пределы

        current_value = self.pointer  # Сохраняем текущее значение для возврата
        self.pointer += self.step  # Увеличиваем указатель на шаг
        return current_value  # Возвращаем текущее значение


# Пример использования
try:
    iter1 = Iterator(100, 200, 0)  # Создаем итератор с шагом 0
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')  # Обрабатываем ошибку

# Создаем другие итераторы с различными параметрами
iter2 = Iterator(-5, 1)   # Итератор от -5 до 1 по умолчанию с шагом 1
iter3 = Iterator(6, 15, 2) # Итератор от 6 до 15 с шагом 2
iter4 = Iterator(5, 1, -1) # Итератор от 5 до 1 с шагом -1
iter5 = Iterator(10, 1)    # Итератор от 10 до 1 по умолчанию с шагом -1

# Итерация по iter2
for i in iter2:
    print(i, end=' ')
print()  # Переход на новую строку

# Итерация по iter3
for i in iter3:
    print(i, end=' ')
print()  # Переход на новую строку

# Итерация по iter4
for i in iter4:
    print(i, end=' ')
print()  # Переход на новую строку

# Итерация по iter5
for i in iter5:
    print(i, end=' ')
print()  # Переход на новую строку