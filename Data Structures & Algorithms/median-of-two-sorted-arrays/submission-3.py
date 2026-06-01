class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        if len(A) > len(B):
            A,B=B,A
        tot=len(A)+len(B)
        half=tot//2

        l,r=0,len(A)-1
        while True:
            m=(l+r)//2
            n=half-m-2
            Al=A[m] if m>=0 else -float('inf')
            Ar=A[m+1] if (m+1)<len(A) else float('inf')
            Bl=B[n] if n>=0 else -float('inf')
            Br=B[n+1] if (n+1)<len(B) else float('inf')
            
            if Al <= Br and Bl <= Ar:
                if tot%2:
                    return min(Ar,Br)
                else:
                    return (max(Al,Bl)+min(Ar,Br))/2
            elif Al > Br:
                r=m-1
            elif Bl > Ar:
                l=m+1
            
       