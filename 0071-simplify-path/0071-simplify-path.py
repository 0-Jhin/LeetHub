class Solution(object):
    def simplifyPath(self, path):
        pathSplit = path.split("/")
        simplified = []
        canonical = "/"
        for i in pathSplit:
            if i == "..":
                if simplified:
                    simplified.pop()
            elif i != "." and i != "":
                simplified.append(i)
        canonical += "/".join(simplified)
        return canonical