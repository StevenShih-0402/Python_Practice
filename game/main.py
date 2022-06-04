import pygame
import random
import os
from pygame.draw import rect

WIDTH = 500                                         #設定完就不會變動的數值，在Python以大寫的變數表示，方便檢查
HEIGHT = 600
FPS = 60

WHITE = (255,255,255)
MINT_LEAF = (0, 184, 148)
ORANGEVILLE = (225, 112, 85)
NEON_BLUE = (24, 220, 255)
BLACK = (0, 0, 0)




#--1.遊戲初始化 & 創建視窗--
pygame.init()                                       #把pygame的所有東西初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #存入一個tuple，代表視窗的長和寬
pygame.display.set_caption("太空生存戰")             #視窗標題
icon_img = pygame.image.load(os.path.join("LOGO.png")).convert()
pygame.display.set_icon(icon_img)                   #視窗左上角的icon
clock = pygame.time.Clock()                         #創建一個管理與操控時間的物件

#載入圖片
background_img = pygame.image.load(os.path.join("img", "background.png")).convert()     #將圖片載入("圖片所在資料夾", "圖片檔名")，convert函式會將圖片轉換成pygame容易讀取的格式。要注意在載入圖片前要先初始化，不然會出問題
bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
player_lives_img = pygame.transform.scale(player_img, (25, 19))
player_lives_img.set_colorkey(BLACK)
rock_img = []
for i in range(7):
    rock_img.append(pygame.image.load(os.path.join("img", f"rock{i}.png")).convert())

#載入字體
# font_name = pygame.font.match_font('Impact')           #直接在系統找並載入分數使用的字體(實務上不常用，因為對方電腦不一定有對應字體，且有些字體不支援中文)
font_name = os.path.join("TaipeiSansTCBeta-Bold.ttf")    #將想要的字體下載進來

def drawText(surf, text, size, x, y):                    #(寫在什麼平面上，要寫的文字，文字大小，X座標，Y座標)
    font = pygame.font.Font(font_name, size)             #套用字體
    textSurface = font.render(text, True, WHITE)         #字型呈現在畫面上的格式(內容，是否使用反鋸齒(讓字體看起來比較滑順)，字體顏色)
    textRect = textSurface.get_rect()
    textRect.centerx = x
    textRect.top = y
    surf.blit(textSurface, textRect)                     #將文字依設定畫到畫面上

#載入音效
item_shield_sound = pygame.mixer.Sound(os.path.join("sound", "pow0.wav"))
item_gun_sound = pygame.mixer.Sound(os.path.join("sound", "pow1.wav"))
shoot_sound = pygame.mixer.Sound(os.path.join("sound", "shoot.wav"))
dead_sound = pygame.mixer.Sound(os.path.join("sound", "rumble.ogg"))
explosion_sound = [
    pygame.mixer.Sound(os.path.join("sound", "expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound", "expl1.wav"))
]
pygame.mixer.music.load(os.path.join("sound", "background.ogg"))

pygame.mixer.music.set_volume(0.4)                                      #調整音量
shoot_sound.set_volume(0.4)
explosion_sound[0].set_volume(0.4)
explosion_sound[1].set_volume(0.4)
item_gun_sound.set_volume(0.4)
item_shield_sound.set_volume(0.4)


#載入爆炸動畫
explosion_ani = {}
explosion_ani["big"] = []           #大爆炸(子彈打到石頭)
explosion_ani["small"] = []         #小爆炸(石頭打到飛船)
explosion_ani["player"] = []        #玩家死亡時爆炸

for i in range(9):                  #載入爆炸的圖片
    explosion_img = pygame.image.load(os.path.join("explosion", f"expl{i}.png")).convert()
    explosion_img.set_colorkey(BLACK)
    explosion_ani["big"].append(pygame.transform.scale(explosion_img, (75,75)))       #大爆炸的圖片大小
    explosion_ani["small"].append(pygame.transform.scale(explosion_img, (30,30)))     #小爆炸的圖片大小
    explosion_player = pygame.image.load(os.path.join("player_explosion", f"player_expl{i}.png")).convert()     #玩家死亡的爆炸圖片
    explosion_player.set_colorkey(BLACK)
    explosion_ani["player"].append(explosion_player)

#載入寶物(雙重子彈、盾牌)
item_img = {}
item_img["gun"] = pygame.image.load(os.path.join("item", "gun.png")).convert()
item_img["shield"] = pygame.image.load(os.path.join("item", "shield.png")).convert()

