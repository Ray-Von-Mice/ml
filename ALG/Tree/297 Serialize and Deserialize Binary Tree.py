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
        inresult = ""
        def inodrdfs(node):
            if not node:
                return
            nonlocal inresult
            inodrdfs(node.left)
            inresult.append(str(node.val)+"#")
            inodrdfs(node.right)
        
        preresult = ""
        def preodrdfs(node):
            if not node:
                return
            nonlocal preresult
            preresult.append(str(node.val)+"#")
            preodrdfs(node.left)
            preodrdfs(node.right)
        
        inodrdfs(root)
        preodrdfs(root)
        return inresult + "||" + preresult
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        orders = data.split("||")
        inOrder, preOrder = orders[0].split("#"), orders[1].split("#")

        inOrder_dict, n = {}, len(preOrder)
        for val, indx in enumerate(inOrder):
            inOrder_dict[val] = indx
        
        curr_index = 0
        def depthTraverseBuild(left, right):
            if left > right:
                return None
            nonlocal curr_index
            curr_value = preOrder[curr_index]
            curr = TreeNode(curr_value)
            curr_index += 1
            centr = inOrder_dict[curr_value]
            curr.left = depthTraverseBuild(left, centr - 1)
            curr.right = depthTraverseBuild(centr + 1, right)
            return curr

        root = depthTraverseBuild(0, n - 1)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))