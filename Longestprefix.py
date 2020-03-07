def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return("")
        elif len(strs)==1:
            return(strs[0])
        else:
            strs.sort()
            output=""
            for i in range(len(strs[0])):
                if strs[0][i]==strs[-1][i]:
                    output += strs[0][i]
                else:
                    break
            return(output)