#新增石頭(維持石頭數量)
def rockAdd():
    rock = Rock()
    allSprite.add(rock)
    rocks.add(rock)

#新增生命條
def drawHealthBar(surf, hp, x, y):
    if(hp < 0):
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100) * BAR_LENGTH
    
    bar = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT) #pygame設定矩形的方法(X軸，Y軸，長，寬)，此處設定血條的外框和內容物
    blood = pygame.Rect(x, y, fill, BAR_HEIGHT)

    pygame.draw.rect(surf, MINT_LEAF, blood)
    pygame.draw.rect(surf, WHITE, bar, 2)           #2像素

#畫出剩餘死亡次數
def drawLives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 35*i                                       #每個生命值之間的間隔
        img_rect.y = y
        surf.blit(img, img_rect)

#顯示初始畫面
def drawStart():
    screen.blit(background_img, (0,0))
    drawText(screen, "太空生存戰", 64, WIDTH/2, HEIGHT/4)
    drawText(screen, "← → 控制飛船移動，空白鍵發射子彈", 22, WIDTH/2, HEIGHT/2)
    drawText(screen, "按任意鍵開始遊戲", 18, WIDTH/2, HEIGHT*3/4)
    pygame.display.update()

    waiting = True                                  #初始畫面的顯示狀態
    while waiting:
        clock.tick(FPS)                             #此迴圈在1秒鐘內最多被執行60次，避免因為電腦效能不同而產生畫面顯示上的差異
        # I.取得輸入
        for event in pygame.event.get():            #pygame.event.get(): 回傳使用者動作的事件(以列表回傳)，此處是將使用者的所有動作放入for迴圈逐一檢視
            if(event.type == pygame.QUIT):          #如果event跟『遊戲關閉』的類型一樣
                pygame.quit()                       #關閉視窗
                return True                         #為了避免關閉視窗後，後面的程式依然繼續執行，用return阻隔，不再繼續執行剩下的程式
            if(event.type == pygame.KEYUP):         #如果event跟『按下後放開鍵盤』的類型一樣
                waiting = False                     #離開初始畫面
                return False

