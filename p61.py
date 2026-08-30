class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)

        # Empty tree
        dp[0] = 1

        # Calculate number of BSTs for each number of nodes
        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root

                dp[nodes] += dp[left] * dp[right]

        return dp[n]