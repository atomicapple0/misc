class Solution:
    def maximalSquare(self, samples) -> int:
        rows = len(samples)
        cols = len(samples[0])
        
        for i in range(rows):
            for j in range(cols):
                samples[i][j] = int(samples[i][j])
        
        for idx in range((rows+cols) // 2):
            # go right, from min(i,cols) to cols
            i = min(idx,rows-1)
            for r in range(min(i,cols), cols):
                if i-1 >= 0 and r-1 >= 0 and samples[i][r] == 1:
                    score = min(samples[i-1][r], samples[i][r-1], samples[i-1][r-1])
                    samples[i][r] = 1 if score == 0 else score + 1
            i = min(idx,cols-1)
            # go down, from min(i+1,rows) to rows
            for d in range(min(i+1,rows), rows):
                if i-1 >= 0 and d-1 >= 0 and samples[d][i] == 1:
                    score = min(samples[d-1][i], samples[d][i-1], samples[d-1][i-1])
                    samples[d][i] = 1 if score == 0 else score + 1
        
        sol = 0
        for i in range(rows):
            for j in range(cols):
                sol = max(sol, samples[i][j])
        return sol * sol

print(Solution().maximalSquare(
    [["0","0","0"],["0","0","0"],["0","0","0"],["0","0","0"]]
    ))