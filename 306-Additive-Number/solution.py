class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(n - 2):
            if i > 0 and num[0] == '0':
                break
            start1 = int(num[:i + 1])
            #print "a: ", start1
            for j in range(i + 1, n):
                if j > i + 1 and num[i + 1] == '0':
                    break
                start2 = int(num[i + 1 :j + 1])
                a = start1
                b = start2
                index = j + 1
                #print "b: ", b
                while True:
                    c = a + b
                    #print "a: ", a, " b: ", b, " c: ", c
                    size = len(str(c))
                    #print str(c), num[index:index + size]
                    if index + size > n:
                        break
                    elif index + size == n:
                        if str(c) == num[index:index + size]:
                            return True
                        else:
                            break
                    elif str(c) == num[index: index + size]:
                        a = b
                        b = c
                        index += size
                    else:
                        break
        return False