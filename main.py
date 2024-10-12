from math import factorial
import matplotlib.pyplot as plt
import numpy as np

def calculate_p0(y, n, M):
    series = sum(y ** i / factorial(i) for i in range(n + 1))
    corr = y ** (n + 1) * (1 - (y / n) ** M) / (factorial(n) * n * (1 - y / n))
    return (series + corr) ** -1

def calculate_pi(y, n, M, p0):
    return y ** (n + M) * p0 / (n ** M * factorial(n))

def calculate_l(y, n, M, p0):
    numerator = y ** (n + 1) * (1 - (y / n) ** M * (M + 1 - M / n * y)) * p0
    divider = factorial(n) * n * (1 - y / n) ** 2
    return numerator / divider


while True:
      choose = int(input("Ваш выбор: "))

      if choose == 1:
            # 2. В порту имеется один причал для разгрузки судов. Интенсивность потока судов равна 0.4 судов в 1 сут. Среднее время
            # разгрузки одного судна составляет 2 сут. Предполагается, что очередь может быть неограниченной длины. Найти показатели
            # эффективности работы причала, а также вероятность того, что ожидают разгрузки не более чем 2 судна.
            # Ответ: pо = 0.2, p1,2,3 = 0.3904, l = 3.2, w = 8 сут, m = 4, u = 10 сут.

            lambd = 0.4
            u = 1 / 2

            y = lambd / u

            p0 = (1 - y)
            p_zan = 1 - p0

            p1 = y ** 1 * (1 - y)
            p2 = y ** 2 * (1 - y)
            p3 = y ** 3 * (1 - y)

            P_k_leq_3 = p1 + p2 + p3

            m = y / (1 - y)
            u = m / lambd

            l = y ** 2 / (1 - y)
            w = l / lambd

            print(f"Вероятность простоя (p0): {round(p0, 1)}\n"
                  f"Вероятность того, что в очереди не более 3 судов (P1 + P2 + P3): {P_k_leq_3:.4f}\n"
                  f"Среднее число судов в очереди (l): {round(l, 1)}\n"
                  f"Среднее время ожидания в очереди (w): {round(w)} суток\n"
                  f"Среднее число судов в системе (m): {round(m, 1)}\n"
                  f"Среднее время пребывания судна в системе (u): {round(u, 1)} суток")
      elif choose == 2:
            # Задача с парикмахерской
            n, M = 3, 3  # 3 мастера и 3 стула
            lambd, u = 12, 3  # lambd = 12 клиентов в час, u = 1/20 минут = 3 клиентов в час

            y = lambd / u

            p0 = calculate_p0(y, n, M)
            pi = calculate_pi(y, n, M, p0)
            Q = 1 - pi
            lambd_ = lambd * Q
            k_zan = lambd_ / u
            l = calculate_l(y, n, M, p0)
            w = l / lambd
            m = l + k_zan
            u = m / lambd

            print(f"Ответ: p0 = {p0:.3f}, π = {pi:.3f}, Q = {Q:.3f}, lambd' = {lambd_:.2f}, "
                  f"k_зан = {k_zan:.2f}, l = {l:.2f}, w = {w:.2f} ч, m = {m:.2f}, u = {u:.2f} ч")

      elif choose == 0:
            print("Завершение программы")
            break
      else:
            continue