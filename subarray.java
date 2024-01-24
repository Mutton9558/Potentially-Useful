// Java Version
public class subarray {
    static int maxSubArray(int[] nums) {
        int sum = 0, maxSum = Integer.MIN_VALUE;

        for (int num : nums) {
            sum = Math.max(sum, 0) + num;
            maxSum = Math.max(maxSum, sum);
        }

        return maxSum;
    }

    public static void main(String[] args) {
        int[] array = {-2,1,-3,8,-3};
        System.out.println(maxSubArray(array));
    }   
}