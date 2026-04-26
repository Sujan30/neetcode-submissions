class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.replace(" ", "")
        cleaned = cleaned.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned)
        print(cleaned)
        tail = len(cleaned)-1
        head = 0

        while head <= tail:
            if not cleaned[head] == cleaned[tail]:
                return False
            head += 1
            tail -= 1
        return True
            