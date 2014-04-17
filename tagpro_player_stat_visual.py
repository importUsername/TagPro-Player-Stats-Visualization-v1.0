import pygame
import sys
import math
import urllib2
from pygame.locals import *

pygame.init()
pygame.display.set_caption("TagPro Player Stats Graphic")

screen = pygame.display.set_mode((700,700))

#colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
blue = pygame.Color(100,100,255)
grey = pygame.Color(200,200,200)
green = pygame.Color(50,255,50)
red = pygame.Color(255,50,50)

#positions (all equadistant from eachother. basically just points on a circle the same distance apart)
center = (348,398,4,4)

Cp = (550,200,4,4)
maxCp = 1.6

Gr = (627,355,4,4)
maxGr = 6.3

CpPGr = (395,123,4,4)
maxCpPGr = 0.45

Pp = (479,650,4,4)
maxPp = 9

Pr = (308,677,4,4)
maxPr = 78

Rt = (150,600,4,4)
maxRt = 10

Sp = (72,441,4,4)
maxSp = 13

Tg = (99,270,4,4)
maxTg = 10

Dr = (600,526,4,4)
maxDr = 5.5

Hl = (224,150,4,4)
maxHl = 85


screen.fill(200)

def getPlayerDict(): #get info manually
    stats = {"name":raw_input("Player name: "),
             "games":0,"tags":0,"popped":0,
             "grabs":0,"drops":0,"hold":0,
             "caps":0,"prevent":0,"returns":0,
             "support":0}
    for stat in stats:
        if stat != "name":
            stats[stat] = float(raw_input(stat+": "))
    return stats

def loadPlayerDict(url): #grab info frmo provided url
    stats = {"name":"",
             "games":0,"tags":0,"popped":0,
             "grabs":0,"drops":0,"hold":0,
             "caps":0,"prevent":0,"returns":0,
             "support":0}
    page = urllib2.urlopen(url).read()
    stats["name"] = page[page.index("<h3>")+4:page.index("<div>")]
    lst = page[page.index("Support"):page.index("Count")]
    lst = lst.replace('</td><td class="duration">',"</td><td>")
    lst = lst.replace('</td></tr><tr><th>',"</td><td>")
    lst = lst.replace('</th><td>',"</td><td>")
    lst2 = lst.split("</td><td>")
    ind = lst2.index("Month")
    stats["tags"] = float(lst2[21])
    stats["popped"] = float(lst2[22])
    stats["grabs"] = float(lst2[23])
    stats["drops"] = float(lst2[24])
    stats["hold"] = float(lst2[25])
    stats["caps"] = float(lst2[26])
    stats["prevent"] = float(lst2[27])
    stats["returns"] = float(lst2[28])
    stats["support"] = float(lst2[29])
    foundNum = False
    for i in range(50):
        try:
            float(page[page.index("Month")+22+i])
            foundNum = True
            stats["games"] = str(stats["games"]) + page[page.index("Month")+22+i]
        except:
            if foundNum == True:
                break
        
    stats["games"] = float(stats["games"])
    return stats
    

def write(x,y,color,msg,size): #prints onto the screen in selected font
    fontObj = pygame.font.Font('freesansbold.ttf',size)
    msgSurfaceObj = fontObj.render(msg, False, color)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (x,y)
    screen.blit(msgSurfaceObj,msgRectobj)

def getDistance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

#Uses dict so it can be used with other programs
#playerDict = getPlayerDict() #to get info by hand
playerDict = loadPlayerDict(raw_input("Player Url: ")) #to get info with URL

