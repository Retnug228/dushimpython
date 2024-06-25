class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(levels):
    if not levels:
        return None

    root = TreeNode(levels[0])
    queue = [root]
    i = 1

    while i < len(levels):
        current = queue.pop(0)
        if levels[i] is not None:
            current.left = TreeNode(levels[i])
            queue.append(current.left)
        i += 1
        if i < len(levels) and levels[i] is not None:
            current.right = TreeNode(levels[i])
            queue.append(current.right)
        i += 1

    return root


def find_paths(root):
    def dfs(node, path, paths):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            paths.append(list(path))
        else:
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)
        path.pop()

    paths = []
    dfs(root, [], paths)
    return paths


# Пример использования
levels1 = [1, 2, 3, None, 4]
levels2 = [1, -3, 6, None, 4, 101, None, 7, None]

root1 = build_tree(levels1)
root2 = build_tree(levels2)

print(find_paths(root1))  # Ожидаемый результат: [[1, 2, 4], [1, 3]]
print(find_paths(root2))  # Ожидаемый результат: [[1, -3, 4, 7], [1, 6, 101]]
