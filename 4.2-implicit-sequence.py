class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def integer_stream(first):
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)

def map_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)

def filter_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()

def first_k_as_list(s, k):
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k-1
    return first_k

# using the sieve of Eratosthenes
def primes(pos_stream):
    def not_divible(x):
        return x % pos_stream.first != 0
    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))
    return Stream(pos_stream.first, compute_rest)

if __name__ == "__main__":
    s = integer_stream(3)
    m = map_stream(lambda x: x*x, s)
    generated_list = first_k_as_list(m, 5)


    prime_numbers = primes(integer_stream(2))
    first_k_as_list(prime_numbers, 7)