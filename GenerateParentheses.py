def createBinaryMatrix (self, startnum, num, str1, arr):
    if str1 == "":
        for i in range(startnum):
            str1 += "_"
    if num == startnum:
        return
    for i in [')', '(']:
        new = list(str1)
        new[num] = str(i)
        str1 = ''.join(new)
        if not "_" in str1 and not (num == 0 and i == 0) and not (num == 1 and i == startnum -1):
            cnt0 = 0
            cnt1 = 0
            removed = False
            for x in new:
                if x == ')':
                    cnt0 += 1
                if x == '(':
                    cnt1 += 1
                if cnt0 > cnt1:
                    removed = True
                    break
            if not removed and cnt0 == cnt1:
                arr.append(str1)
        self.createBinaryMatrix(startnum, num + 1, str1, arr)
    return arr

def generateParenthesis(self, n: int):
    arr = self.createBinaryMatrix(n * 2, 0, "", [])
    return arr