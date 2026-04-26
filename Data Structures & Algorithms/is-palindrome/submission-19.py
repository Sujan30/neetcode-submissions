class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = re.sub('[^a-zA-Z0-9]', '', s)
        clean_string = clean_string.strip()
        clean_string = clean_string.lower()
        l = 0
        r = len(clean_string)-1
        
        while l<=r:
            if clean_string[l] != clean_string[r]:
                return False
            else:
                l+=1
                r-=1
        return True

