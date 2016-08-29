class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def streamInterval(start, end):
            count = start
            while True:
                if count > end:
                    raise StopIteration
                else:
                    yield count
                    count += 1
                    
        def streamFilter(pred, stream):
            while True:
                value = stream.next()
                if pred(value):
                    yield value
                    
        def sieve(stream):
            while True:
                value = stream.next()
                yield value
                stream = streamFilter(lambda x, value = value: x % value != 0, stream)
        
        count = 0
        for prime in sieve(streamInterval(2, n - 1)):
            count += 1
        return count
