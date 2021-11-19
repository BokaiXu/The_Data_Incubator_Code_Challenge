import numpy as np
import math as math

class RollDice:
    """docstring for rollDice"""
    def __init__(self, M = 1):
        if M <= 0:
            raise ValueError('M must be a positive interger!')
        self._M = M
        # init the probability map, row index: num of rolls, column: sum of rolls
        self._dp = np.zeros((M + 6, 6), dtype = np.double)

        # init the probability array for dynamic programming
        dp = np.zeros((M + 6, M + 6), dtype = np.double)        
        # update the second row: probability distribution for rolling once
        dp[1, range(1, 7)] = 1.0 / 6.0;
        # update the rest of the probability array: roll twice, thrice, ...
        for i in range(2, dp.shape[0]):
            partial_sum = 0.0
            for j in range(i, dp.shape[1]):
                if j > 7:
                    partial_sum = partial_sum - dp[i - 1, j - 7]
                if j <= M:
                    partial_sum = partial_sum + dp[i - 1, j - 1]
                dp[i, j] = partial_sum / 6.0

        # extract the column M : M + 5, i.e. sum of rolls = M, M + 1, ..., M + 5
        self._dp = dp[:, range(M, M + 6)]

    def get_mean_sumofroll(self):
        pr_sumofroll = np.sum(self._dp, axis = 0)
        sumofroll = np.arange(self._M, self._M + 6, dtype = np.double)
        mean_sumofroll = np.inner(sumofroll, pr_sumofroll)
        print(mean_sumofroll - self._M);

    def get_std_sumofroll(self):
        pr_sumofroll = np.sum(self._dp, axis = 0)
        sumofroll = np.arange(self._M, self._M + 6, dtype = np.double)
        sumofroll_square = np.square(sumofroll)
        mean_sumofroll = np.inner(sumofroll, pr_sumofroll)
        mean_sumofroll_square = np.inner(sumofroll_square, pr_sumofroll)
        std_sumofroll = math.sqrt(mean_sumofroll_square - mean_sumofroll * mean_sumofroll)
        print(std_sumofroll);

    def get_mean_numofroll(self):
        pr_numofroll = np.sum(self._dp, axis = 1)
        numofroll = np.arange(0, self._M + 6, dtype = np.double)
        mean_numofroll = np.inner(numofroll, pr_numofroll)
        print(mean_numofroll)
        
if __name__ == '__main__':
    print('M = 20:')
    A = RollDice(20)
    print('mean of sum of rolls minus M: ', end = '')
    A.get_mean_sumofroll();
    print('std of sum of rolls minus M: ', end = '')
    A.get_std_sumofroll();
    print('mean of num of rolls: ', end = '')
    A.get_mean_numofroll();

    print('\nM = 5000:')
    B = RollDice(5000)
    print('mean of sum of rolls minus M: ', end = '')
    B.get_mean_sumofroll();
    print('std of sum of rolls minus M: ', end = '')
    A.get_std_sumofroll();
    print('mean of num of rolls: ', end = '')
    A.get_mean_numofroll();