class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i=0
        j=len(A)-1
        m=1000000007
        ans=0
        while(i<j):
            if(A[i]+A[j]==B):
                x = A[i]
                xx = i
                while (i < j and A[i] == x) :
                    i+=1 
                y = A[j]
                yy = j
                while (j >= i and A[j] == y):
                    j-=1 
                if (x == y):
                    temp = i - xx + yy - j - 1 
                    ans += (temp* (temp+ 1)) // 2
                    ans=ans%m
                else:
                    ans += (i- xx) * (yy - j); 
                    ans=ans%m;
    
            elif(A[i]+A[j]>B):
                j-=1
            else:
                i+=1
        return ans;
ś