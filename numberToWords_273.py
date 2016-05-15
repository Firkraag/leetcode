#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        global billion, million, thousand, hundred
        
        billion = 10 ** 9
        million = 10 ** 6
        thousand = 1000
        hundred = 100
        mappings = dict()
        l = [(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (11, 'Eleven'), (12, 'Twelve'), (13, 'Thirteen'), (14, 'Fourteen'), (15, 'Fifteen'), (16, 'Sixteen'), (17, 'Seventeen'), (18, 'Eighteen'), (19, 'Nineteen'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty'), (50, 'Fifty'), (60, 'Sixty'), (70, 'Seventy'), (80, 'Eighty'), (90, 'Ninety')]
        for pair in l:
            mappings[pair[0]] = pair[1]
        l = list()
        self.numberToWordsAux(num, mappings, l)
        return ' '.join(l)
        
    def numberToWordsAux(self, num, mappings, l):
        global billion, million, thousand, hundred
        
        if num >= billion:
            self.numberToWordsAux(num / billion, mappings, l)
            l.append('Billion')
            if num % billion != 0:
                self.numberToWordsAux(num % billion, mappings, l)
        elif num >= million:
            self.numberToWordsAux(num / million, mappings, l)
            l.append('Million')
            if num % million != 0:
                self.numberToWordsAux(num % million, mappings, l)
        elif num >= thousand:
            self.numberToWordsAux(num / thousand, mappings, l)
            l.append('Thousand')
            if num % thousand != 0:
                self.numberToWordsAux(num % thousand, mappings, l)
        elif num >= hundred:
            self.numberToWordsAux(num / hundred, mappings, l)
            l.append('Hundred')
            if num % hundred:
                self.numberToWordsAux(num % hundred, mappings, l)
        else:
            if num in mappings:
                l.append(mappings[num])
            else:
                l.append(mappings[num - num % 10])
                l.append(mappings[num % 10])
