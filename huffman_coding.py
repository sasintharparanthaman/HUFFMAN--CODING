# Get the input String
string = input("Enter a string :")

# Create tree nodes
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return f"{self.left}{self.right}" 

# Main function to implement huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculate frequency of occurrence
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Sort characters by frequency
nodes = sorted(freq.items(), key=lambda x: x[1])

# Build Huffman Tree
while len(nodes) > 1:
    (key1, val1) = nodes[0]
    (key2, val2) = nodes[1]
    nodes = nodes[2:]
    node = NodeTree(key1, key2)
    nodes.append((node, val1 + val2))
    nodes = sorted(nodes, key=lambda x: x[1])

# Print the characters and its huffmancode
# [5]: Print the characters and its huffmancode
huffmanCode = huffman_code_tree(nodes[0][0])
print(' Char | Huffman code ')
print('------------------')
# Use .items() to get (key, value) pairs from the frequency dictionary
for (char, frequency) in freq.items():
    print('%-4r | %12s' % (char, huffmanCode[char]))