"""导入随机函数相关文件"""
import random


class View(object):
    """游戏试图类"""
    def __init__(self, ratio=0.2, num_of_cols=25, num_of_rows=25):
        self.num_of_cols = num_of_cols
        self.num_of_rows = num_of_rows
        self.round = 0
        self.map = list()
        self.map = [[1 if random.random() < ratio else 0 \
             for j in range(num_of_cols)] for i in range(num_of_rows)]

    def update(self):
        """游戏界面更新"""
        print('update')
        backup = list()
        backup = [[self.map[i][j] for j in range(self.num_of_cols)]\
                  for i in range(self.num_of_rows)]
        for i in range(self.num_of_rows):
            for j in range(self.num_of_cols):
                if self.count_neighbours(i, j, backup) == 3:

                    self.map[i][j] = 1
                elif self.count_neighbours(i, j, backup) != 2:
                    self.map[i][j] = 0

        self.round += 1

    def count_neighbours(self, i, j, backup):
        """判断下一回合是否为活细胞"""
        up = i - 1 if i > 0 else self.num_of_rows - 1
        down = i + 1 if i < self.num_of_rows - 1 else 0
        left = j - 1 if j > 0 else self.num_of_cols - 1
        right = j + 1 if j < self.num_of_cols - 1 else 0
        return backup[i][left] + backup[i][right] + backup[up][j] \
               +backup[down][j] + backup[up][left] \
               +backup[up][right] + backup[down][left] + backup[down][right]
