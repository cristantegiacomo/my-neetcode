class TreeNode:
    def __init__(self):
        self.mp = {}


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        self.words = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.mp:
                curr.mp[word[i]] = TreeNode()
            curr = curr.mp[word[i]]


    def search(self, word: str) -> bool:
        if word in self.words:
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