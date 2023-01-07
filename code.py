class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s=set(wordList)
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
        queue=deque([])                     #for fast append and pop more than list
        queue.append([beginWord,0])
        while queue:
            a,b=queue.popleft()            #Get the next node to explore from the top of the queue
            if a==endWord:                 # Goal check (before adding to the queue)
                return b+1                 #steps or depth
# Get the node's children 
# By recreating all possible patterns for that string
            for j in range(len(a)):
                for i in l:
                    if (a[:j]+i+a[j+1:]) in s and (a[:j]+i+a[j+1:])!=beginWord:
                        s.remove(a[:j]+i+a[j+1:])
                        queue.append([a[:j]+i+a[j+1:],b+1])  # Add to the end of the queue
        return 0 #run if retrun 1 it means there is an error while excuting
#The pop() method is used to remove and return the right most element from the queue, and popleft() method is used to remove and return left most element from the queue.
        
