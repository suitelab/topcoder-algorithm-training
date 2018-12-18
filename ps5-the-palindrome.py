class ThePalindrome:
    def find(self, s):
        i = len(s)
        while True:
            flag = True
            for j in range(len(s)):
                if (i - j - 1) < len(s) and s[j] != s[i - j - 1]:
                    flag = False
                    break
            
            if flag:
                return i
            i += 1


my_class = ThePalindrome()
print(my_class.find('abc'))