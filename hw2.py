class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
    
        num = 0
        a = abs(x)
        while(a != 0):
            temp = a % 10
            num = num * 10 +temp
            a = int(a/10)
        if x>0 and num <2147483647:
            return num
        elif x<0 and num <= 2147483647:
            return -num
        else:
            return 0