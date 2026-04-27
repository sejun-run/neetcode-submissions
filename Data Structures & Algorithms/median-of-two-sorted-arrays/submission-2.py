class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<=len(nums2):
            a,b=nums1,nums2
        else:
            a,b=nums2,nums1
        s,e=0,len(a)-1
        tot=len(a)+len(b)

        if tot%2:
            res=0
            med=tot//2+1
            if len(a)==0 or (len(b)>med-1 and b[med-1]<=a[0]):
                res= b[med-1]
            elif len(a)>med-1 and a[med-1]<=b[0]:
                res= a[med-1]
            else:
                while s<=e:
                    m=(s+e)//2
                    if len(b)-1 < med-m+1 or a[m]<=b[med-m-1]:
                        if len(a)-1< m+1 or a[m+1]>=b[med-m-2]:
                            res= max(a[m],b[med-m-2])
                            break
                        else:
                            s=m+1
                    else:
                        e=m-1
            return res
        else:
            res=0
            for med in [tot//2,tot//2+1]:
                s,e=0,len(a)-1
                if len(a)==0 or (len(b)>med-1 and b[med-1]<=a[0]):
                    res+= b[med-1]
                elif len(a)>med-1 and a[med-1]<=b[0]:
                    res+= a[med-1]
                else:
                    while s<=e:
                        m=(s+e)//2
                        print(m)
                        print(med-m-1)
                        if len(b)-1 < med-m+1 or a[m]<=b[med-m-1]:
                            if len(a)-1< m+1 or a[m+1]>=b[med-m-2]:
                                res+= max(a[m],b[med-m-2])
                                break
                            else:
                                s=m+1
                                print(s)
                        else:
                            e=m-1
                print(med,res)
            return res/2


        

            