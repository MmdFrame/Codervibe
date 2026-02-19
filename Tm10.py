# پیمایش عرضی (BFS)
def traverse_bfs(graph, start):
    queue = [start]
    visited = {start}

    while queue:
        v = queue.pop(0)
        for neigh in graph.get(v, []):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)

    return visited


# پیمایش عمقی (DFS) - بازگشتی
def traverse_dfs(graph, start, visited):
    visited.add(start)
    for neigh in graph.get(start, []):
        if neigh not in visited:
            traverse_dfs(graph, neigh, visited)


# ------------------ مرتب‌سازی ------------------

# مرتب‌سازی انتخابی (Selection Sort) - برمی‌گرداند لیست مرتب شده (کپی)
def selection_sort_simple(arr):
    a = arr[:]              # کپی تا لیست اصلی خراب نشود
    out = [0] * len(a)

    for i in range(len(a)):
        mn = float("inf")
        idx = -1
        for j in range(len(a)):
            if a[j] < mn:
                mn = a[j]
                idx = j
        out[i] = mn
        a[idx] = float("inf")

    return out


# مرتب‌سازی حبابی (Bubble Sort) - درجا مرتب می‌کند
def bubble_sort_inplace(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
