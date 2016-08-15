class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = self.getSkylineAux(buildings, 0, len(buildings) - 1)
        return [[contour[0], contour[2]] for contour in skyline]
        
    def getSkylineAux(self, buildings, start, end):
        if start > end:
            return []
        elif start == end:
            contour = buildings[start]
            return [[contour[0], contour[1], contour[2]], [contour[1], contour[1], 0]]
        else:
            mid = (start + end) / 2
            skyline1 = self.getSkylineAux(buildings, start, mid)
            skyline2 = self.getSkylineAux(buildings, mid + 1, end)
           # print skyline1, skyline2
            return self.merge(skyline1, skyline2)
    
    def merge(self, skyline1, skyline2):
        i = 0
        j = 0
        n1 = len(skyline1)
        n2 = len(skyline2)
        skyline = []
        #print "skylien1: ", skyline1, "skyline2: ", skyline2
        while i < n1 and j < n2:
            contour1 = skyline1[i]
            contour2 = skyline2[j]
            if contour1[0] == contour1[1]:
                if contour1[1] < contour2[0]:
                    skyline.append([contour1[0], contour2[0], 0])
                i += 1
            elif contour2[0] == contour2[1]:
                j += 1
            elif contour1[1] <= contour2[0]:
                skyline.append(contour1) 
                i += 1
            elif contour1[0] < contour2[0]:
                skyline.append([contour1[0], contour2[0], contour1[2]])
                contour1[0] = contour2[0]
            elif contour1[0] == contour2[0]:
                if contour1[1] == contour2[1]:
                    skyline.append([contour1[0], contour1[1], max(contour1[2], contour2[2])])
                    i += 1
                    j += 1
                elif contour1[1] < contour2[1]:
                    skyline.append([contour1[0], contour1[1], max(contour1[2], contour2[2])])
                    i += 1
                    contour2[0] = contour1[1]
                else:
                    skyline.append([contour2[0], contour2[1], max(contour1[2], contour2[2])])
                    contour1[0] = contour2[1]
                    j += 1
        if i >= n1:
            for k in range(j, n2):
                skyline.append(skyline2[k])
        else:
            for k in range(i, n1):
                skyline.append(skyline1[k])
        #print "skyline: ", skyline
        result = [skyline[0]]
        i = 1
        while i < len(skyline):
            if skyline[i][2] == result[-1][2]:
                while skyline[i][2] == result[-1][2]:
                    result[-1][1] = skyline[i][1]
                    i += 1
            else:
                result.append(skyline[i])
                i += 1
       #print "result: ", result
        return result
