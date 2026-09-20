import random
import statistics

def stats_calculator(*args, mode="basic"):
    print("\n#-# результаты расчетов #-#")
    print("режим:", mode)

    if mode == "basic":
        maximum = max(args)
        minimum = min(args)
        mean_val = statistics.mean(args)

        print("максимум:", maximum)
        print("минимум:", minimum)
        print("среднее арифметическое:", mean_val)

    elif mode == "advanced":
        maximum = max(args)
        minimum = min(args)
        mean_val = statistics.mean(args)
        median_val = statistics.median(args)
        mode_val = statistics.mode(args)

        print("максимум:", maximum)
        print("минимум:", minimum)
        print("среднее арифметическое:", mean_val)
        print("медиана:", median_val)
        print("мода:", mode_val)

    elif mode == "scientific":
        maximum = max(args)
        minimum = min(args)
        mean_val = statistics.mean(args)
        median_val = statistics.median(args)
        mode_val = statistics.mode(args)
        geom_mean = statistics.geometric_mean(args)
        harmonic_mean = statistics.harmonic_mean(args)

        print("максимум:", maximum)
        print("минимум:", minimum)
        print("среднее арифметическое:", mean_val)
        print("медиана:", median_val)
        print("мода:", mode_val)
        print("среднее геометрическое:", geom_mean)
        print("среднее гармоническое:", harmonic_mean)

    else:
        print("нету такого")

count = int(input("сколько чисел нужно сгенерировать? "))
start = int(input("введите нижнюю границу: "))
end = int(input("введите верхнюю границу: "))

numbers = []
for i in range(count):
    random_num = random.randint(start, end)
    numbers.append(random_num)

print("\nсгенерированные числа:", numbers)

user_mode = input(
    "выберите режим (basic / advanced / scientific) [по умолчанию basic]: "
)

if user_mode == "":
    user_mode = "basic"

stats_calculator(*numbers, mode=user_mode)