#generate plot points
points = []
m = float(playerDict["caps"])/float(playerDict["games"])#get caps per game
m = m/float(maxCp) #get fraction of max
x = ((Cp[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Cp[1])*m) #calc y
points.append((x,y)) #captures

m = float(playerDict["caps"])/float(playerDict["grabs"])#get caps per grab
m = m/float(maxCpPGr) #get fraction of max
x = ((CpPGr[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-CpPGr[1])*m) #calc y
points.append((x,y)) #captures per grab

m = float(playerDict["hold"])/float(playerDict["games"])#get hold per game
m = m/float(maxHl) #get fraction of max
x = ((Hl[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Hl[1])*m) #calc y
points.append((x,y)) #hold

m = float(playerDict["tags"])/float(playerDict["games"])#get tags per game
m = m/float(maxTg) #get fraction of max
x = ((Tg[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Tg[1])*m) #calc y
points.append((x,y)) #tags

m = float(playerDict["support"])/float(playerDict["games"])#get support per game
m = m/float(maxSp) #get fraction of max
x = ((Sp[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Sp[1])*m) #calc y
points.append((x,y)) #support

m = float(playerDict["returns"])/float(playerDict["games"])#get returns per game
m = m/float(maxRt) #get fraction of max
x = ((Rt[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Rt[1])*m) #calc y
points.append((x,y)) #returns

m = float(playerDict["prevent"])/float(playerDict["games"])#get prevent per game
m = m/float(maxPr) #get fraction of max
x = ((Pr[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Pr[1])*m) #calc y
points.append((x,y)) #prevent

m = float(playerDict["popped"])/float(playerDict["games"])#get popped per game
m = m/float(maxPp) #get fraction of max
x = ((Pp[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Pp[1])*m) #calc y
points.append((x,y)) #popped

m = float(playerDict["drops"])/float(playerDict["games"])#get drops per game
m = m/float(maxDr) #get fraction of max
x = ((Dr[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Dr[1])*m) #calc y
points.append((x,y)) #drops

m = float(playerDict["grabs"])/float(playerDict["games"])#get grabs per game
m = m/float(maxGr) #get fraction of max
x = ((Gr[0]-center[0])*m)+center[0] #calc x
y = center[1] - ((center[1]-Gr[1])*m) #calc y
points.append((x,y)) #grabs


while True:
    screen.fill(grey)# BG

    #outside rim
    pygame.draw.polygon(screen,white,[(Cp[0],Cp[1]),(CpPGr[0],CpPGr[1]),(Hl[0],Hl[1]),(Tg[0],Tg[1]),(Sp[0],Sp[1]),(Rt[0],Rt[1]),(Pr[0],Pr[1]),(Pp[0],Pp[1]),(Dr[0],Dr[1]),(Gr[0],Gr[1])])
    pygame.draw.polygon(screen,black,[(Cp[0],Cp[1]),(CpPGr[0],CpPGr[1]),(Hl[0],Hl[1]),(Tg[0],Tg[1]),(Sp[0],Sp[1]),(Rt[0],Rt[1]),(Pr[0],Pr[1]),(Pp[0],Pp[1]),(Dr[0],Dr[1]),(Gr[0],Gr[1])],3)

    #player shape
    pygame.draw.polygon(screen,blue,points)

    #write names, draw lines/circles. Needed to be separate for adjusted positioning
    pygame.draw.ellipse(screen,black,Cp) #caps
    write(Cp[0],Cp[1]-16,black,"Captures/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Cp[0]+1,Cp[1]+1),1)

    pygame.draw.ellipse(screen,black,Hl) #hold
    write(Hl[0]-38,Hl[1]-16,black,"Hold/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Hl[0]+1,Hl[1]+1),1)

    pygame.draw.ellipse(screen,black,Dr) #drops
    write(Dr[0]-10,Dr[1]+16,red,"Drops/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Dr[0]+1,Dr[1]+1),1)

    pygame.draw.ellipse(screen,black,Tg) #tags
    write(Tg[0]-48,Tg[1]-16,black,"Tags",12)
    write(Tg[0]-48,Tg[1],black,"/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Tg[0]+1,Tg[1]+1),1)

    pygame.draw.ellipse(screen,black,Sp) #support
    write(Sp[0]-60,Sp[1]-16,black,"Support",12)
    write(Sp[0]-56,Sp[1],black,"/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Sp[0]+1,Sp[1]+1),1)

    pygame.draw.ellipse(screen,black,Rt) #returns
    write(Rt[0]-60,Rt[1]+20,black,"Returns/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Rt[0]+1,Rt[1]+1),1)
    
    pygame.draw.ellipse(screen,black,Pr) #prevent
    write(Pr[0]-40,Pr[1]+10,black,"Prevent/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Pr[0]+1,Pr[1]+1),1)

    pygame.draw.ellipse(screen,black,Pp) #popped
    write(Pp[0],Pp[1]+10,red,"Popped/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Pp[0]+1,Pp[1]+1),1)

    pygame.draw.ellipse(screen,black,Gr) #Grabs
    write(Gr[0]+6,Gr[1]-12,black,"Grabs",12)
    write(Gr[0]+6,Gr[1],black,"/Game",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(Gr[0]+1,Gr[1]+1),1)
    
    pygame.draw.ellipse(screen,black,CpPGr) #capture per grab
    write(CpPGr[0]+5,CpPGr[1]-16,black,"Captures/Grab",12)
    pygame.draw.line(screen,black,(center[0],center[1]),(CpPGr[0]+1,CpPGr[1]+1),1)

    #title bar
    write(245,25,black,"Stats For "+playerDict["name"],30)
    write(593,5,black,"Graphic By",10)
    write(585,15,black,"Knuckball AKA",10)
    write(574,25,black,"doctorprofessortaco",10)


    #get input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mx,my = event.pos
        if event.type == MOUSEBUTTONUP:
            pygame.image.save(screen,playerDict["name"]+"stats.png")

    pygame.display.update()

