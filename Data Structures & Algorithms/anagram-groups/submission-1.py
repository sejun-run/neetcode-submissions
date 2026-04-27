class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags={}
        ret=[]
        for i in range(len(strs)):
            anags[strs[i]]={}
            for c in strs[i]:
                anags[strs[i]][c]=anags[strs[i]].get(c,0) +1
            print(anags[strs[i]])
            flag = 0
            for p in range(len(ret)):
                flag = 1
                if anags[ret[p][0]] == {}:
                    if anags[strs[i]]!= {}:
                        flag=2
                        print(strs[i]+" flag2 for "+ret[p][0])
                for k in anags[ret[p][0]]:
                    if anags[ret[p][0]][k] != anags[strs[i]].get(k,-1):
                        flag=2
                        print(strs[i]+" flag2 for "+ret[p][0])
                        break
                if flag==1:
                    ret[p].append(strs[i])
                    print(strs[i]+" flag1 for "+ret[p][0])
                    break
            if flag !=1 :
                ret.append([strs[i]])
        return ret