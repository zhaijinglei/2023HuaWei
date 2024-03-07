#!/bin/bash
import sys
import numpy as np

def read_util_ok():
    while input() != "OK":
        pass


def finish():
    sys.stdout.write('OK\n')
    sys.stdout.flush()

def read_frame():#读取帧
    result = []
    while 1:
        line = sys.stdin.readline().strip('\n')  # line此时是字符串列表，并已去掉前后空格 回车符
        if line == "OK":
            break
        if line:
            line = list(map(float, line.split(' ')) ) # 把line的空格元素去掉，转成字符串列表list，并转成整型int
        result += line
    k=float(result[2])
    k=int(k)
    num1=0
    num2=0
    num3=0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9=0
    for i in range(len(result)):
        result[i] = float(result[i])

    for i in range(k):
        if result[i * 6 + 3] == 1:
            num1+=1
        if result[i * 6 + 3] == 2:
            num2 += 1
        if result[i * 6 + 3] == 3:
            num3 += 1
        if result[i * 6 + 3] == 4:
            num4+=1
        if result[i * 6 + 3] == 5:
            num5 += 1
        if result[i * 6 + 3] == 6:
            num6 += 1
        if result[i * 6 + 3] == 7:
            num7+=1
        if result[i * 6 + 3] == 8:
            num8 += 1
        if result[i * 6 + 3] == 9:
            num9 += 1
    #工作台位置
    gallery1 = np.zeros((num1,7))
    gallery2 = np.zeros((num2,7))
    gallery3 = np.zeros((num3,7))
    gallery4 = np.zeros((num4, 7))
    gallery5 = np.zeros((num5, 7))
    gallery6 = np.zeros((num6, 7))
    gallery7 = np.zeros((num7, 7))
    gallery8 = np.zeros((num8, 7))
    gallery9 = np.zeros((num9,7))

    num11 = 0
    num22 = 0
    num33 = 0
    num44 = 0
    num55 = 0
    num66 = 0
    num77 = 0
    num88 = 0
    num99 = 0
    ##机器人位置
    robot = np.zeros((4, 5))


    robot[0][0] = 0
    robot[1][0] = 1
    robot[2][0] = 2
    robot[3][0] = 3

    robot[0][1] = result[6*k+11]#x坐标
    robot[0][2] = result[6*k+12]#y坐标
    robot[0][3] = result[6 * k + 10]#朝向
    robot[0][4] = result[6 * k + 4]#携带物品类型

    robot[1][1] = result[6 * k + 21]
    robot[1][2] = result[6 * k + 22]
    robot[1][3] = result[6 * k + 20]
    robot[1][4] = result[6 * k + 14]

    robot[2][1] = result[6 * k + 31]
    robot[2][2] = result[6 * k + 32]
    robot[2][3] = result[6 * k + 30]
    robot[2][4] = result[6 * k + 24]

    robot[3][1] = result[6 * k + 41]
    robot[3][2] = result[6 * k + 42]
    robot[3][3] = result[6 * k + 40]
    robot[3][4] = result[6 * k + 34]

    for i in range(k):
        if result[i * 6 + 3] == 1 and num1>0:
            gallery1[num11][0]=i#工作台ID
            gallery1[num11][1] = float(result[i*6+4])#x
            gallery1[num11][2] = float(result[i*6+5])#y
            gallery1[num11][3] = float(result[i * 6 + 8])  # 产品状态
            gallery1[num11][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery1[num11][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery1[num11][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num11+=1
        if result[i * 6 + 3] == 2 and num2>0:
            gallery2[num22][0] = i  # 工作台ID
            gallery2[num22][1] = float(result[i*6+4])  # x
            gallery2[num22][2] = float(result[i*6+5]) # y
            gallery2[num22][3] = float(result[i*6+8])#产品状态
            gallery2[num22][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery2[num22][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery2[num22][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num22 += 1
        if result[i * 6 + 3] == 3 and num3>0:
            gallery3[num33][0] = i  # 工作台ID
            gallery3[num33][1] = float(result[i*6+4])  # x
            gallery3[num33][2] = float(result[i*6+5])  # y
            gallery3[num33][3] = float(result[i * 6 + 8])  # 产品状态
            gallery3[num33][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery3[num33][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery3[num33][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num33 += 1
        if result[i * 6 + 3] == 4 and num4>0:
            gallery4[num44][0]=i#工作台ID
            gallery4[num44][1] = float(result[i*6+4])#x
            gallery4[num44][2] = float(result[i*6+5])#y
            gallery4[num44][3] = float(result[i * 6 + 8])  # 产品状态
            gallery4[num44][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery4[num44][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery4[num44][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num44+=1
        if result[i * 6 + 3] == 5 and num5>0:
            gallery5[num55][0] = i  # 工作台ID
            gallery5[num55][1] = float(result[i*6+4])  # x
            gallery5[num55][2] = float(result[i*6+5]) # y
            gallery5[num55][3] = float(result[i*6+8])#产品状态
            gallery5[num55][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery5[num55][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery5[num55][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num55 += 1
        if result[i * 6 + 3] == 6 and num6>0:
            gallery6[num66][0] = i  # 工作台ID
            gallery6[num66][1] = float(result[i*6+4])  # x
            gallery6[num66][2] = float(result[i*6+5])  # y
            gallery6[num66][3] = float(result[i * 6 + 8])  # 产品状态
            gallery6[num66][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery6[num66][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery6[num66][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num66 += 1
        if result[i * 6 + 3] == 7 and num7>0:
            gallery7[num77][0]=i#工作台ID
            gallery7[num77][1] = float(result[i*6+4])#x
            gallery7[num77][2] = float(result[i*6+5])#y
            gallery7[num77][3] = float(result[i * 6 + 8])  # 产品状态
            gallery7[num77][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery7[num77][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery7[num77][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num77+=1
        if result[i * 6 + 3] == 8 and num8>0:
            gallery8[num88][0] = i  # 工作台ID
            gallery8[num88][1] = float(result[i*6+4])  # x
            gallery8[num88][2] = float(result[i*6+5]) # y
            gallery8[num88][3] = float(result[i*6+8])#产品状态
            gallery8[num88][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery8[num88][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery8[num88][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num88 += 1
        if result[i * 6 + 3] == 9 and num9>0:
            gallery9[num99][0] = i  # 工作台ID
            gallery9[num99][1] = float(result[i*6+4])  # x
            gallery9[num99][2] = float(result[i*6+5])  # y
            gallery9[num99][3] = float(result[i * 6 + 8])  # 产品状态
            gallery9[num99][4] = float(result[i * 6 + 7])  # 原材料状态
            gallery9[num99][5] = float(result[i * 6 + 3])  # 工作台类型
            gallery9[num99][6] = float(result[i * 6 + 6])  # 剩余生产时间
            num99 += 1
    frame_id=int(result[0])
    return gallery1,gallery2,gallery3,gallery4,gallery5,gallery6,gallery7,gallery8,gallery9,robot,frame_id


def distance(a, b):
    d = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return d


def judge(buy_gallery,sell_gallery,robot,process):#工作台和机器人是1*4矩阵，计算工作进程
    x_buy = buy_gallery[1]
    y_buy = buy_gallery[2]
    x_sell = sell_gallery[1]
    y_sell = sell_gallery[2]
    x_rb = robot[1]
    y_rb = robot[2]
    p=process
    buy_distance=((y_buy-y_rb)**2+(x_buy-x_rb)**2)**0.5
    if buy_distance<0.4:
        p = 1
    sell_distance = ((y_sell-y_rb)**2+(x_sell-x_rb)**2)**0.5
    if sell_distance < 0.4:
        p = 0
    return p

def jud_right(robot_x, robot_y,angle_intial,angle_other):#转角避障
    flag_angle=0
    if (0.785 <= angle_intial <= 2.355) and (-2.355 <= angle_other <= -0.785) :  # 此时其为上下行驶
        if robot_x[0]<=robot_x[1]:
            flag_angle=1
        else :
            flag_angle = -1
    if (-2.355 <= angle_intial <= -0.785) and  (0.785 <= angle_other <= 2.355):
        if robot_x[0]<=robot_x[1]:
            flag_angle=-1
        else :
            flag_angle = 1
    if ((2.355 < angle_intial) or (angle_intial < -2.355)) and((0.785 > angle_other>0) or ( 0>=angle_other > -0.785)):
        if robot_y[0] <= robot_y[1]:
            flag_angle = -1
        else :
            flag_angle = 1
    if ((0.785 > angle_intial>0) or ( 0>=angle_intial > -0.785)) and((2.355 < angle_other) or (angle_other < -2.355)):
        if robot_y[0] <= robot_y[1]:
            flag_angle = -1
        else :
            flag_angle = 1
    return flag_angle

def LOS(x1,x2,y1,y2):
    if (y1 >= y2 and x1 > x2) or (y1 < y2 and x1 > x2):
        angle_target = np.arctan((y1-y2)/(x1-x2))
    elif y1 >= y2 and x1 < x2:
        angle_target = np.arctan((y1 - y2) / (x1 - x2)) + 3.1415926
    elif y1 < y2 and x1 < x2:
        angle_target = np.arctan((y1 - y2) / (x1 - x2)) - 3.1415926
    elif y1 >= y2 and x1 == x2:
        angle_target = 3.1415926/2
    elif y1 < y2 and x1 == x2:
        angle_target = -3.1415926/2
    return angle_target
def move3(gallery1,robot1,djm,dis_sell,process):#不避障程序

    y1 = gallery1[2]
    x1 = gallery1[1]
    y2 = robot1[2]
    x2 = robot1[1]

    robot_flag = robot1[4]
    gallery_flag = gallery1[3]
    robot_ID = robot1[0]
    angle_intial = robot1[3]
    dis_target = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    angle_target = LOS(x1, x2, y1, y2)

    if 3.14>=angle_target>=(3*3.14/4) or -3*3.14/4>=angle_target>=-3.14:
        if angle_target<0:
            angle_target=(3.14*2+angle_target)
        if angle_intial<0:
            angle_intial=(3.14*2+angle_intial)

        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 10):
                line_speed = 6

            else:line_speed=0
        else:
            angle_derta = 0
            line_speed = 2
        angle_speed = 50 * angle_derta

    else:
        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 5):
                line_speed = 6

            else:
                line_speed = 1.5
        else:
            angle_derta = 0
            line_speed = 2

        angle_speed = 10 * angle_derta

    return angle_speed,line_speed,robot_ID,dis_target,gallery_flag,robot_flag
def move(gallery1,robot1,djm,dis_sell,process):#不避障程序

    y1 = gallery1[2]
    x1 = gallery1[1]
    y2 = robot1[2]
    x2 = robot1[1]

    robot_flag = robot1[4]
    gallery_flag = gallery1[3]
    robot_ID = robot1[0]
    angle_intial = robot1[3]
    dis_target = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    angle_target = LOS(x1, x2, y1, y2)

    if 3.14 >= angle_target >= (3 * 3.14 / 4) or -3 * 3.14 / 4 >= angle_target >= -3.14:
        if angle_target < 0:
            angle_target = (3.14 * 2 + angle_target)
        if angle_intial < 0:
            angle_intial = (3.14 * 2 + angle_intial)

        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 5):
                line_speed = 6

            else:
                line_speed = 0
        else:
            angle_derta = 0
            line_speed = 2

        angle_speed = 50 * angle_derta
    else:
        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 5):
                line_speed = 6

            else:
                line_speed = 2.5
        else:
            angle_derta = 0
            line_speed = 4

        angle_speed = 30 * angle_derta


    # if dis_sell[int(robot_ID)] < 1.5 and process[int(robot_ID)] == 0 :
    #     #if dis_target > 0.5:
    #     #     angle_derta = angle_target - angle_intial
    #     # else:
    #     #     angle_derta = 0
    #     if robot_ID == 0 or robot_ID == 1:
    #         angle_speed = 30 * angle_derta * -1
    #         line_speed = robot_ID + 2
    #     if robot_ID == 2 or robot_ID == 3:
    #         angle_speed = 30 * angle_derta
    #         line_speed = robot_ID + 3
    #

    return angle_speed,line_speed,robot_ID,dis_target,gallery_flag,robot_flag

def cal_dis(robot,sell_gallery):
    djm=np.ones((4,4))#12 13 14 23 24 34
    dis_sell=[0,0,0,0]
    x_sell = sell_gallery[1]
    y_sell = sell_gallery[2]
    x=[0,0,0,0]
    y = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            dis=((robot[i][1]-robot[j][1])**2+(robot[i][2]-robot[j][2])**2)**0.5
            djm[i][j]=dis

    for i in range(4):
        x[i]=robot[i][1]
        y[i]=robot[i][2]
        sell_distance = ((y_sell -y[i]) ** 2 + (x_sell - x[i]) ** 2) ** 0.5
        dis_sell[i]=sell_distance

    return djm,dis_sell

def cal_dis4(robot,buy_gallery,sell_gallery):
    djm=np.ones((4,4))#12 13 14 23 24 34
    dis_sell=[0,0,0,0]
    dis_buy = [0, 0, 0, 0]
    x_sell = sell_gallery[1]
    y_sell = sell_gallery[2]

    x_buy = buy_gallery[1]
    y_buy = buy_gallery[2]

    x=[0,0,0,0]
    y = [0, 0, 0, 0]
    angle=[0,0,0,0]
    for i in range(4):
        for j in range(4):
            dis=((robot[i][1]-robot[j][1])**2+(robot[i][2]-robot[j][2])**2)**0.5
            djm[i][j]=dis

    for i in range(4):
        x[i]=robot[i][1]
        y[i]=robot[i][2]
        angle[i]=robot[i][3]
        dis_sell[i] = ((y_sell -y[i]) ** 2 + (x_sell - x[i]) ** 2) ** 0.5
        dis_buy[i] = ((y_buy - y[i]) ** 2 + (x_buy - x[i]) ** 2) ** 0.5


    return djm,dis_sell,dis_buy,x,y,angle

def move1(gallery1,robot1,djm,dis_sell,process,x,y,angle,robot):
    robot_x = [0, 0]
    robot_y = [0, 0]
    flaga=0
    flag=0#刹车判断符

    #np.savetxt('1.txt',process)
    angle_speed=0

    y1 = gallery1[2]
    x1 = gallery1[1]
    y2 = robot1[2]
    x2 = robot1[1]
    if robot1[4] == 7 and abs(y2-46.25)<0.5:
        x1,y1 = [30.75, 46.25]
        diss = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if diss<2 :
            y1 = gallery1[2]
            x1 = gallery1[1]
    if robot1[4] == 4 and abs(x2-18.75)>2 and abs(y2-1.25)<2:
        x1,y1 = [18.75, 1.25]
        diss = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if diss<2 :
            x1 = gallery1[1]
    if robot1[4] == 5 and abs(x2-30.75)>2 and abs(y2-21.25)<2 and x1==24.75:
        x1,y1 = [30.75, 21.25]
        diss = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if diss<2 :
            y1 = gallery1[2]
            x1 = gallery1[1]
    if robot1[4] == 6 and abs(x2-18.75)>2 and abs(y2-26.25)<2 and x1==24.75:
        x1,y1 = [18.75, 26.25]
        diss = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if diss<2 :
            x1 = gallery1[1]
    line_speed = 1.5
    robot_flag = robot1[4]
    gallery_flag = gallery1[3]
    robot_ID = robot1[0]
    angle_intial = robot1[3]
    dis_target = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    angle_target = LOS(x1, x2, y1, y2)
    xiabiao=[5,5,5,5]
    for i in range(4):
        if dis_sell[i]<3:
            xiabiao[i]=i
    mm=min(xiabiao)
    if robot_ID == 0:
        if djm[0][1]<5 or  djm[0][2]<5 or  djm[0][3]<5:
            flag=1
        if process[1] + process[0]>=1:
            robot_x[0] = x[0]  # 主控制车辆的x坐标
            robot_x[1] = x[1]
            robot_y[0] = y[0]  # 主控制车辆的y坐标
            robot_y[1] = y[1]
            flag_angle=jud_right(robot_x, robot_y,angle_intial,angle[1])
            if djm[0][1] <2:
                flaga = djm[0][1]
        if process[2] + process[0]>=1:
            robot_x[0] = x[0]  # 主控制车辆的x坐标
            robot_x[1] = x[2]
            robot_y[0] = y[0]  # 主控制车辆的y坐标
            robot_y[1] = y[2]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[2])
            if djm[0][2] <2:
                flaga =djm[0][2]
        if process[3] + process[0]>=1:
            robot_x[0] = x[0]  # 主控制车辆的x坐标
            robot_x[1] = x[3]
            robot_y[0] = y[0]  # 主控制车辆的y坐标
            robot_y[1] = y[3]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[3])
            if djm[0][3] <2:
                flaga = djm[0][3]
    if robot_ID == 1:
        if  djm[1][3]<2 or djm[1][2]<2:
            flag=1
        if process[0]+process[1]>=1:
            robot_x[0] = x[1]  # 主控制车辆的x坐标
            robot_x[1] = x[0]
            robot_y[0] = y[1]  # 主控制车辆的y坐标
            robot_y[1] = y[0]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[0])
            if   djm[1][0]<2:
                flaga=djm[1][0]
        if process[2] + process[1]>=1:
            robot_x[0] = x[1]  # 主控制车辆的x坐标
            robot_x[1] = x[2]
            robot_y[0] = y[1]  # 主控制车辆的y坐标
            robot_y[1] = y[2]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[2])
            if   djm[1][2]<2:
                flaga= djm[1][2]
        if process[3] + process[1]>=1:
            robot_x[0] = x[1]  # 主控制车辆的x坐标
            robot_x[1] = x[3]
            robot_y[0] = y[1]  # 主控制车辆的y坐标
            robot_y[1] = y[3]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[3])
            if   djm[1][3]<2:
                flaga=djm[1][3]
    if robot_ID == 2:

        if djm[2][3]<2:
            flag=1
        if process[0] + process[2]>=1:
            robot_x[0] = x[2]  # 主控制车辆的x坐标
            robot_x[1] = x[0]
            robot_y[0] = y[2]  # 主控制车辆的y坐标
            robot_y[1] = y[0]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[0])
            if djm[2][0] <2:
                flaga = djm[2][0]
        if process[1] + process[2]>=1:
            robot_x[0] = x[2]  # 主控制车辆的x坐标
            robot_x[1] = x[1]
            robot_y[0] = y[2]  # 主控制车辆的y坐标
            robot_y[1] = y[1]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[1])
            if djm[2][1] <2:
                flaga = djm[2][1]
        if process[3] + process[2]>=1:
            robot_x[0] = x[2]  # 主控制车辆的x坐标
            robot_x[1] = x[3]
            robot_y[0] = y[2]  # 主控制车辆的y坐标
            robot_y[1] = y[3]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[3])
            if djm[2][3] <2:
                flaga = djm[2][3]

    if robot_ID == 3:
        if process[0] + process[3]>=1:
            robot_x[0] = x[3]  # 主控制车辆的x坐标
            robot_x[1] = x[0]
            robot_y[0] = y[3]  # 主控制车辆的y坐标
            robot_y[1] = y[0]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[0])
            if djm[3][0] <2:
                flaga = djm[3][0]
        if process[1] + process[3]>=1:
            robot_x[0] = x[3]  # 主控制车辆的x坐标
            robot_x[1] = x[1]
            robot_y[0] = y[3]  # 主控制车辆的y坐标
            robot_y[1] = y[1]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[1])
            if djm[3][1] <2:
                flaga = djm[3][1]
        if process[2] + process[3]>=1:
            robot_x[0] = x[3]  # 主控制车辆的x坐标
            robot_x[1] = x[2]
            robot_y[0] = y[3]  # 主控制车辆的y坐标
            robot_y[1] = y[2]
            flag_angle = jud_right(robot_x, robot_y, angle_intial,angle[2])
            if djm[3][2] <2:
                flaga = djm[3][2]

    if 3.14 >= angle_target >= (3 * 3.14 / 4) or -3 * 3.14 / 4 >= angle_target >= -3.14:
        if angle_target < 0:
            angle_target = (3.14 * 2 + angle_target)
        if angle_intial < 0:
            angle_intial = (3.14 * 2 + angle_intial)

        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 5):
                line_speed = 6

            else:
                line_speed = 0
        else:
            angle_derta = 0
            line_speed = 2

        angle_speed = 50 * angle_derta
    else:
        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 5):
                line_speed = 6

            else:
                line_speed = 2.5
        else:
            angle_derta = 0
            line_speed = 4

        angle_speed = 30 * angle_derta
    # if flag > 0:
    #
    #
    #     angle_mid, line_speed = apf(robot, robot1)
    #     angle_speed = 1.5*(angle_mid - angle_intial)



    # if dis_sell[int(robot_ID)] < 1.5 and process[int(robot_ID)] == 0 :
    #     #if dis_target > 0.5:
    #     #     angle_derta = angle_target - angle_intial
    #     # else:
    #     #     angle_derta = 0
    #     if robot_ID == 0 or robot_ID == 1:
    #         angle_speed = 30 * angle_derta * -1
    #         line_speed = robot_ID + 2
    #     if robot_ID == 2 or robot_ID == 3:
    #         angle_speed = 30 * angle_derta
    #         line_speed = robot_ID + 3
    #
    # if dis_buy[int(robot_ID)] < 2 and process[int(robot_ID)] == 1 :
    #     # if dis_target > 0.5:
    #     #     angle_derta = angle_target - angle_intial
    #     # else:
    #     #     angle_derta = 0
    #     if robot_ID==0 or robot_ID==1:
    #         angle_speed = 30 * angle_derta*-1
    #         line_speed = robot_ID+4
    #     if robot_ID==2 or robot_ID==3:
    #         angle_speed = 30 * angle_derta
    #         line_speed = robot_ID+3


    return angle_speed,line_speed,robot_ID,dis_target,gallery_flag,robot_flag
def apf(robot,main_robot):
    P0 = np.array([main_robot[1], main_robot[2], 6*np.cos(main_robot[3]), 6*np.sin(main_robot[3])])  # 车辆起点位置，分别代表x,y,vx,vy
    Pobs = np.zeros((3, 4))
    mm=0
    # 障碍物位置
    for i in range(4):
        if robot[i][0]!=main_robot[0]:
            Pobs[mm][0]=robot[i][1]
            Pobs[mm][1] = robot[i][2]
            mm+=1
    Eta_rep_ob = 15  # 斥力的增益系数
    d0 = 2  # 障碍影响的最大距离
    num = Pobs.shape[0]  # 障碍与目标总计个数
    n = 1
    delta = np.zeros((num, 2))  # 保存车辆当前位置与障碍物的方向向量，方向指向车辆；以及保存车辆当前位置与目标点的方向向量，方向指向目标点
    unite_vec = np.zeros((num, 2))  # 保存车辆当前位置与障碍物的单位方向向量，方向指向车辆；以及保存车辆当前位置与目标点的单位方向向量，方向指向目标点
    F_rep_ob = np.zeros((3, 2))  # 存储每一个障碍到车辆的斥力,带方向
    v = 6 # 设车辆速度为常值
    ## ***************初始化结束，开始主体循环******************
    Pi = P0[0:2]  # 当前车辆位置
    dists = []
    # 计算车辆当前位置与障碍物的单位方向向量
    for j in range(len(Pobs)):
        delta[j] = Pi[0:2] - Pobs[j, 0:2]
        dists.append(np.linalg.norm(delta[j]))
        unite_vec[j] = delta[j] / dists[j]
    ## 计算斥力
    # 在原斥力势场函数增加目标调节因子（即车辆至目标距离），以使车辆到达目标点后斥力也为0
    for j in range(3):
        if dists[j] >= d0:
            F_rep_ob[j][0] = 0
            F_rep_ob[j][1] = 0
        else:
            # 障碍物的斥力1，方向由障碍物指向车辆
            F_rep_ob_abs = Eta_rep_ob * (1 / dists[j] - 1 / d0) * (dists[len(Pobs)-1]) ** n / dists[j] ** 2  # 斥力大小
            F_rep_ob_angle = F_rep_ob_abs * unite_vec[j]  # 斥力向量
            F_rep_ob[j][0] = F_rep_ob_abs
            angle=LOS(0, F_rep_ob_angle[0], 0, F_rep_ob_angle[1])
            F_rep_ob[j][1] = angle
    fx=[0,0,0]
    fy = [0, 0, 0]
    for i in range(3):
        fx[i]= F_rep_ob[i][0]*np.cos(F_rep_ob[i][1])
        fy[i] = F_rep_ob[i][0] * np.sin(F_rep_ob[i][1])
    FFX = np.sum(fx)
    FFY = np.sum(fy)

    F_angle=LOS(0, FFX, 0,FFY)
    F=FFX/np.cos(F_angle)

    angle_speed=(F_angle)*1
    line_speed=4

    return angle_speed,line_speed

def get_bit_val(byte, index):
    """
    得到某个字节中某一位（Bit）的值

    :param byte: 待取值的字节值
    :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :returns: 返回读取该位的值，0或1
    """
    if ((byte) & (1 << (index))):
        return 1
    else:
        return 0



def move2(gallery1,robot1,djm,dis_sell,process,b):

    flag=0#刹车判断符
    angle_speed=0

    y1 = gallery1[2]
    x1 = gallery1[1]
    y2 = robot1[2]
    x2 = robot1[1]

    line_speed = 1.5
    robot_flag = robot1[4]
    gallery_flag = gallery1[3]
    robot_ID = robot1[0]
    angle_intial = robot1[3]
    dis_target = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    angle_target = LOS(x1, x2, y1, y2)
    #
    if robot_ID == 0:
        if djm[0][1]<2 or  djm[0][2]<2 or  djm[0][3]<2:
            flag=1
    if robot_ID == 1:
        if  djm[1][3]<2 or djm[1][2]<2:
            flag=1
    if robot_ID == 2:

        if djm[2][3]<2:
            flag=1

    # if flag==0:
    # if dis_target < 1.2:
    #     line_speed = 2
    if 3.14>=angle_target>=(3*3.14/4) or -3*3.14/4>=angle_target>=-3.14:
        if angle_target<0:
            angle_target=(3.14*2+angle_target)
        if angle_intial<0:
            angle_intial=(3.14*2+angle_intial)

        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 10):
                line_speed = 6

            else:line_speed=0
        else:
            angle_derta = 0
            line_speed = 2
            # if abs(angle_derta) > (3.14 / 10):
            #     line_speed = 0

        angle_speed = 50 * angle_derta

    else:
        if dis_target > 1:
            angle_derta = -angle_intial + (angle_target)
            if abs(angle_derta) < (3.14 / 5):
                line_speed = 6

            else:
                line_speed = 1.5
        else:
            angle_derta = 0
            line_speed = 2
            # if abs(angle_derta) > (3.14 / 10):
            #     line_speed = 0

        angle_speed = 10 * angle_derta
        #angle_speed = 3 * angle_derta

    if flag>0 and b==0:

        # angle_speed += angle_turn[i] /2
        #line_speed =1
        main_robot=robot1
        angle_speed,line_speed=apf1(robot, main_robot)

    # if dis_sell[int(robot_ID)] < 5 and process[int(robot_ID)] == 0:
    #     if dis_target > 0.5:
    #         angle_derta = angle_target - angle_intial
    #     else:
    #         angle_derta = 0
    #     angle_speed = 30 * angle_derta
    #     line_speed = 6

    return angle_speed,line_speed,robot_ID,dis_target,gallery_flag,robot_flag
def apf1(robot,main_robot):


    P0 = np.array([main_robot[1], main_robot[2], 6*np.cos(main_robot[3]), 6*np.sin(main_robot[3])])  # 车辆起点位置，分别代表x,y,vx,vy
    Pobs = np.zeros((3, 4))
    mm=0
    # 障碍物位置
    for i in range(4):
        if robot[i][0]!=main_robot[0]:
            Pobs[mm][0]=robot[i][1]
            Pobs[mm][1] = robot[i][2]
            mm+=1


    Eta_rep_ob = 15  # 斥力的增益系数
    d0 = 2  # 障碍影响的最大距离
    num = Pobs.shape[0]  # 障碍与目标总计个数
    n = 1
    delta = np.zeros((num, 2))  # 保存车辆当前位置与障碍物的方向向量，方向指向车辆；以及保存车辆当前位置与目标点的方向向量，方向指向目标点
    unite_vec = np.zeros((num, 2))  # 保存车辆当前位置与障碍物的单位方向向量，方向指向车辆；以及保存车辆当前位置与目标点的单位方向向量，方向指向目标点
    F_rep_ob = np.zeros((3, 2))  # 存储每一个障碍到车辆的斥力,带方向

    v = 6 # 设车辆速度为常值
    ## ***************初始化结束，开始主体循环******************
    Pi = P0[0:2]  # 当前车辆位置

    dists = []
    # 计算车辆当前位置与障碍物的单位方向向量
    for j in range(len(Pobs)):
        delta[j] = Pi[0:2] - Pobs[j, 0:2]
        dists.append(np.linalg.norm(delta[j]))
        unite_vec[j] = delta[j] / dists[j]

    ## 计算斥力
    # 在原斥力势场函数增加目标调节因子（即车辆至目标距离），以使车辆到达目标点后斥力也为0
    for j in range(3):
        if dists[j] >= d0:
            F_rep_ob[j][0] = 0
            F_rep_ob[j][1] = 0

        else:
            # 障碍物的斥力1，方向由障碍物指向车辆
            F_rep_ob_abs = Eta_rep_ob * (1 / dists[j] - 1 / d0) * (dists[len(Pobs)-1]) ** n / dists[j] ** 2  # 斥力大小
            F_rep_ob_angle = F_rep_ob_abs * unite_vec[j]  # 斥力向量
            F_rep_ob[j][0] = F_rep_ob_abs
            angle=LOS(0, F_rep_ob_angle[0], 0, F_rep_ob_angle[1])
            F_rep_ob[j][1] = angle
    fx=[0,0,0]
    fy = [0, 0, 0]
    for i in range(3):
        fx[i]= F_rep_ob[i][0]*np.cos(F_rep_ob[i][1])
        fy[i] = F_rep_ob[i][0] * np.sin(F_rep_ob[i][1])
    FFX=np.sum(fx)
    FFY = np.sum(fy)

    F_angle=LOS(0, FFX, 0,FFY)
    F=FFX/np.cos(F_angle)

    angle_speed=(F_angle)*2
    line_speed=F

    return angle_speed,line_speed



if __name__ == '__main__':
    ##初始化，计算使用哪几个工作台
    read_util_ok()
    process = np.zeros((1,4))  # 进程判定符，初始化为0，购买进程，则为0，到了售卖进程，则为1
    derta_distance_sell=10000
    derta_distance_buy=10000
    flag_sell=1
    flag_buy=0
    finish()
    woids=np.zeros((4, 4))#每行代表一个机器人，四列分别代表有无任务、购买工作台、售出工作台、售出工作台原材料类型
    for ii in woids:
        ii[1]=-1
        ii[2] = -1
        ii[3] = -1
    mm=0
    nn=0
    mn=0
    derprice=[4580,4780,4980,19133,19833,22333,29000]#差价矩阵
    weight=50#评价指标中的距离权值
    offset456=1500#123为456送货给的正增益
    offset5 = 1500
    offset4 = 1500# 123为456送货给的正增益
    offset7=7000#456为7送货给的正增益
    mapid=-1
    b=0
    while True:

        gallery1, gallery2, gallery3,gallery4, gallery5, gallery6, gallery7, gallery8, gallery9, robot,frame_id = read_frame()
        if len(gallery7) > 7:
            if frame_id > 8700:
                gallery7[6][3] = 1
        gallery=np.concatenate((gallery1,gallery2,gallery3,gallery4,gallery5,gallery6,gallery7,gallery8,gallery9),axis=0)
        if len(gallery7)>7 :#map 1

            if len(gallery7)==0:
                offset9 = 0  # 123456为9送货给的负增益
            else:
                offset9 = -15000

            noflag4 = 0
            noflag5 = 0
            noflag6 = 0
            for gal in gallery7:
                if(get_bit_val(int(gal[4]),4)==0):#如果缺少456那么就给送的增益增加
                    noflag4 = 1
                if (get_bit_val(int(gal[4]), 5) == 0):
                    noflag5 = 1
                if (get_bit_val(int(gal[4]), 6) == 0):
                    noflag6 = 1

            # if(frame_id==1):#生成距离矩阵
            #np.savetxt('2.txt', gallery)
            # wgallery = [gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0]]
            sys.stdout.write('%d\n' % frame_id)
            mn=frame_id
            # bianli=[3,2,1,0]
            #np.savetxt('1.txt', gallery7)
            if 7000>frame_id>6500:
                b=1
            if 7800>frame_id>7700:
                derprice=[4580,4780,4980,19133,19833,22333,0]#差价矩阵
            if frame_id>7800:
                derprice = [4580, 4780, 4980, 19133, 19833, 22333, 29000]  # 差价矩阵
            for i in range(4):
                if robot[i][0] == 0:
                    offset5 = 2500
                else:
                    offset5 = 1500
                if robot[i][0] == 1:
                    offset4 = 2500
                else:
                    offset4 = 1500
                # woids = [x[5] for x in robot]#所有机器人的任务工作台
                #np.savetxt('1.txt', woids)
                if(woids[i][0]==0 and robot[i][4]==0):
                    task = np.zeros((1,4))#临时存储一个任务的信息

                    alltask=np.zeros((1,4))#存储所有候选任务信息
                    nn=nn+1
                    for gal in gallery:#遍历所有工作台
                        if((gal[3]==1 or frame_id<=50) and gal[5]==1):#根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery4:
                                if(get_bit_val(int(galsell[4]),1)==0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 1):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]),2)==1) :
                                            offset=offset+offset4
                                        if noflag4 == 1:
                                            offset = offset + offset4
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 1
                                        task[0][3] = derprice[1-1]+offset-weight*(distance(robot[i][1:3],gal[1:3])+distance(gal[1:3],galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery5:
                                if(get_bit_val(int(galsell[4]),1)==0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 1):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]),3)==1):
                                            offset = offset + offset5
                                        if noflag5 == 1:
                                            offset = offset + offset5

                                        task[0][0]=gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 1
                                        task[0][3] = derprice[1-1]+offset-weight*(distance(robot[i][1:3],gal[1:3])+distance(gal[1:3],galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0]=gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 1
                                    task[0][3] = derprice[1-1]+offset9-weight*(distance(robot[i][1:3],gal[1:3])+distance(gal[1:3],galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                        if ((gal[3]==1 or frame_id<=50) and gal[5] == 2):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery4:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]),1)==1):
                                            offset = offset + offset4
                                        if noflag4 == 1:
                                            offset = offset + offset4

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]),3)==1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 2
                                    task[0][3] = derprice[2 - 1]+offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                        if ((gal[3]==1 or frame_id<=50) and gal[5] == 3):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery5:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]),1)==1):
                                            offset = offset + offset5
                                        if noflag5 == 1:
                                            offset = offset + offset5


                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]),2)==1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 3
                                    task[0][3] = derprice[3 - 1]+offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                        if (gal[3]==1 and gal[5] == 4):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:

                                if (get_bit_val(int(galsell[4]), 4) == 0):
                                    mm = frame_id
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 4):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]),5)==1) and (get_bit_val(int(galsell[4]),6)==1):
                                            offset=offset7
                                        elif (get_bit_val(int(galsell[4]),5)==1) or (get_bit_val(int(galsell[4]),6)==1):
                                            offset = offset7/2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 4
                                        task[0][3] = derprice[4 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 4
                                    task[0][3] = derprice[4 - 1]+offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                        if (gal[3]==1 and gal[5] == 5):  # 根据工作台类型判断哪个工作台缺少这一产品
                            if 7900>frame_id>7700:
                                gallery7[6][3]=0
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 5) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 5):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]),4)==1) and (get_bit_val(int(galsell[4]),6)==1):
                                            offset=offset7
                                        elif (get_bit_val(int(galsell[4]),4)==1) or (get_bit_val(int(galsell[4]),6)==1):
                                            offset = offset7/2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 5
                                        task[0][3] = derprice[5 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 5
                                    task[0][3] = derprice[5 - 1]+offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                        if (gal[3]==1 and gal[5] == 6):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 6) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 6):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]),5)==1) and (get_bit_val(int(galsell[4]),4)==1):
                                            offset=offset7
                                        elif (get_bit_val(int(galsell[4]),5)==1) or (get_bit_val(int(galsell[4]),4)==1):
                                            offset = offset7/2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 6
                                        task[0][3] = derprice[6 - 1]+offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 6
                                    task[0][3] = derprice[6 - 1]+offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)

                        if (gal[3]==1 and gal[5] == 7):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery8:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                    alltask=np.concatenate((alltask,task),axis=0)
                    if(len(alltask)>1):
                        alltask_new=np.delete(alltask, 0, axis=0)
                        #np.savetxt('4.txt', alltask_new)
                        indicator = alltask_new[:,3]#筛选出评价指标那一列进行排序
                        maxindic=np.argmax(indicator)
                        woids[i][0] = 1
                        woids[i][1] = alltask_new[maxindic][0]
                        woids[i][2] = alltask_new[maxindic][1]
                        woids[i][3] = alltask_new[maxindic][2]

                for id in gallery1:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery2:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery3:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery4:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery5:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery6:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery7:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery8:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break
                for id in gallery9:
                    if id[0]==woids[i][1]:
                        buy_gallery=id
                        break
                    if id[0]==woids[i][2]:
                        sell_gallery=id
                        break

                main_robot = robot[i]
                if woids[i][0] != 0:
                    djm, dis_sell, dis_buy, x, y, angle = cal_dis4(robot, buy_gallery, sell_gallery)

                    if process[0][i] == 0:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_buy, flag_buy, robot_flag = move2(buy_gallery,
                                                                                                           main_robot, djm,
                                                                                                           dis_sell,
                                                                                                           process[0],b)
                    if process[0][i] == 1:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_sell, flag_sell, robot_flag = move2(sell_gallery,
                                                                                                             main_robot,
                                                                                                             djm, dis_sell,
                                                                                                             process[0],b)
                    # for robot_id in range(4) :#
                    sys.stdout.write('forward %d %d\n' % (robot_id, line_speed))
                    sys.stdout.write('rotate %d %f\n' % (robot_id, angle_speed))
                    if frame_id<8850:
                        if derta_distance_buy<0.4:
                            if flag_buy and robot_flag==0:
                                sys.stdout.write('buy %d\n' % (robot_id))
                    if 8950>frame_id >8900:
                        sys.stdout.write('buy %d\n' % (robot_id))
                    if derta_distance_sell<0.4:
                        if robot_flag>0:
                            sys.stdout.write('sell %d\n' % (robot_id))
                            woids[i][0] = 0
                            woids[i][1] = -1
                            woids[i][2] = -1
                            woids[i][3] = -1
                            #卖完之后必须使main_robot[5]归0，机器人没有任务了
                else:
                    sys.stdout.write('forward %d %d\n' % (main_robot[0], 0))
                    sys.stdout.write('rotate %d %f\n' % (main_robot[0], 0))
            finish()
        if len(gallery7)==2:#map2
            # derprice = [3000, 3200, 3400, 7100, 7800, 8300, 29000]  # 差价矩阵
            # weight = 80
            sys.stdout.write('%d\n' % frame_id)
            mn = frame_id
            for i in range(4):
                if (woids[i][0] == 0 and robot[i][4] == 0):
                    task = np.zeros((1, 4))  # 临时存储一个任务的信息

                    alltask = np.zeros((1, 4))  # 存储所有候选任务信息
                    nn = nn + 1
                    for gal in gallery:  # 遍历所有工作台
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 1):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery4:
                                if (get_bit_val(int(galsell[4]), 1) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 1):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 2) == 1):
                                            offset = offset + offset4
                                        if noflag4 == 1:
                                            offset = offset + offset4
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 1
                                        task[0][3] = derprice[1 - 1] + offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery5:
                                if (get_bit_val(int(galsell[4]), 1) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 1):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 3) == 1):
                                            offset = offset + offset5
                                        if noflag5 == 1:
                                            offset = offset + offset5

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 1
                                        task[0][3] = derprice[1 - 1] + offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 1
                                    task[0][3] = derprice[1 - 1] + offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 2):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery4:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 1) == 1):
                                            offset = offset + offset4
                                        if noflag4 == 1:
                                            offset = offset + offset4

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 3) == 1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 2
                                    task[0][3] = derprice[2 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 3):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery5:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 1) == 1):
                                            offset = offset + offset5
                                        if noflag5 == 1:
                                            offset = offset + offset5

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 2) == 1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 3
                                    task[0][3] = derprice[3 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 4):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:

                                if (get_bit_val(int(galsell[4]), 4) == 0):
                                    mm = frame_id
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 4):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 5) == 1) and (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 5) == 1) or (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 4
                                        task[0][3] = derprice[4 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 4
                                    task[0][3] = derprice[4 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 5):  # 根据工作台类型判断哪个工作台缺少这一产品
                            if 7900 > frame_id > 7700:
                                gallery7[6][3] = 0
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 5) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 5):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 4) == 1) and (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 4) == 1) or (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 5
                                        task[0][3] = derprice[5 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 5
                                    task[0][3] = derprice[5 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 6):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 6) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 6):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 5) == 1) and (
                                                get_bit_val(int(galsell[4]), 4) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 5) == 1) or (
                                                get_bit_val(int(galsell[4]), 4) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 6
                                        task[0][3] = derprice[6 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 6
                                    task[0][3] = derprice[6 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)

                        if (gal[3] == 1 and gal[5] == 7):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery8:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                    if (len(alltask) > 1):
                        alltask_new = np.delete(alltask, 0, axis=0)
                        # np.savetxt('4.txt', alltask_new)
                        indicator = alltask_new[:, 3]  # 筛选出评价指标那一列进行排序
                        maxindic = np.argmax(indicator)
                        woids[i][0] = 1
                        woids[i][1] = alltask_new[maxindic][0]
                        woids[i][2] = alltask_new[maxindic][1]
                        woids[i][3] = alltask_new[maxindic][2]
                for id in gallery1:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery2:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery3:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery4:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery5:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery6:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery7:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery8:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery9:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break

                main_robot = robot[i]
                if woids[i][0] != 0:
                    djm, dis_sell = cal_dis(robot, sell_gallery)

                    if process[0][i] == 0:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_buy, flag_buy, robot_flag = move3(buy_gallery,
                                                                                                           main_robot,
                                                                                                           djm,
                                                                                                           dis_sell,
                                                                                                           process[0])
                    if process[0][i] == 1:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_sell, flag_sell, robot_flag = move3(
                            sell_gallery,
                            main_robot,
                            djm, dis_sell,
                            process[0])
                    # for robot_id in range(4) :#
                    sys.stdout.write('forward %d %d\n' % (robot_id, line_speed))
                    sys.stdout.write('rotate %d %f\n' % (robot_id, angle_speed))
                    if frame_id < 8850:
                        if derta_distance_buy < 0.4:
                            if flag_buy and robot_flag == 0:
                                sys.stdout.write('buy %d\n' % (robot_id))

                    if derta_distance_sell < 0.4:
                        if robot_flag > 0:
                            sys.stdout.write('sell %d\n' % (robot_id))
                            woids[i][0] = 0
                            woids[i][1] = -1
                            woids[i][2] = -1
                            woids[i][3] = -1
                            # 卖完之后必须使main_robot[5]归0，机器人没有任务了
                else:
                    sys.stdout.write('forward %d %d\n' % (main_robot[0], 0))
                    sys.stdout.write('rotate %d %f\n' % (main_robot[0], 0))
            finish()
        if len(gallery5) > 9 and len(gallery9) ==1:#图三
            if len(gallery7) == 0:
                offset9 = 0  # 123456为9送货给的负增益
            else:
                offset9 = -15000

            noflag4 = 0
            noflag5 = 0
            noflag6 = 0
            for gal in gallery7:
                if (get_bit_val(int(gal[4]), 4) == 0):  # 如果缺少456那么就给送的增益增加
                    noflag4 = 1
                if (get_bit_val(int(gal[4]), 5) == 0):
                    noflag5 = 1
                if (get_bit_val(int(gal[4]), 6) == 0):
                    noflag6 = 1

            # if(frame_id==1):#生成距离矩阵
            # np.savetxt('2.txt', gallery)
            # wgallery = [gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0]]
            sys.stdout.write('%d\n' % frame_id)
            mn = frame_id
            # bianli=[3,2,1,0]
            for i in range(4):
                # woids = [x[5] for x in robot]#所有机器人的任务工作台
                # np.savetxt('1.txt', woids)

                if (woids[i][0] == 0 and robot[i][4] == 0):
                    task = np.zeros((1, 4))  # 临时存储一个任务的信息

                    alltask = np.zeros((1, 4))  # 存储所有候选任务信息
                    nn = nn + 1
                    for gal in gallery:  # 遍历所有工作台
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 1):  # 根据工作台类型判断哪个工作台缺少这一产品
                            # for galsell in gallery4:
                            #     if (get_bit_val(int(galsell[4]), 1) == 0):
                            #         nrepet = 1
                            #         for ii in woids:
                            #             if (ii[2] == galsell[0] and ii[3] == 1):
                            #                 break
                            #             nrepet = nrepet + 1
                            #         if nrepet == 5:
                            #             offset = 0
                            #             if (get_bit_val(int(galsell[4]), 2) == 1):
                            #                 offset = offset + offset4
                            #             if noflag4 == 1:
                            #                 offset = offset + offset4
                            #             task[0][0] = gal[0]
                            #             task[0][1] = galsell[0]
                            #             task[0][2] = 1
                            #             task[0][3] = derprice[1 - 1] + offset - weight * (
                            #                         distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                            #                                                                      galsell[1:3]))
                            #             alltask = np.concatenate((alltask, task), axis=0)
                            # for galsell in gallery5:
                            #     if (get_bit_val(int(galsell[4]), 1) == 0):
                            #         nrepet = 1
                            #         for ii in woids:
                            #             if (ii[2] == galsell[0] and ii[3] == 1):
                            #                 break
                            #             nrepet = nrepet + 1
                            #         if nrepet == 5:
                            #             offset = 0
                            #             if (get_bit_val(int(galsell[4]), 3) == 1):
                            #                 offset = offset + offset5
                            #             if noflag5 == 1:
                            #                 offset = offset + offset5
                            #
                            #             task[0][0] = gal[0]
                            #             task[0][1] = galsell[0]
                            #             task[0][2] = 1
                            #             task[0][3] = derprice[1 - 1] + offset - weight * (
                            #                         distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                            #                                                                      galsell[1:3]))
                            #             alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 1
                                    task[0][3] = derprice[1 - 1] + offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 2):  # 根据工作台类型判断哪个工作台缺少这一产品
                            # for galsell in gallery4:
                            #     if (get_bit_val(int(galsell[4]), 2) == 0):
                            #         nrepet = 1
                            #         for ii in woids:
                            #             if (ii[2] == galsell[0] and ii[3] == 2):
                            #                 break
                            #             nrepet = nrepet + 1
                            #         if nrepet == 5:
                            #             offset = 0
                            #             if (get_bit_val(int(galsell[4]), 1) == 1):
                            #                 offset = offset + offset4
                            #             if noflag4 == 1:
                            #                 offset = offset + offset4
                            #
                            #             task[0][0] = gal[0]
                            #             task[0][1] = galsell[0]
                            #             task[0][2] = 2
                            #             task[0][3] = derprice[2 - 1] + offset - weight * (
                            #                     distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                            #                                                                  galsell[1:3]))
                            #             alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 3) == 1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 2
                                    task[0][3] = derprice[2 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 3):  # 根据工作台类型判断哪个工作台缺少这一产品
                            # for galsell in gallery5:
                            #     if (get_bit_val(int(galsell[4]), 3) == 0):
                            #         nrepet = 1
                            #         for ii in woids:
                            #             if (ii[2] == galsell[0] and ii[3] == 3):
                            #                 break
                            #             nrepet = nrepet + 1
                            #         if nrepet == 5:
                            #             offset = 0
                            #             if (get_bit_val(int(galsell[4]), 1) == 1):
                            #                 offset = offset + offset5
                            #             if noflag5 == 1:
                            #                 offset = offset + offset5
                            #
                            #             task[0][0] = gal[0]
                            #             task[0][1] = galsell[0]
                            #             task[0][2] = 3
                            #             task[0][3] = derprice[3 - 1] + offset - weight * (
                            #                     distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                            #                                                                  galsell[1:3]))
                            #             alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 2) == 1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 3
                                    task[0][3] = derprice[3 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 4):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:

                                if (get_bit_val(int(galsell[4]), 4) == 0):
                                    mm = frame_id
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 4):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 5) == 1) and (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 5) == 1) or (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 4
                                        task[0][3] = derprice[4 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 4
                                    task[0][3] = derprice[4 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 5):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 5) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 5):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 4) == 1) and (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 4) == 1) or (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 5
                                        task[0][3] = derprice[5 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 5
                                    task[0][3] = derprice[5 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 6):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 6) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 6):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 5) == 1) and (
                                                get_bit_val(int(galsell[4]), 4) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 5) == 1) or (
                                                get_bit_val(int(galsell[4]), 4) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 6
                                        task[0][3] = derprice[6 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 6
                                    task[0][3] = derprice[6 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 7):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery8:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                    if (len(alltask) > 1):
                        alltask_new = np.delete(alltask, 0, axis=0)
                        # np.savetxt('4.txt', alltask_new)
                        indicator = alltask_new[:, 3]  # 筛选出评价指标那一列进行排序
                        maxindic = np.argmax(indicator)
                        woids[i][0] = 1
                        woids[i][1] = alltask_new[maxindic][0]
                        woids[i][2] = alltask_new[maxindic][1]
                        woids[i][3] = alltask_new[maxindic][2]
                        # del alltask
                        # del alltask_new

                    # #if 需不需要判断没有接收到任务
                    # if frame_id==1:
                    #     wgallery.append(buy_gallery)
                    #     wgallery.append(sell_gallery)
                    # else:
                    #     wgallery[i*2] = buy_gallery
                    #     wgallery[i*2 + 1] = sell_gallery
                # elif (woids[i][0] != 0 or robot[i][4] != 0):
                #     # #np.savetxt('2.txt', wgallery)
                #     mm=mm+1
                #     buy_gallery=wgallery[i*2]
                #     sell_gallery=wgallery[i*2 + 1]
                # np.savetxt('3.txt', np.append(np.append(np.append(gallery1[0],nn),mm),mn))#查看进接受任务和执行任务两种情况的次数
                # gallery=np.vstack((a, b))
                for id in gallery1:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery2:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery3:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery4:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery5:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery6:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery7:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery8:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery9:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break

                main_robot = robot[i]
                if woids[i][0] != 0:
                    djm, dis_sell = cal_dis(robot, sell_gallery)

                    if process[0][i] == 0:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_buy, flag_buy, robot_flag = move(
                            buy_gallery,
                            main_robot, djm,
                            dis_sell,
                            process[0])
                    if process[0][i] == 1:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_sell, flag_sell, robot_flag = move(
                            sell_gallery,
                            main_robot,
                            djm, dis_sell,
                            process[0])
                    # for robot_id in range(4) :#
                    sys.stdout.write('forward %d %d\n' % (robot_id, line_speed))
                    sys.stdout.write('rotate %d %f\n' % (robot_id, angle_speed))
                    if frame_id < 8850:
                        if derta_distance_buy < 0.4:
                            if flag_buy and robot_flag == 0:
                                sys.stdout.write('buy %d\n' % (robot_id))

                    if derta_distance_sell < 0.4:
                        if robot_flag > 0:
                            sys.stdout.write('sell %d\n' % (robot_id))
                            woids[i][0] = 0
                            woids[i][1] = -1
                            woids[i][2] = -1
                            woids[i][3] = -1
                            # 卖完之后必须使main_robot[5]归0，机器人没有任务了
                else:
                    sys.stdout.write('forward %d %d\n' % (main_robot[0], 0))
                    sys.stdout.write('rotate %d %f\n' % (main_robot[0], 0))
            finish()
        if len(gallery7)==1:#map 4

            if len(gallery7) == 0:
                offset9 = 0  # 123456为9送货给的负增益
            else:
                offset9 = -15000

            noflag4 = 0
            noflag5 = 0
            noflag6 = 0
            for gal in gallery7:
                if (get_bit_val(int(gal[4]), 4) == 0):  # 如果缺少456那么就给送的增益增加
                    noflag4 = 1
                if (get_bit_val(int(gal[4]), 5) == 0):
                    noflag5 = 1
                if (get_bit_val(int(gal[4]), 6) == 0):
                    noflag6 = 1

            # if(frame_id==1):#生成距离矩阵
            # np.savetxt('2.txt', gallery)
            # wgallery = [gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0],gallery1[0]]
            sys.stdout.write('%d\n' % frame_id)
            mn = frame_id
            # bianli=[3,2,1,0]
            for i in range(4):
                if robot[i][0] == 0:
                    offset5 = 2500
                else:
                    offset5 = 1500
                if robot[i][0] == 1 or robot[i][0] == 2:
                    offset4 = 5500
                else:
                    offset4 = 1500
                # woids = [x[5] for x in robot]#所有机器人的任务工作台
                # np.savetxt('1.txt', woids)
                if (woids[i][0] == 0 and robot[i][4] == 0):
                    task = np.zeros((1, 4))  # 临时存储一个任务的信息

                    alltask = np.zeros((1, 4))  # 存储所有候选任务信息
                    nn = nn + 1
                    for gal in gallery:  # 遍历所有工作台
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 1):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery4:
                                if (get_bit_val(int(galsell[4]), 1) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 1):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 2) == 1):
                                            offset = offset + offset4
                                        if noflag4 == 1:
                                            offset = offset + offset4
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 1
                                        task[0][3] = derprice[1 - 1] + offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery5:
                                if (get_bit_val(int(galsell[4]), 1) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 1):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 3) == 1):
                                            offset = offset + offset5
                                        if noflag5 == 1:
                                            offset = offset + offset5

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 1
                                        task[0][3] = derprice[1 - 1] + offset - weight * (
                                                    distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                                 galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 1
                                    task[0][3] = derprice[1 - 1] + offset9 - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 2):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery4:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 1) == 1):
                                            offset = offset + offset4
                                        if noflag4 == 1:
                                            offset = offset + offset4

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 2) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 2):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 3) == 1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 2
                                        task[0][3] = derprice[2 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 2
                                    task[0][3] = derprice[2 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if ((gal[3] == 1 or frame_id <= 50) and gal[5] == 3):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery5:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 1) == 1):
                                            offset = offset + offset5
                                        if noflag5 == 1:
                                            offset = offset + offset5

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery6:
                                if (get_bit_val(int(galsell[4]), 3) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if (ii[2] == galsell[0] and ii[3] == 3):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        offset = 0
                                        if (get_bit_val(int(galsell[4]), 2) == 1):
                                            offset = offset + offset456
                                        if noflag6 == 1:
                                            offset = offset + offset456

                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 3
                                        task[0][3] = derprice[3 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 3
                                    task[0][3] = derprice[3 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3], galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 4):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:

                                if (get_bit_val(int(galsell[4]), 4) == 0):
                                    mm = frame_id
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 4):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 5) == 1) and (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 5) == 1) or (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 4
                                        task[0][3] = derprice[4 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 4
                                    task[0][3] = derprice[4 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 5):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 5) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 5):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 4) == 1) and (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 4) == 1) or (
                                                get_bit_val(int(galsell[4]), 6) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 5
                                        task[0][3] = derprice[5 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 5
                                    task[0][3] = derprice[5 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 6):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery7:
                                if (get_bit_val(int(galsell[4]), 6) == 0):
                                    nrepet = 1
                                    for ii in woids:
                                        if ii[1] == gal[0] or (ii[2] == galsell[0] and ii[3] == 6):
                                            break
                                        nrepet = nrepet + 1
                                    if nrepet == 5:
                                        if (get_bit_val(int(galsell[4]), 5) == 1) and (
                                                get_bit_val(int(galsell[4]), 4) == 1):
                                            offset = offset7
                                        elif (get_bit_val(int(galsell[4]), 5) == 1) or (
                                                get_bit_val(int(galsell[4]), 4) == 1):
                                            offset = offset7 / 2
                                        else:
                                            offset = 0
                                        task[0][0] = gal[0]
                                        task[0][1] = galsell[0]
                                        task[0][2] = 6
                                        task[0][3] = derprice[6 - 1] + offset - weight * (
                                                distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                             galsell[1:3]))
                                        alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 6
                                    task[0][3] = derprice[6 - 1] + offset9 - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                        if (gal[3] == 1 and gal[5] == 7):  # 根据工作台类型判断哪个工作台缺少这一产品
                            for galsell in gallery8:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                            for galsell in gallery9:
                                nrepet = 1
                                for ii in woids:
                                    if ii[1] == gal[0]:
                                        break
                                    nrepet = nrepet + 1
                                if nrepet == 5:
                                    task[0][0] = gal[0]
                                    task[0][1] = galsell[0]
                                    task[0][2] = 7
                                    task[0][3] = derprice[7 - 1] - weight * (
                                            distance(robot[i][1:3], gal[1:3]) + distance(gal[1:3],
                                                                                         galsell[1:3]))
                                    alltask = np.concatenate((alltask, task), axis=0)
                    if (len(alltask) > 1):
                        alltask_new = np.delete(alltask, 0, axis=0)
                        # np.savetxt('4.txt', alltask_new)
                        indicator = alltask_new[:, 3]  # 筛选出评价指标那一列进行排序
                        maxindic = np.argmax(indicator)
                        woids[i][0] = 1
                        woids[i][1] = alltask_new[maxindic][0]
                        woids[i][2] = alltask_new[maxindic][1]
                        woids[i][3] = alltask_new[maxindic][2]

                for id in gallery1:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery2:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery3:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery4:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery5:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery6:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery7:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery8:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break
                for id in gallery9:
                    if id[0] == woids[i][1]:
                        buy_gallery = id
                        break
                    if id[0] == woids[i][2]:
                        sell_gallery = id
                        break

                main_robot = robot[i]
                if woids[i][0] != 0:
                    # np.savetxt('2.txt',gallery5)
                    # np.savetxt('1.txt', gallery6)
                    djm, dis_sell, dis_buy, x, y, angle = cal_dis4(robot, buy_gallery, sell_gallery)

                    if process[0][i] == 0:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])

                        angle_speed, line_speed, robot_id, derta_distance_buy, flag_buy, robot_flag= move1(
                            buy_gallery,
                            main_robot, djm,
                            dis_sell,
                            process[0],x,y,angle,robot)

                    if process[0][i] == 1:
                        process[0][i] = judge(buy_gallery, sell_gallery, main_robot, process[0][i])
                        angle_speed, line_speed, robot_id, derta_distance_sell, flag_sell, robot_flag = move1(
                            sell_gallery,
                            main_robot,
                            djm, dis_sell,
                            process[0],x,y,angle,robot
                        )

                    sys.stdout.write('forward %d %d\n' % (robot_id, line_speed))
                    sys.stdout.write('rotate %d %f\n' % (robot_id, angle_speed))
                    if frame_id < 8850:
                        if derta_distance_buy < 0.4:
                            if flag_buy and robot_flag == 0:
                                sys.stdout.write('buy %d\n' % (robot_id))

                    if derta_distance_sell < 0.4:
                        if robot_flag > 0:
                            sys.stdout.write('sell %d\n' % (robot_id))
                            woids[i][0] = 0
                            woids[i][1] = -1
                            woids[i][2] = -1
                            woids[i][3] = -1
                            # 卖完之后必须使main_robot[5]归0，机器人没有任务了
                else:
                    sys.stdout.write('forward %d %d\n' % (main_robot[0], 0))
                    sys.stdout.write('rotate %d %f\n' % (main_robot[0], 0))
            finish()#map2