class Solution {
     public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> prob=new HashMap<>();
        for (int i=0;i<nums.length;i++) {
            if(prob.containsKey(nums[i])){
                return new int[]{prob.get(nums[i]), i};
            }
            else
                prob.put(target-nums[i],i);
        }
        return null;
    }
}