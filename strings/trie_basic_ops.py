import pprint

class Trie:
    def __init__(self, words=[]):
        self.trie = {}
        if words:
            self.build(words)


    def build(self, words):
        '''Adds words to existing trie.'''
        for word in words:
            curr_dict = self.trie
            print(f'word={word}')
            for char in word:
                print(f'\tchar={char}')
                if char not in curr_dict:
                    curr_dict[char] = {}
                curr_dict = curr_dict[char]
            # Add end of word marker
            curr_dict['*'] = True

        pp = pprint.PrettyPrinter()
        pp.pprint(self.trie)

    def __repr__(self):
        '''TODO: This should be a DFS'''
        pass


    def __len__(self):
        '''TODO'''

        words = 0
        t = self.trie
        while t:
            if '*' in t:
                words += 1
            else:
                pass
            # TODO...

        return words

    def search(self, word):
        curr_dict = self.trie
        for char in word:
            print(f'searching: char={char}, curr_dict.keys()={list(curr_dict.keys())}')
            if char in curr_dict:
                curr_dict = curr_dict[char]
            else:
                print(f'Did NOT find {word} -- Returning False')
                return False
        if '*' in curr_dict:
            print(f'Found {word} -- Returning True')
            return True
        print(f'Did NOT find {word} -- Returning False')
        return False
        

#---
# TEST CODE
#---

t = Trie()
t.build(['cat', 'cicada', 'mouse', 'cathode', 'dog', 'dongle', 'carry', 'more'])
assert t.search('cicada') == True
assert t.search('cicero') == False
assert t.search('dongle') == True
assert t.search('cat') == True
assert t.search('caution') == False

t = Trie()
t.build(['a'])
assert t.search('a') == True

t = Trie()
t.build([])
assert t.search('') == False
