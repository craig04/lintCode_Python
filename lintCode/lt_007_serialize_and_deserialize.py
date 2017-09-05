class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''

    def serialize(self, root):
        data = []
        q = [root]
        i = 0
        while i != len(q):
            node = q[i]
            if node is None:
                data.append(None)
            else:
                data.append(node.val)
                q.append(node.left)
                q.append(node.right)
            i += 1
        return data

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''

    def deserialize(self, data):
        used = True
        fake = TreeNode(0)
        p = fake
        q = []
        i = 0
        for val in data:
            node = None
            if val is not None:
                node = TreeNode(val)
                q.append(node)
            if not used:
                p.left = node
            else:
                p.right = node
                if i != len(q):
                    p = q[i]
                    i += 1
            used = not used
        return fake.right
