## Represents a single node in the Trie



class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        output = []
        if self.is_word and suffix != '':
            output.append(suffix)
        if len(self.children) == 0:
            return output
        
        for char in self.children:
            output.extend(self.children[char].suffixes(suffix=suffix+char))

        return output

        

        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    def insert(self, word):
        ## Add a word to the Trie
        current_node  = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
    
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return node
    





MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)




from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');