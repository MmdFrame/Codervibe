"تابع پیجیدگی زمانی تکه برنامه زیر را بنویسید"
def example_loop(n):
    t = 0
    l = 1

    for i in range(0, n + 3, 3):
        t = t + 5
        l = 2 * l

    return t, l