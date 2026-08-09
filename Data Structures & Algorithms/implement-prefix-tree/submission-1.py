class TreeNode:
    def __init__(self):
        self.mp = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.mp:
                curr.mp[word[i]] = TreeNode()
            curr = curr.mp[word[i]]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.mp:
                return False
            curr = curr.mp[word[i]]
        if curr.end:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in range(len(prefix)):
            if prefix[i] not in curr.mp:
                return False
            curr = curr.mp[prefix[i]]
        return True