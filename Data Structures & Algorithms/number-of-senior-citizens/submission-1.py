class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # count = 0
        # for i in details:
        #     if int(i[11:13]) > 60:
        #         count += 1
        # return count

        res = 0
        for d in details:
            ten = ord(d[11]) - ord("0")
            one = ord(d[12]) - ord("0")
            age = one + 10 * ten
            if age > 60:
                res += 1
        return res