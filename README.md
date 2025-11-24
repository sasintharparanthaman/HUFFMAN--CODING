# Huffman-Coding
## Aim
To implement Huffman coding to compress the data using Python.

## Software Required
1. Anaconda - Python 3.7

## Algorithm:
### Step1:
Get the input string.
<br>


### Step2:
Create tree nodes.
<br>

### Step3:
Main function to implement huffman coding.
<br>

### Step4:
calculate frequency of occurance.
<br>

### Step5:
Print the characters and its huffmancode.
<br>

 
## Program:
```
Name : PRAKASH C
Reg.No : 212223240122
```

``` Python
# Get the input String
string = input("Enter a String :")


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



```
## Output:

### Print the characters and its huffmancode
<br>
<img width="204" height="26" alt="image" src="https://github.com/user-attachments/assets/650ab639-dcad-48af-95a5-fdc2d43b0768" />
<img width="218" height="149" alt="image" src="https://github.com/user-attachments/assets/cea8a832-4e70-4758-b1aa-0477031e5f34" />

<br>
<br>
<br>
<br>
<br>



## Result
Thus the huffman coding was implemented to compress the data using python programming.