class Player(pygame.sprite.Sprite):                                 #Sprite可用來創建遊戲內的物件
    def __init__(self):                                             #宣告時自動執行的函式，用來存放一些基本設定
        pygame.sprite.Sprite.__init__(self)                         #呼叫pygame.sprite.Sprite的基本設定
        # self.image = pygame.Surface((50, 60))#建立一個50X60的物件
        # self.image.fill(MINT_LEAF)           #以MINT_LEAF填滿
        self.image = pygame.transform.scale(player_img, (50, 40))   #載入圖片並進行縮放
        self.image.set_colorkey(BLACK)                              #令指定的RGB顏色變成透明
        self.rect = self.image.get_rect()                           #在視窗中幫物件定位
        self.radius = self.rect.width * 0.85 / 2                    #圓形(偵測碰撞範圍)的半徑
        # pygame.draw.circle(self.image, NEON_BLUE, self.rect.center, self.radius)
        self.rect.centerx = WIDTH/2                                 #可調整X軸和Y軸，以及top、bottom、left、right等方位
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8                                             #物件在X軸上的移動速度
        self.health = 100                                           #玩家的生命值
        self.lives = 2                                              #玩家有3條命
        self.hidden = False                                         #玩家是否死亡
        self.hiddenTime = 0                                         #玩家死亡的時間
        self.gun = 1                                                #玩家能發射的子彈數(1或2)
        self.gunTime = 0                                            #玩家吃到閃電(雙重子彈)的時間

    def update(self):
        now = pygame.time.get_ticks()
        if(self.gun > 1 and now - self.gunTime > 4000):         #道具持續時間4秒
            self.gun -= 1
            self.gunTime = now

        if(self.hidden and now - self.hiddenTime > 1000):       #『update函式被呼叫的時間』與『玩家圖片被隱藏的時間』相差一秒以上時，將玩家圖片重新顯示出來
            self.hidden = False                                                     #狀態改回False
            self.rect.centerx = WIDTH/2                                             #定位到原本的位置
            self.rect.bottom = HEIGHT - 10

        keyPressed = pygame.key.get_pressed()                       #回傳一串布林值，鍵盤中被按下的按鍵會回傳True，否則回傳False
        if(keyPressed[pygame.K_RIGHT]):
            self.rect.x += self.speedx
        if(keyPressed[pygame.K_LEFT]):
            self.rect.x -= self.speedx

        if(self.rect.right > WIDTH):
            self.rect.right = WIDTH
        if(self.rect.left < 0):
            self.rect.left = 0

    def shoot(self):
        if(not(self.hidden)):                                           #玩家在沒有死亡時才能射擊
            if(self.gun == 1):                                          #在子彈數=1的情況
                bullet = Bullet(self.rect.centerx, self.rect.top)
                allSprite.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()                                      #播放射擊音效
            elif(self.gun >= 2):                                        #在子彈數=2的情況
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                allSprite.add(bullet1)
                bullets.add(bullet1)
                allSprite.add(bullet2)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hiddenTime = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+500)                    #死亡後暫時將圖片移到視窗外，讓玩家暫時消失

    def doubleGun(self):
        self.gun += 1
        self.gunTime = pygame.time.get_ticks()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageOrigin = random.choice(rock_img)                                      #pygame.transform.rotate的轉動會有一些失真，在60FPS下，1秒內會疊加60次這樣的失真，會讓畫面產生極大的偏移。因此創建一個沒轉動過的圖片(不讓原本的圖片一直旋轉，而是將沒轉動過的圖片旋轉成不同角度後再重複疊加)
        self.imageOrigin.set_colorkey(BLACK)
        self.image = self.imageOrigin.copy()       
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)                                   #圓形(偵測碰撞範圍)的半徑
        # pygame.draw.circle(self.image, NEON_BLUE, self.rect.center, self.radius)  
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-180, -100)                                      #在視窗外的地方生成石頭再落下
        self.speedx = random.randrange(-3, 3)                                           #-3是為了讓石頭可以往左移動
        self.speedy = random.randrange(2, 9)
        self.totalDegree = 0
        self.rotateDegree = random.randrange(-3, 3)

    def rotate(self):                                                                   #讓石頭旋轉
        self.totalDegree += self.rotateDegree                                           #沒轉動過的圖片→旋轉3度後的圖片→旋轉6度後的圖片→旋轉9度後的圖片
        self.totalDegree = self.totalDegree % 360                                       #不超過360度，因為沒有意義
        self.image = pygame.transform.rotate(self.imageOrigin, self.totalDegree)        #pygame內建讓圖片旋轉的函式(圖片檔名，旋轉角度)
        center = self.rect.center                                                       #由於原先的定位方式是固定的，所以圖片轉動時會一直跑回左上角，造成圖片產生莫名的抖動
        self.rect = self.image.get_rect()
        self.rect.center = center                                                       #改善方法：每次旋轉時都讓圖片重新定位在center
        
    def update(self):
        self.rotate()
        self.rect.x += self.speedx                                                      #讓石頭可以沿著一條隨機的直線移動
        self.rect.y += self.speedy
        if(self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0):    #石頭離開視窗後，立刻補上一顆新的石頭
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-180, -100)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 9)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):                       #x, y表示飛船的所在位置
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x                       #子彈要從飛船前方出現
        self.rect.bottom = y
        self.speedy = -10                           #子彈要往上飛，所以y軸的速度為負

    def update(self):
        self.rect.y += self.speedy
        if(self.rect.bottom < 0):
            self.kill()                             #kill是pygame.sprite.Sprite裡面內建的函式，會在擁有這個物件的群組(allSprite)中把所有該物件(Bullet)移除

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):                       #(爆炸動畫，爆炸中心點，爆炸規模)
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_ani[self.size][0]            #爆炸動畫的第一張圖片
        self.rect = self.image.get_rect()
        self.rect.center = center                          
        self.frame = 0                                      #動畫更新到第幾張圖片
        self.last_update = pygame.time.get_ticks()          #最後一次更新圖片的時間(經過的毫秒數)
        self.frameRate = 50                                 #更新完後過50毫秒再更新下一張(60FPS的情況下，正常更新會太快)，可以用這個控制動畫的速度

    def update(self):
        now = pygame.time.get_ticks()
        if(now - self.last_update > self.frameRate):
            self.last_update = now
            self.frame += 1
            if(self.frame == len(explosion_ani[self.size])):#當圖片更新到最後一張，就清空self停止動畫
                self.kill()
            else:
                self.image = explosion_ani[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

class Item(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["gun", "shield"])
        self.image = item_img[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if(self.rect.top > HEIGHT):                 #掉落到最底部時消失
            self.kill()


pygame.mixer.music.play()                           #播放背景音樂



#--2.建立遊戲迴圈(Game Loop)--
#遊戲的運作方式：開始 → 取得輸入的資料 → 更新遊戲 → 執行遊戲內容並顯示畫面 → 結束 → 過一段時間執行下一次

showStart = True                                #是否要顯示初始畫面
running = True                                  #判斷遊戲是否繼續
while running:
    if(showStart):
        close = drawStart()                     #存放drawStart回傳的布林值，判斷視窗是否關閉
        if(close):                              #如果視窗被關閉(TRUE)
            break                               #跳脫遊戲迴圈(停止遊戲)
        showStart = False
        allSprite = pygame.sprite.Group()                   #用來存放所有Sprite物件的群組
        rocks = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        items = pygame.sprite.Group()

        player = Player()                                   #建立玩家的物件
        allSprite.add(player)                               #放進allSprite
        for i in range(8):
            rockAdd()

        score = 0

    clock.tick(FPS)                             #此迴圈在1秒鐘內最多被執行60次，避免因為電腦效能不同而產生畫面顯示上的差異
    # I.取得輸入
    for event in pygame.event.get():            #pygame.event.get(): 回傳使用者動作的事件(以列表回傳)，此處是將使用者的所有動作放入for迴圈逐一檢視
        if(event.type == pygame.QUIT):          #如果event跟『遊戲關閉』的類型一樣
            running = False                     #離開遊戲迴圈
        if(event.type == pygame.KEYDOWN):       #如果event跟『按下鍵盤』的類型一樣
            if(event.key == pygame.K_SPACE):    #如果按下的是空白鍵
                player.shoot()                  #player執行shoot函式


    # II.更新遊戲
    allSprite.update()                                              #執行allSprite裡所有物件的update函式(現在FPS是60，所以每1/60秒就會執行這段程式，讓物件的位置看起來像翻書動畫動起來一樣)
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)   #sprite內建的方法，可以偵測前兩個sprite群組內的物件是否有發生碰撞，後兩個布林值則是在發生碰撞後，決定Rock或Bullet要不要被刪除，最後會回傳一個碰撞到rock的所有bullet的字典(KEY:rock, VALUE:bullet)
    #石頭撞子彈
    for hit in hits:                                                #由於石頭碰撞後就會從群組中刪除，刪完8顆後就不會有石頭出現了，所以每刪除(擊中)一顆石頭就要補一顆石頭回來
        random.choice(explosion_sound).play()                       #播放爆炸音效
        score += hit.radius                                         #根據碰撞的石頭半徑大小給予分數(hit的key值是碰撞到的石頭)
        explo = Explosion(hit.rect.center, 'big')
        allSprite.add(explo)
        if(random.random() < 0.1):                                  #掉寶率約3%左右
            item = Item(hit.rect.center)
            allSprite.add(item)
            items.add(item)
        rockAdd()

    #石頭撞飛船
    damages = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)       #偵測兩個sprite物件產生碰撞的方法，石頭撞到飛船後，玩家就要死亡並結束遊戲，後面是將偵測碰撞的方式從預設的矩形改成圓形，增加精確度
    for damage in damages:                                                                          #如果death有回傳產生碰撞的列表
        rockAdd()
        player.health -= damage.radius*1.25
        explo = Explosion(damage.rect.center, 'small')
        allSprite.add(explo)
        if(player.health <= 0):
            death_explo = Explosion(player.rect.center, 'player')
            allSprite.add(death_explo)
            dead_sound.play()
            player.lives -= 1                                                                     #死亡後減一條命，再將生命值回滿
            player.health = 100
            player.hide()                                                                         #避免畫面太突兀，死亡後留一點緩衝時間再重生
        
    if player.lives == 0 and not(death_explo.alive()):                                             #玩家生命條全部用完，且爆炸動畫已不存在
        # running = False                                                                          #跳出遊戲迴圈
        showStart = True                                                                           #顯示初始畫面

    #寶物撞飛船
    strongs = pygame.sprite.spritecollide(player, items, True)
    for strong in strongs:
        if(strong.type == "shield"):
            player.health += 20
            if(player.health > 100):
                player.health = 100
            item_shield_sound.play()
        if(strong.type == "gun"):
            player.doubleGun()
            item_gun_sound.play()
    # III.顯示畫面
    # screen.fill(WHITE)                        #填滿特定顏色(R，G，B)
    screen.blit(background_img, (0,0))          #用圖片填滿(圖片檔名，從指定的XY座標開始填滿)
    allSprite.draw(screen)                      #把allSprite的所有物件全部畫進螢幕裡
    drawText(screen, str(score), 18, WIDTH/2, 10)
    drawHealthBar(screen, player.health, 5, 15)
    drawLives(screen, player.lives, player_lives_img, WIDTH-100, 15)
    pygame.display.update()

pygame.quit()