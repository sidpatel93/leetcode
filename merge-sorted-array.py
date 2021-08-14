def merge(nums1,nums2,m,n):
    p1 = m-1 
    p2 = n-1
    i = m+n-1

    while(p2 >=0):
        if(p1>=0 and nums1[p1]>nums2[p2]):
            nums1[i] = nums1[p1]
            i-=1
            p1-=1
        else:
            nums1[i] = nums2[p2]
            i-=1
            p2-=1
        




print(merge([1,2,3,0,0,0],[2,5,6],3,3))