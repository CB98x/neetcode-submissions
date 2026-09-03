class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = ""
        suffix = ""
        for char in strs:
            len_c = len(char)
            prefix += str(len_c)+ ","
            suffix += char
        prefix += "#"
        transmission = prefix + suffix
        print(transmission)
        return transmission
    def decode(self, s: str) -> List[str]:
        prefix_len  = []
        pos_str = 0
        len_char = ""
        for char in s:
            if char == "#":
                break
            pos_str += 1
            if char != ",":
                len_char += char 
            else:
                prefix_len.append(int(len_char))
                len_char = ""
        print(prefix_len)
        actual_str = s[pos_str +1:]
        next_start = 0
        result = []
        for length in prefix_len:
            result.append(actual_str[next_start:next_start+length])
            next_start += length
        print(result)
        return result


