class TrieNode:
    def __init__(self):
        self.children = {} # key: char val:TrieNode for char
        self.endOfWord = False # signifies end of a word at this char

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # pointer to track current node
        curr = self.root
        # iterate through each char in word
        for c in word:
            # adding new chars
            if c not in curr.children:
                # add char to curr children
                curr.children[c] = TrieNode()
            # move curr to new child or existing child
            curr = curr.children[c]
        # done w/ word, mark it
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True if curr.endOfWord else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        