class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index1 , index2 = 0 , 0
        while index2 < len(abbr) and index1 < len(word):
        
            if  ord("a") <= ord(abbr[index2]) <= ord("z"):
                if word[index1] != abbr[index2]:
                    return False
                else:
                    index2 = index2 + 1
                    index1 = index1 + 1
            else:
                if abbr[index2] == "0":
                    return False #pretty smart way to deal with leading 0
                num = 0
                while index2 < len(abbr) and abbr[index2].isdigit():
                    num = num * 10 + int(abbr[index2])
                    index2 += 1
                index1 = index1 + num
        return index1 == len(word) and index2 == len(abbr)
                
        