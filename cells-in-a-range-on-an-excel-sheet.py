from typing import List
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/submissions/1367135020/
class Solution:
    def cellsInRange(s: str) -> List[str]:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        start = s.split(":")[0];
        end = s.split(":")[1];
        
        startnum = int(start[1:]);
        endnum = int(end[1:]);

        startletter = start[0];
        endletter = end[0];

        alphabetsplice = alphabet.split(startletter)[1];
        alphabetsplice = startletter + alphabetsplice;
        alphabetsplice = alphabetsplice.split(endletter)[0];
        alphabetsplice = alphabetsplice + endletter;

        result = []
        for i in alphabetsplice:
            for j in range(startnum, endnum+1):
                result.append(f"{i}{j}");
        return result

s = "K1:L2";
print(Solution.cellsInRange(s));