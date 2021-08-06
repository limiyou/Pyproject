#encoding:utf8
"""
下面代码是一个猜数字游戏，请完善代码，实现把用户的游戏猜测过程记录到game.log文件中。
提示：
把所有的print改为使用logging模块记录。
"""
import random

from autoTest.day4.common.mylogger_homework import create_logger

logger=create_logger()
def guess_game():
    """系统从[1,100]区间随机生成一个数，用户有5次猜测机会，系统会根据用户的猜测给出提示：例如,太大了，太小了。"""
    res = random.randint(1, 100)  # 预期答案
    for i in range(5):
        guess = int(input('请输入你猜的数字：'))
        if guess > res:
            #print('你给的答案是%d,太大了,你还剩余"%d"
            # ' % (guess, 4 - i))
            logger.info('你给的答案是%d,太大了,你还剩余"%d"次机会' % (guess, 4 - i))
        elif guess == res:
            print('恭喜中奖!')
            break
        elif guess < res:
            logger.info('你给的答案是%d,太小了,你还剩余"%d"次机会' % (guess, 4 - i))
    logger.info('答案是"%s"，没猜中吧,哈哈哈！' % res)


def main():
    print('系统从[1,100]区间随机生成一个数，用户有5次猜测机会，系统会根据用户的猜测给出提示：例如,太大了，太小了。')
    print('游戏开始！')
    guess_game()


if __name__ == '__main__':
    main()
