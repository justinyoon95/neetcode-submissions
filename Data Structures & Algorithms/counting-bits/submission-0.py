class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []

        for i in range(0, n + 1):
            lst.append(self.hammingWeight(i))

        return lst


    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in str(bin(n)):
            if i == '1':
                count += 1

        return count