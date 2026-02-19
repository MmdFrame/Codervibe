class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# تعداد کل نودهای درخت
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# تعداد برگ‌ها (نودی که هیچ فرزندی ندارد)
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


# تعداد نودهای درجه یک (فقط یک فرزند دارند)
def count_deg1(root):
    if root is None:
        return 0
    if (root.left is None and root.right is not None) or \
       (root.left is not None and root.right is None):
        return 1 + count_deg1(root.left) + count_deg1(root.right)
    return count_deg1(root.left) + count_deg1(root.right)


# تعداد نودهای درجه دو (دو فرزند دارند)
def count_deg2(root):
    if root is None:
        return 0
    if root.left is not None and root.right is not None:
        return 1 + count_deg2(root.left) + count_deg2(root.right)
    return count_deg2(root.left) + count_deg2(root.right)


# جمع کل مقادیر درخت
def sum_tree(root):
    if root is None:
        return 0
    return root.data + sum_tree(root.left) + sum_tree(root.right)


# جستجوی یک مقدار در درخت
def search(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    return search(root.left, target) or search(root.right, target)


# پیدا کردن بیشترین مقدار درخت
def max_tree(root):
    if root is None:
        return float("-inf")
    return max(root.data, max_tree(root.left), max_tree(root.right))