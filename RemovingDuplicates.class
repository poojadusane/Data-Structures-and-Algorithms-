
class Solution {
    public int removeDuplicates(int[] nums) {

        int len = nums.length;
        for (int i = 0; i < len- 1; i++)
        {
            
            if(nums[i] == nums [i+1])
            {
                
                for(int j = i+1; j < len-1 ; j++)
                {
                    nums[j] = nums[j+1];
                    
                }  
                len--; 
                
                i--;
            }
            

        }
        
        for(int i= 0; i< len; i++)
        {
            System.out.println(nums[i]);
        }
        
         return len;
    }
}