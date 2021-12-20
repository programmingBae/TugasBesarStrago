class BoyerMoore:
    def __init__(self, pattern):
       self.R = 256;
       self.pattern = pattern
       self.array = [None] * len(pattern)
       for i in range(self.R):
           self.array[i] = 0
       for i in range(len(pattern)):
           self.array[ord(pattern[i])] = i


    def search(self, text):
        m = len(self.pattern)
        n = len(text)
        array_int= []
        skip = 0;
        for i in range (n-m+1,  skip):
            skip = 0
            for j in range(m-1, 0, -1):
                if self.pattern[j] != text[i+j]:
                    skip = max(1, j - self.array[ord(text[i+j])])
                    break
            if skip == 0:
                array_int.append(i)
                skip+=1
        return array_int
        

    