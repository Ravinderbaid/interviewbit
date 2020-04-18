def cntoftripletlessthank(A,k):
    cnt=0
    n=len(A)
    for i in range(n):
        if(3*A[i]) > k:
            continue
        for j in range(i+1,n):
            s=A[i]+A[j]
            if s>(k-A[j]):
                continue
            ans=j
            lo,hi=j+1,n-1
            while lo<=hi:
                mid=(lo+hi)//2
                if s+A[mid]<k:
                    ans=mid
                    lo=mid+1
                else:
                    hi=mid-1
            cnt+=ans-j
   # print(k,cnt)
    return cnt
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        ans=0
        lo,hi=3,300000000
        while lo<=hi:
            mid=(lo+hi)//2
            if cntoftripletlessthank(A,mid) >= B:
                hi=mid-1
            else:
                ans=mid
                lo=mid+1
        return ans

