"""
# 二叉树解题框架
灵魂三问:
    1. 题目让我干嘛？
    2. 根节点该干嘛?
    3. 该用神马遍历?前/中/后
突发奇想: 是层序吗?

# 二叉搜索树解题框架
    1. 特性: 中序遍历得到递增序列(先右后左得到递减序列);
    2. 代码框架
    BST(TreeNode root, int target) {
        if (root.val == target)
            // 找到目标，做点什么
        if (root.val > target)
           BST(root.left, target)
        if (root.val < target)
           BST(root.right, target)
    }
"""