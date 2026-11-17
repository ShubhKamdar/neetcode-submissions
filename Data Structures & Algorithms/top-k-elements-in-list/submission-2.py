class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = []
        #We are creating a list of lists and adding +1 because our assumption is that for us to access the element appearing 3 times in the array we need to have an index of 3 in the list of lists and since everyhting is indexed at 0 we need to add a +1 to the range so that we have 3 indexes which is basically 4 elements
        for i in range(len(nums) +1):
            bucket.append([])
        #We are now creating the count of the dictionary to assign values to all the unique elements we saw
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        #We will now put these elements in the buckets we created. We have created a list because 2 elements can have the same count.
        for num, count in freq.items():
            bucket[count].append(num)
        #Now we build the solution, we start the loop within the index of possible values, hence we do -1 in length of the bucket since, if we dont do that the index foes out of range for when we do bucket[i]. also we create a new list and then append stuff in that list.
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res





