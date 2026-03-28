class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        path_l = path.split("/")
        
        for token in path_l:
            if token == "..":
                if stack:
                    stack.pop()
            elif token != "" and token != ".":
                stack.append(token)
        
        return "/" + "/".join(stack)