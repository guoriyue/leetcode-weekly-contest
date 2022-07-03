class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        dic={}
        cnt=0
        had=[]
        pre=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in key:
            if (not i==' ') and (not i in had):
                dic[i]=pre[cnt]
                cnt+=1
                had.append(i)
        decoded=""
        for i in message:
            if (not i==' '):
                decoded=decoded+dic[i]
            else:
                decoded=decoded+' '
        return decoded
