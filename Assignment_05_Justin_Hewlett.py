import unittest
import pdb

# Exception used to signify a missing key in the trie
class MissingKeyException(Exception):
    pass

# Exception used to signify the attempted insertion of a duplicate key 
class DuplicateKeyException(Exception):
    pass

# Given a key-value pair and a trie, inserts the key into the trie
# and puts the value in its bucket. If a duplicate key is inserted
# a DuplicateKeyException is raised
def insert_key(key, value, trie):
    if len(key) == 0:
        raise Exception("Key cannot be empty")

    current_char = key[0]

    contains_char, child_index = children_contain_char(trie, current_char)

    if contains_char:
        children = get_children(trie)
        
        if len(key) > 1:
            insert_key(key[1:], value, get_sub_trie(children, child_index))
        elif not is_end_of_word(children[child_index]):
            child = children[child_index]
            children[child_index] = (child[0], child[1], value)
        elif value != get_value(children[child_index]):
            raise DuplicateKeyException
    else:
        if len(key) == 1:
            append_child_end_of_word(current_char, value, trie)
        else:
            children = get_children(trie)
            sub_trie = [[]]
            insert_key(key[1:], value, sub_trie)
            children.append((current_char, sub_trie))
            
# Given a key and a trie, returns whether the key exists in the trie
def has_key(key, trie):
    try:
        retrieve_val(key, trie)
        return True
    except MissingKeyException:
        return False

# Given a key and a trie, returns the value associated with that key.
# If the key does not exist, a MissingKeyException is raised
def retrieve_val(key, trie):
    if len(key) == 0:
        raise MissingKeyException
    
    current_char = key[0]

    contains_char, child_index = children_contain_char(trie, current_char)
        
    if contains_char:
        children = get_children(trie)
        if len(key) == 1 and is_end_of_word(children[child_index]):
            return get_value(children[child_index])
        else:
            return retrieve_val(get_tail(key), get_sub_trie(get_children(trie), child_index))
    else:
        raise MissingKeyException

# Given a prefix and a trie, returns all keys in the trie that begin with that prefix
def start_with_prefix(prefix, trie):
    if len(prefix) == 0:
        return []
    
    sub_trie = traverse_to_prefix(prefix, trie)

    word_list = get_all_words(sub_trie, prefix)

    if has_key(prefix, trie):
        word_list = [prefix] + word_list

    return word_list

# Given a prefix, traverse to the end of that prefix in the trie and return the resulting sub trie
def traverse_to_prefix(prefix, trie):
    if len(prefix) == 0:
        return trie
    
    current_char = prefix[0]
    contains_char, child_index = children_contain_char(trie, current_char)

    if contains_char:
        return traverse_to_prefix(get_tail(prefix), get_sub_trie(get_children(trie), child_index)) 

# Given a trie, returns a list of all words formed by its children
def get_all_words(trie, prefix):
    children = get_children(trie)

    word_list = []

    if is_end_of_word(trie):
        word_list += prefix
        
    for child_index, child in enumerate(children):
        word = prefix + get_key(child)

        if is_end_of_word(child):
            word_list += [word]

        word_list += get_all_words(get_sub_trie(children, child_index), word)
        
    return word_list

# Given a trie and a character, returns whether the root node branches to that character
def children_contain_char(trie, char):
    children = get_children(trie)
    
    contains_char = False
    child_index = -1
    for child_index, child in enumerate(children):
        if get_key(child) == char:
            contains_char = True
            break
        
    return (contains_char, child_index)

def get_children(node):
    return node[0]

def get_key(child):
    return child[0]

def get_value(node):
    return node[2]

def get_sub_trie(children, child_index):
    return children[child_index][1]

def make_node_end_of_word(key, value):
    return (key, [[]], value)

def append_child_end_of_word(char, value, trie):
    children = get_children(trie)
    children.append(make_node_end_of_word(char, value))

def is_end_of_word(child_node):
    return isinstance(child_node, tuple) and len(child_node) == 3

def get_tail(string):
    return string[1:]

class TrieTests(unittest.TestCase):
    def test_start_with_prefix(self):
        trie = [[]]
        insert_key("tea", True, trie)
        insert_key("te", True, trie)
        insert_key("to", True, trie)
        insert_key("ten", True, trie)
        insert_key("tent", True, trie)
        insert_key("tentacle", True, trie)
        words_with_prefix = start_with_prefix("te", trie)
        self.assertEqual(['te', 'tea', 'ten', 'tent', 'tentacle'], words_with_prefix)
    
    def test_insert_key(self):
        trie = [[]]
        insert_key("ab", 5, trie)
        insert_key("ab", 5, trie)
        self.assertEqual([[('a',[[('b', [[]], 5)]])]], trie)

    def test_insert_key_key_already_exists_new_value_throws_exception(self):
        trie = [[]]
        insert_key("a", 5, trie)

        try:
            insert_key("a", 6, trie)
        except DuplicateKeyException:
            pass
        else:
            self.fail("Expected a DuplicateKeyException")

    def test_insert_key_sub_words(self):
        trie = [[]]
        insert_key("in", True, trie)
        insert_key("inn", True, trie)
        self.assertEqual([[('i', [[('n', [[('n', [[]], True)]], True)]])]], trie)

    def test_insert_key_sub_word_reverse(self):
        trie = [[]]
        insert_key("inn", True, trie)
        insert_key("in", True, trie)
        self.assertEqual([[('i', [[('n', [[('n', [[]], True)]], True)]])]], trie)

    def test_has_key_true(self):
        trie = [[]]
        insert_key("abc", True, trie)
        insert_key("ab", True, trie)
        self.assertTrue(has_key("ab", trie))

    def test_has_key_false(self):
        trie = [[]]
        insert_key("ba", True, trie)
        self.assertFalse(has_key("b", trie))

    def test_retrieve_val(self):
        trie = [[]]
        insert_key("abc", "def", trie)
        value = retrieve_val("abc", trie)
        self.assertEqual("def", value)

    def test_has_key_value_is_None(self):
        trie = [[]]
        insert_key("a", None, trie)
        self.assertTrue(has_key("a", trie))
                        
if __name__ == '__main__':
    unittest.main()


