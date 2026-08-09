class TreeNode:
    def __init__(self):
        self.mp = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.mp:
                curr.mp[c] = TreeNode()
            curr = curr.mp[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)
        

    def dfs(self, word, root):
        curr = root
        list_s = list(word)
        var = False

        for i, c in enumerate(word):
            if c not in curr.mp and c!=".":
                return False
            
            if c == ".":
                for key in curr.mp:
                    list_s[i] = key
                    stringa = "".join(list_s)
                    var = var or self.dfs(stringa[i :], curr)
                return var
            else:
                curr = curr.mp[c]

        return curr.end



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)