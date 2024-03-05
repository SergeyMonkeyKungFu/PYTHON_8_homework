import numpy as np


def random_predict(number,left_b, right_b):
    """Угадываем число

    Args:
        number: Загаданное число

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(left_b, right_b+1)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def my_predict(number,left_b, right_b):
    """Угадываем число

    Args:
        number: Загаданное число

    Returns:
        int: Число попыток
    """
    count = 0
    
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    predict_number = (left_b + right_b) // 2
    
    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            left_b = predict_number + 1
        else:
            right_b = predict_number
            
        predict_number = (left_b + right_b) // 2
    return count


def score_game(predict,left_b, right_b):
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
       predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] 
    
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(left_b, right_b+1, size=(1000))  # загадали список из 1000 чисел

    for number in random_array:
        count_ls.append(predict(number,left_b,right_b))

    score = int(np.mean(count_ls))
    
    return score

