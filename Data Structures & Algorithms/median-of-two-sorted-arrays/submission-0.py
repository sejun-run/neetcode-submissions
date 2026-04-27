class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=0
        if len(nums1)<=len(nums2):
            a,b=nums1,nums2
        else:
            a,b=nums2,nums1
        s,e=0,len(a)-1
        tot=len(a)+len(b)

        if tot%2:
            med=tot//2+1-2
            while s<=e:
                m=(s+e)//2
                print(m,a[m],med-m+1)
                if len(b)-1 < med-m+1 or a[m]<b[med-m+1]:
                    if len(a)-1< m+1 or a[m+1]>b[med-m]:
                        res=(max(a[m],b[med-m]))
                        break
                    else:
                        s=m+1
                else:
                    e=m-1
            if e==-1:
                res=b[med+1]
            return res
        else:
            med=tot//2-2
            while s<=e:
                m=(s+e)//2
                print(m,a[m],med-m+1)
                if len(b)-1 < med-m+1 or a[m]<b[med-m+1]:
                    if len(a)-1< m+1 or a[m+1]>b[med-m]:
                        res=(max(a[m],b[med-m])+ min(a[m+1],b[med-m+1]))/2
                        break
                    else:
                        s=m+1
                else:
                    e=m-1
            if e==-1:
                res=b[med+1]
        return res

        

            