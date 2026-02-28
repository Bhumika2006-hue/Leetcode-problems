class Solution {
public:
int M = 1e9+7;
    int concatenatedBinary(int n) {
        long result = 0;
        int digits = 0;

        for(int num = 1; num <= n; num++) {
            //digit count tabhi barhta hai jab power of 2 ata hai
            if((num & (num-1)) == 0)
                digits++;

            result = ((result << digits)%M + num)%M;
        }

        return result;
    }
};