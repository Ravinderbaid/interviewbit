class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
        wL = wR = 0
        bestL = bestWindow = 0
        zeroCount = 0
        while wR < len(A): 
            if zeroCount <= B : 
                if A[wR] == 0 : 
                    zeroCount += 1
                wR += 1
            if zeroCount > B : 
                if A[wL] == 0 : 
                    zeroCount -= 1
                wL += 1
            if (wR-wL > bestWindow) and (zeroCount<=B) : 
                bestWindow = wR - wL 
                bestL = wL 
        r=[]
        for i in range(0, bestWindow): 
            r.append(bestL+i) 
        return r
	                    
	            