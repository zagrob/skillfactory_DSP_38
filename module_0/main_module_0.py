import numpy as np
# результат выполнения текущей попытки отгадывания
# 0 элемент - Загаднное число
# 1 элемент - С какой попытки отгадали  
result = []

# Список со значениями количества попыток для вычисления среднего значения
results_list = []

# Бинарный поиск 
def BinSearch():
    # счетчик попыток
    count = 1
    # загадали число
    number = np.random.randint(1,101)   
    # Минимальное число для генерации предполагаемого числа 
    predict_min = 1
    # Максимальное число для генерации предполагаемого числа
    predict_max = 100
    # среднее значение между макс. и мин.
    # предполагаемое число
    predict_avg = int(predict_max/2)
    
    # цикл пока не найдем загаданное число
    while True:
        # предполагаемое число совпадает с загаданным
        # если совпадает то выходим из цикла
        if predict_avg == number: break
       
        # загаданное число больше предполагаемого
        if number > predict_avg:
            # увеличиваем нижнюю границу области поиска 
            predict_min = predict_avg+1
        # загаданное число меньше предполагаемого
        else:
            # уменьшаем верхнюю границу области поиска
            predict_max = predict_avg-1
        # увеличиваем счетчик попыток
        count += 1
        
        # генерируем новое предполгаемое число
        predict_avg = int((predict_min+predict_max)/2)
    # возвращаем загаднное число и с какой попытки его угадали    
    return [number, count]
    

# цикл из 1000 
for n in range(1, 1001):
    #result = guess_number()
    result = BinSearch()

    results_list.append(result[1])
    print ('№ {0}. Загаданное число: {1}. Отгадано за {2} попыт(ки/ок).'.format(n, result[0], result[1]))


# вычисляем среднее количество попыток которое понадобилось для отгадывания
avg = int(sum(results_list)/len(results_list))

print('*********************************************************')
print ('Максимальное количество попыток: ', max(results_list))
print ('Минимальное количество попыток: ',  min(results_list))
print ('Среднее количество попыток: ', avg)
    