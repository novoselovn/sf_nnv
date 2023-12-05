"""Игра угадай число
Компьютер сам загадывает и сам угадывает число 
"""

import numpy as np

def binary_search(first_num, end_num, number, count):
    """Ищем число через бинарный поиск

    Args:
        first_num (int): первое число списка с искомым значением
        end_num (int): последнее число списка с искомым значением
        number (int): искомое значение
        count (int): количество итераций цикла while для поиска значения(число попыток)

    Returns:
        int: Число попыток
    """
    count += 1
    
    while True:
        my_result = (first_num + end_num) // 2 # находим среднее значение между началом и концом списка
        if number == my_result:# если искомое значение найдено, возвращаем Число попыток
            #print(my_result,count) # можно вернуть значение и число попыток
            return count
        if number < my_result: # если искомое значение меньше среднего, запускаем рекурсивно binary_search изменив начало и конец списка с искомым значением
            return binary_search(first_num, my_result-1, number, count)
         # если искомое значение больше среднего, запускаем рекурсивно binary_search изменив начало и конец списка с искомым значением
        return binary_search(my_result+1, end_num, number, count)
    
    
    

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1,101) # предполагаемое число
        
        if number == predict_number:
            return count  # возвращаем Число попыток, если угадали
        if predict_number < number:
            result = binary_search(predict_number, number, number, count=0)
            return result # возвращаем Число попыток бинарного поиска, если угадали 
        if predict_number > number:
            result = binary_search(number, predict_number, number, count=0)
            return result # возвращаем Число попыток бинарного поиска, если угадали
       
            


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
