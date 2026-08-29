from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Stores parents of each word in shortest paths
        parents = defaultdict(list)

        # BFS
        queue = deque([beginWord])
        visited = {beginWord}
        found = False

        while queue and not found:
            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i+1:]

                        if new_word not in wordSet:
                            continue

                        # First time seeing this word
                        if new_word not in visited:
                            if new_word not in level_visited:
                                level_visited.add(new_word)
                                queue.append(new_word)

                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

                        # Another shortest path to the same word
                        elif new_word in level_visited:
                            parents[new_word].append(word)

            visited.update(level_visited)

        if endWord not in parents:
            return []

        # DFS to construct paths
        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result