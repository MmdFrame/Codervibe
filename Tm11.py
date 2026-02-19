def demo_loops_and_shift(size):
    # ---- بخش اول: دو حلقه تو در تو ----
    for row in range(size):
        for col in range(size):
            print(row)
            print(col)
            print(row + col)

    # ---- بخش دوم: یک حلقه با چند انتساب ----
    # مقداردهی اولیه (برای اینکه ارور نگیریم)
    x1, x2, x3, x4, x5 = 1, 2, 3, 4, 5

    for step in range(size - 2):
        x1 = x2
        x2 = x3
        x3 = x4
        x4 = x5
        # x5 اگر قرار است عوض شود باید مشخص کنی (فعلاً ثابت می‌ماند)

    return x1, x2, x3, x4, x5