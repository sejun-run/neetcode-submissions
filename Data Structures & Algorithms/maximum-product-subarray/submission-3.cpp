class Solution {
public:
    int nonZero(vector<int> &nums, int s, int e) {
        int res = 1;
        for (int i = s; i <= e; i++) {
            res *= nums[i];
        }
        if (res > 0) {
            return res;
        }
        int l = 1;
        for (int i = s; i <= e; i++) {
            l *= nums[i];
            if (l < 0) {
                break;
            }
        }
        int r = 1;
        for (int i = e; i >= s; i--) {
            r *= nums[i];
            if (r < 0) {
                break;
            }
        }
        int x = max(l, r);
        if (res == x) {
            return res;
        }
        return res / max(l, r);
    }
    int maxProduct(vector<int>& nums) {
        int sz = nums.size();
        int res = -0x7fffffff;
        for (int i = 0; i < sz; i++) {
            res = max(res, nums[i]);
        }
        for (int s = 0; s < sz; s++) {
            if (nums[s] == 0) {
                continue;
            }
            int e = s;
            while (e + 1 < sz && nums[e + 1] != 0) {
                e++;
            }
            res = max(res, nonZero(nums, s, e));
        }

        return res;
    }
};
