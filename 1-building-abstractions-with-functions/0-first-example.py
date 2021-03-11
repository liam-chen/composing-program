from urllib.request import urlopen

# Statements & Expressions
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

print(shakespeare)

# Objects.  An object seamlessly bundles together data and the logic that manipulates that data, in a way that manages the complexity of both.
words = set(shakespeare.read().decode().split())
print("words: ", words)

# a compound expression that evaluates to the set of all Shakespearian words that are simultaneously a word spelled in reverse.
reverse_6 = {w for w in words if len(w) == 6 and w[::-1] in words}
print(reverse_6)

# Interpreters
# Evaluating compound expressions requires a precise procedure that interprets code in a predictable way.

# functions are objects, objects are functions, and interpreters are instances of both.


