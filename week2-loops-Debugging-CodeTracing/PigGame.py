# play pig game
import random
import time

def playPig():
    # input how many players will be playing -> player
    # each player take turns to roll the dice -> dice
    # roll the dice until the play decides to hold -> score
    # if the player rolls a 1, they score nothing and it becomes the next player
    # turn;
    # 

    playerNum = 0
    dice = 0  
    sum = 0
    winner = 0
    maxScore = 0

    playerNum = input("请输入玩家人数：")
    if (input("按回车开始游戏...")):
        time.sleep(0.3)
        print("游戏开始！")
    for player in range(1, int(playerNum) + 1):
        print("")
        time.sleep(0.3)
        print(player,"号玩家回合...")
        time.sleep(0.3)
        sum = 0
        while(True):
            # roll dice
            dice = int(random.uniform(1,6))
            print("摇到了",dice)
            if (dice == 1):
                time.sleep(0.3)
                print("算了吧你，零分！下一个～")
                time.sleep(0.3)
                sum = 0
                print(player,"号玩家总分:", sum)
                break
            else:
                sum += dice
                if(sum >= maxScore):
                    winner = player
                    maxScore = sum
                time.sleep(0.3)
                print("目前您的分数为:", sum, end=" ")
                choice = input("还要继续吗？Y/N：")
                if(choice == 'Y' or choice == 'y'):
                    time.sleep(0.51)
                    continue
                else:
                    time.sleep(0.3)
                    print(player,"号玩家总分:",sum)
                    if(player == playerNum):
                        print("游戏结束！")
                        print(winner,"号玩家总分：",maxScore,"获胜！")
                    break
    for x in range(40):
        print("-",end="")
    print()
    if(maxScore == 0):
        print("没人获胜这局打平了！")
    else:
        print("游戏结束！")
        print(winner,"号玩家获胜！总分",maxScore,"分, 让我们恭喜这个比～")
    return

playPig()