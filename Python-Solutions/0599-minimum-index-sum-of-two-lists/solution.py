class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res={}
        for word in range(len(list1)):
            if list1[word] in list2 :
                ind=list2.index(list1[word])
                if (ind+word) not in res:
                    res[word+ind]=[list1[word]]
                else:
                    res[word+ind].append(list1[word])
        '''result=list(set(res.keys()))[0]
        return res[result]'''
        min_sum = min(res.keys())
        return res[min_sum]
