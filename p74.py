class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            # Target reached
            if total == target:
                result.append(current.copy())
                return

            # Total exceeded
            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Choose the number
                current.append(num)

                # i is passed again because we can reuse
                # the same number unlimited times
                backtrack(i, current, total + num)

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)

        return result