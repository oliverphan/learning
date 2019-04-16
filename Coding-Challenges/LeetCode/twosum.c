/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *result = malloc(sizeof(int) * 2);
    int i;
    for (i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (target - nums[i] - nums[j] == 0) {
                result[0] = i;
                result[1] = j;
            }   
        }
    }
    return result;
}

// Python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (target - nums[i] - nums[j] == 0):
                    result.append(i)
                    result.append(j)
        return result