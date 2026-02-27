# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        preresult = []
        def preodrdfs(node):
            nonlocal preresult
            if not node:
                preresult.append("O")
                return
            preresult.append(str(node.val))
            preodrdfs(node.left)
            preodrdfs(node.right)
        
        preodrdfs(root)
        result = "#".join(preresult)
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preOrder = data.split("#")
        curr_index = 0
        def depthTraverseBuild():
            nonlocal curr_index
            if preOrder[curr_index] == "O":
                curr_index += 1
                return None
            node = TreeNode(int(preOrder[curr_index]), None, None)
            curr_index += 1
            node.left = depthTraverseBuild()
            node.right = depthTraverseBuild()
            return node

        root = depthTraverseBuild()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))