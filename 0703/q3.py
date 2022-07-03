class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        mod=1000000007
        share=1+delay
        dic={}
        for i in range(1,forget+1):
            dic[i]=0
        dic[1]=1
        date=1
        while date<n:
            new_dic={}
            gen=0
            for i in range(1,forget+1):
                if i>=2:
                    new_dic[i]=dic[i-1]
                if i>=share-1 and i<=forget-1:
                    gen+=dic[i]
                    gen=gen%mod
            new_dic[1]=gen
            dic=new_dic
            date+=1
        final=0
        for i in range(1,forget+1):
            final=final+dic[i]
            final=final%mod
        return final
