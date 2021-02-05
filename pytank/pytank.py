# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:41:26 2021

"""

import pygame
import time
import random
from pygame.sprite import Sprite
 
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)

#定义一个基类
class BaseItem(Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)

class MainGame():
    window=None
    my_tank = None
 
    #存储敌方坦克的列表
    enemyTankList=[]
    enemyTankCount=5
 
    # 存储我方坦克子弹的列表
    myBulletList = []
    
    #存储敌方子弹的列表
    enemyBulletList=[]
    explodeList = []
 
    #创建墙壁列表
    wallList = []
 
    def __init__(self):
        pass
 
    def startGame(self):
        pygame.display.init() #初始化窗口
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #初始化我方坦克
        self.createMyTank()
        pygame.display.set_caption('坦克大战1.03')
        #初始化敌方坦克
        self.createEnemyTank()
 
        self.createWall()
 
        while True:
            time.sleep(0.02)
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            #绘制文字
            MainGame.window.blit(self.getTextSuface('敌方坦克剩余数量%d'%len(MainGame.enemyTankList)),(10,10))
            #调用坦克显示方法
            if MainGame.my_tank and MainGame.my_tank.live:
                MainGame.my_tank.displayTank()
            else:
                del MainGame.my_tank
                MainGame.my_tank = None
  
            #循环遍历列表显示敌方坦克
            self.blitEnemyTank()
            #循环遍历爆炸列表
            self.blitExplode()
            #循环遍历墙壁
            self.blitWall()
     
            #循环遍历我方坦克的子弹
            self.blitMyBullet()
            #循环遍历子弹列表，展示敌方子弹
            self.blitEnemyBullet()
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
                    #检测我方坦克是否与墙壁发生碰撞
                    MainGame.my_tank.hitWall()
                    MainGame.my_tank.myTank_hit_enemyTank()
         
            pygame.display.update()
 
    def blitWall(self):
        for wall in MainGame.wallList:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.wallList.remove(wall)
 
    def createWall(self):
        #初始化墙壁
        for i in range(6):
            wall = Wall(i*130,220)
            MainGame.wallList.append(wall)
 
    def createMyTank(self):
        MainGame.my_tank = MyTank(350, 300)
        #创建music对象
        music = Music('sound/start.wav')
        music.play()
 
    def createEnemyTank(self):
        top=100
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0,600)
            speed = random.randint(1,4)
            enemy=EnemyTank(left,top,speed)
            MainGame.enemyTankList.append(enemy)
 
    def blitExplode(self):
        for explode in MainGame.explodeList:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.explodeList.remove(explode)
 
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            if enemyTank.live:
                EnemyTank.displayTank(enemyTank)
                enemyTank.randMove()
                enemyTank.hitWall()
 
                if MainGame.my_tank and MainGame.my_tank.live:
                    enemyTank.enemyTank_hit_myTank()
      
                    #发射子弹
                    enemyBullet=enemyTank.shot()
                
                if enemyBullet:
                    MainGame.enemyBulletList.append(enemyBullet)
            else:#不活着 删除
                MainGame.enemyTankList.remove(enemyTank)
                music = Music('sound/fire.wav')
                music.play()
 
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            if myBullet.live:
                myBullet.displayBullet()
                myBullet.move()
                #调用检测我方子弹是否与敌方坦克碰撞
                myBullet.myBullet_hit_enemyTank()
                myBullet.hitWall()
            else:
                MainGame.myBulletList.remove(myBullet)
    
    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            if enemyBullet.live:
                enemyBullet.displayBullet()
                enemyBullet.move()
                #调用敌方子弹与我方坦克的碰撞方法
                enemyBullet.enemyBullet_hit_myTank()
                enemyBullet.hitWall()
            else:
                MainGame.enemyBulletList.remove(enemyBullet)
 
    def endGame(self):
        print('谢谢使用，欢迎再次使用')
        exit()
 
    def getTextSuface(self,text):
        #初始化字体模块
        pygame.font.init()
        font=pygame.font.SysFont('kaiti',18)
        textSurface=font.render(text,True,TEXT_COLOR)
        return textSurface
 
    #获取事件
    def getEvent(self):
        eventList=pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
                
            if event.type == pygame.KEYDOWN:#如果按下下键
                if not MainGame.my_tank:
                    if event.key== pygame.K_ESCAPE:
                        self.createMyTank()
 
                if MainGame.my_tank and MainGame.my_tank.live:
                    #判断上下左右
                    if event.key == pygame.K_LEFT:
                        MainGame.my_tank.direction='L'
                        #修改坦克开关状态
                        MainGame.my_tank.stop=False
                        #MainGame.my_tank.move()
                        print('按下左键，坦克向左移动')
                    elif event.key == pygame.K_RIGHT:
                        MainGame.my_tank.direction='R'
                        MainGame.my_tank.stop = False
                        #MainGame.my_tank.move()
                        print('按下右键，坦克向右移动')
                    elif event.key == pygame.K_UP:
                        MainGame.my_tank.direction='U'
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('按下上键，坦克向上移动')
                    elif event.key == pygame.K_DOWN:
                        MainGame.my_tank.direction='D'
                        MainGame.my_tank.stop = False
                        #MainGame.my_tank.move()
                        print('按下下键，坦克向下移动')
                    elif event.key == pygame.K_SPACE:
                        print('发送子弹')
                        
                        if len(MainGame.myBulletList)<3:#最多发射3个子弹
                              myBullet=Bullet(MainGame.my_tank)
                              MainGame.myBulletList.append(myBullet)
                              music = Music('sound/hit.wav')
                              music.play()
            
            if event.type == pygame.KEYUP:
                if MainGame.my_tank and MainGame.my_tank.live:
                    #判断释放键是上下左右才停止
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        MainGame.my_tank.stop = True
 
class Tank(BaseItem):
    def __init__(self,left,top):#距离左边上边距离
        #保存加载的图片
        self.images={
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        #方向
        self.direction='L'
 
        self.image = self.images[self.direction]
        #根据图片获取区域
        self.rect = self.image.get_rect()
        #设置区域的left和TOP
        self.rect.left=left
        self.rect.top=top
 
        self.speed = 5
        #坦克移动的开关
        self.stop=True
 
        #是否活着
        self.live=True
        #距离原来坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
 
    #tank move
    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        #判断坦克方向
        if self.direction == 'L':
            if self.rect.left>0:
                self.rect.left -=self.speed
        elif self.direction == 'U':
            if self.rect.top>0:
                self.rect.top -=self.speed
        elif self.direction == 'D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top +=self.speed
        elif self.direction == 'R':
            if self.rect.left+self.rect.height<SCREEN_WIDTH:
                self.rect.left += self.speed
 
    #tank shottint
    def shot(self):
        return Bullet(self)
 
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
 
    #检测坦克是否与墙壁发生碰撞
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self,wall):
                self.stay()
 
    def displayTank(self):
        #获取展示的对象
        #调用blit方法展示
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)
 
 
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
        #检查我方坦克与敌方坦克发生碰撞
    
    def myTank_hit_enemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(self,enemyTank):
                self.stay()
 
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        #调用父类的舒适化方法
        super(EnemyTank,self).__init__(left,top)
        #图片
        self.images={
          'U': pygame.image.load('img/enemy1U.gif'),
          'D': pygame.image.load('img/enemy1D.gif'),
          'L': pygame.image.load('img/enemy1L.gif'),
          'R': pygame.image.load('img/enemy1R.gif')
        }
        #方向 随机生成敌方坦克
        self.direction = self.randDirection()
        #根据方向获取image
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
         
        self.rect.left=left
        self.rect.top=top
         
        self.speed=speed
        self.flag=True
         
        self.step=60

    def enemyTank_hit_myTank(self):
        if pygame.sprite.collide_rect(self,MainGame.my_tank):
            self.stay()
            
    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num==2:
            return 'D'
        elif num==3:
            return 'L'
        elif num==4:
            return 'R'
            
    def randMove(self):
        if self.step<=0:
            self.step=60
            self.direction = self.randDirection()
        else:
            self.move()
            self.step-=1
            
    def shot(self):
        #随机生成100以内的数
        num = random.randint(1,100)
        if num<10:
            return Bullet(self)
        
class Bullet(BaseItem):
    def __init__(self,tank):
#        self.image = pygame.image.load('img/enemymissile.gif')
        self.image = pygame.image.load('img/dzd.gif')
        #坦克的方向决定子弹的方向
        self.direction = tank.direction
        #获取区域
        self.rect = self.image.get_rect()
 
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
 
        #子弹的速度
        self.speed=6
 
        #子弹的姿态，是否碰到墙壁，如果是墙壁，修改此状态
        self.live=True
 
    #move
    def move(self):
        if self.direction == 'U':
            if self.rect.top>0:
                self.rect.top-=self.speed
            else:
                #修改子弹的状态
                self.live=False
        elif self.direction == 'R':
            if self.rect.left+self.rect.width<SCREEN_WIDTH:
                self.rect.left+=self.speed
            else:
                self.live=False
        elif self.direction == 'D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top+=self.speed
            else:
                self.live=False
        elif self.direction == 'L':
            if self.rect.left>0:
                self.rect.left-=self.speed
            else:
                self.live=False
 
    #我方坦克和敌方子弹的碰撞
    def myBullet_hit_enemyTank(self):
        #循环遍历敌方坦克列表，判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank,self):
                #修改敌方坦克和我方子弹的状态
                enemyTank.live = False
                self.live = False
                #创建爆炸对象
                explode = Explode(enemyTank)
                MainGame.explodeList.append(explode)
 
    #子弹是否碰撞墙壁
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self,wall):
                self.live=False
                wall.hp-=1
            if wall.hp<=0:
                wall.live=False
    
    #show
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
 
    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank,self):
                explode = Explode(MainGame.my_tank)
                MainGame.explodeList.append(explode)
                self.live=False
                MainGame.my_tank.live=False
 
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load('img/steels.gif')
         
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
         
        self.live = True
        #设置墙壁生命值
        self.hp = 3
 
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)
 
class Explode():
    def __init__(self,tank):
        #爆炸的位置有当前子弹打中的位置确定
        self.rect=tank.rect
        self.images=[
#           pygame.image.load('img/blast0.gif'),
           pygame.image.load('img/blast1.gif'),
           pygame.image.load('img/blast2.gif'),
           pygame.image.load('img/blast3.gif'),
           pygame.image.load('img/blast4.gif'),
           pygame.image.load('img/blast5.gif')
         ]
        self.step=0
        self.image = self.images[self.step]
     
        self.live=True
    
    def displayExplode(self):
        #根据索引获取爆炸对象
        if self.step < len(self.images):
            self.image = self.images[self.step]
            self.step+=1
            MainGame.window.blit(self.image,self.rect)
        else:
            self.live=False
            self.step=0
 
class Music():
    def __init__(self,fileName):
        self.fileName = fileName
        #play music
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)
     
    def play(self):
        pygame.mixer.music.play()
 
 
if __name__ == '__main__':
    MainGame().startGame()
    #MainGame().getTextSuface()