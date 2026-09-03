class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #helper fn - anagram check, add if anagram
        # result = [] #final contianer
        dict = {} # to store all words with common alphabets
        #efficient storage? with dict
        for ind in range(len(strs)):
            #compute sorted word and then store in dict after checking if key exists
            sorted_str = "".join(sorted(strs[ind]))
            dict.setdefault(sorted_str,[]).append(strs[ind])
        result = [value for value in dict.values()]

        return result


            
        