# Justin Hewlett
# CS 3430
# Assignment 4
#
# Methods to build a huffman tree from a string, encode strings, and decode strings

from operator import itemgetter

# Given a string, compute the frequency and return the representative huffman tree
def build_huffman_tree(txt):
    sorted_list = get_sorted_frequency_list(txt)

    # Continue until we have only one item left, the root of our final tree
    while len(sorted_list) > 1:
        
        # Combine first two items into a single tree
        combined_tree = make_huffman_tree(sorted_list[0], sorted_list[1])

        # Remove first two items
        sorted_list.pop(0)
        sorted_list.pop(0)

        sorted_list.append(combined_tree)

        #Sort by frequency
        sorted_list = sorted(sorted_list, key = lambda huff: get_freq(huff))

    return sorted_list

# Given a frequency table, convert to a list of tuples and sort the list by frequency
def get_sorted_frequency_list(txt):
    return sorted(get_frequency_table(txt).items(), key = itemgetter(1))

# Given a string, return a dictionary with a character as a key and the number of occurences of that character as the value
def get_frequency_table(txt):
    freq_table = {}
    for char in txt:
        if char in freq_table:
            freq_table[char] += 1
        else:
            # Add char to dict and initialize to 1
            freq_table[char] = 1

    return freq_table

def huffman_encode(symbols, huffman_tree):
    return huffman_encode_internal(symbols, huffman_tree, huffman_tree)

# Internal method that keeps track of the root of the tree
def huffman_encode_internal(symbols, huffman_tree, huffman_tree_root):
    if len(symbols) == 0:
        return []

    # If we're on a leaf, encoding of that symbol is finished.
    # Start with the next symbol at the root of the tree
    if is_leaf(huffman_tree):
        return huffman_encode_internal(symbols[1:], huffman_tree_root, huffman_tree_root)
    
    input_symbol = symbols[0]
	
    # Branch left or right in the tree and append the appropriate bit
    if get_symbols(get_left_branch(huffman_tree)).count(input_symbol) == 1:
        return [0] + huffman_encode_internal(symbols, get_left_branch(huffman_tree), huffman_tree_root)
    if get_symbols(get_right_branch(huffman_tree)).count(input_symbol) == 1:
        return [1] + huffman_encode_internal(symbols, get_right_branch(huffman_tree), huffman_tree_root)

    # We are not on a leaf node and the symbol was not found in either the left or right branches.
    # This means the symbol is not in the tree.
    raise Exception('Cannot encode symbol: ' + input_symbol)

def huffman_decode(bits, huffman_tree):
    if len(bits) == 0:
        return []
	
    return huffman_decode_internal(bits, huffman_tree, huffman_tree)

def huffman_decode_internal(bits, huffman_tree, huffman_tree_root):
    # We've reached a leaf node. Return the symbol and continue decoding the rest of
    # the sequence if there are more bits remaining
    if is_leaf(huffman_tree):
        symbol = get_symbols(huffman_tree)
        if len(bits) == 0:
            return symbol
        return symbol + huffman_decode_internal(bits, huffman_tree_root, huffman_tree_root)
    # We've exhaused all the bits and are on a non-leaf node. The sequence must be invalid.
    if len(bits) == 0:
        raise Exception('Incorrect bit string given.')

    current_bit = bits[0]

    # Branch left or right depending on the bit
    if current_bit == 0:
        return huffman_decode_internal(bits[1:], get_left_branch(huffman_tree), huffman_tree_root)
    if current_bit == 1:
        return huffman_decode_internal(bits[1:], get_right_branch(huffman_tree), huffman_tree_root)

    # A non-bit was supplied.
    raise Exception('Invalid token: ' + str(current_bit))

def make_leaf(symbol, freq):
    return (symbol, freq)

def is_leaf(x):
    return isinstance(x, tuple) and \
           len(x) == 2 and \
           isinstance(x[0], str) and \
           isinstance(x[1], int)

def get_leaf_symbol(leaf):
    return leaf[0]

def get_leaf_freq(leaf):
    return leaf[1]

def get_left_branch(huff_tree):
    return huff_tree[0]

def get_right_branch(huff_tree):
    return huff_tree[1]

def get_symbols(huff_tree):
    if is_leaf(huff_tree):
        return [get_leaf_symbol(huff_tree)]
    else:
        return huff_tree[2]

def get_freq(huff_tree):
    if is_leaf(huff_tree):
        return get_leaf_freq(huff_tree)
    else:
        return huff_tree[3]

def make_huffman_tree(left_branch, right_branch):
    return [left_branch,
            right_branch,
            get_symbols(left_branch) + get_symbols(right_branch),
            get_freq(left_branch) + get_freq(right_branch)]
