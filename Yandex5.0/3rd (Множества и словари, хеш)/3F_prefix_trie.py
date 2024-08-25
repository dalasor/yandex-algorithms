class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root


def find_shortest_prefix(trie, word):
    node = trie
    prefix = ""
    for char in word:
        if char in node.children:
            node = node.children[char]
            prefix += char
            if node.is_end_of_word:
                return prefix
        else:
            break
    return word


dict_words = input().split()
text_words = input().split()
trie = build_trie(dict_words)
text = [find_shortest_prefix(trie, word) for word in text_words]
print(' '.join(text))
