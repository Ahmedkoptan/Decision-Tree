import math
class Shape:
    pass
t = 0 #no. of shapes that are triangles
s = 0 #no. of shapes that are squares
r = rt = rs = 0 # no. of red triangles and squares 
g = gt = gs = 0 # no. of green triangles and squares
y = yt = ys = 0 # no. of yellow triangles and squares
d = dt = ds = 0 # no. of dashed triangles and squares
sld = sldt = slds = 0 # no. of solid triangles and squares
dot = dott = dots = 0 # no. of triangles and squares with dots
nd = ndt = nds = 0 # no. of triangles and squares without dots

def calcEntr(t,s,tot):
    if t == 0:
        entr = -(s/tot)*math.log2(s/tot)
    elif s == 0:
        entr = -(t/tot)*math.log2(t/tot)
    else:
        entr = -(t/tot)*math.log2(t/tot)-(s/tot)*math.log2(s/tot)
    return(entr)

def IG2(hset,p1,h1,p2,h2,tot):
    IG = hset - (p1/tot)*h1 - (p2/tot)*h2
    return(IG)

def IG3(hset,p1,h1,p2,h2,p3,h3,tot):
    IG = hset - (p1/tot)*h1 - (p2/tot)*h2 - (p3/tot)*h3
    return(IG)       

tot = input('The total Number of Elements: ')
tot = int (tot)
set = []

for x in range(0,tot):
    shape = Shape()
    shape.col = input('Color of Element ' + str(x+1) + ': ')
    set.insert(x,shape)
for x in range(0,tot):
    set[x].out = input('Outline of Element ' + str(x+1) + ': ')
for x in range(0,tot):
    set[x].dot = input('Dot of Element ' + str(x+1) + ': ')
for x in range(0,tot):
    set[x].shape = input('Shape of Element ' + str(x+1) + ': ')


# getting the entropy of the total set

for x in range (0,len(set)):
    if set[x].shape == 't':
        t+= 1
    elif set[x].shape == 's':
        s+= 1
hS = calcEntr(t,s,len(set))

# getting the IG for color features, set includes only red (r), green (g) and yellow (y)
for x in range (0,len(set)):
    if set[x].col == 'r':
        r+= 1
        if set[x].shape == 't':
            rt+= 1
        elif set[x].shape == 's':
            rs+= 1
    elif set[x].col == 'g':
        g+= 1
        if set[x].shape == 't':
            gt+= 1
        elif set[x].shape == 's':
            gs+= 1
    elif set[x].col == 'y':
        y+= 1
        if set[x].shape == 't':
            yt+= 1
        elif set[x].shape == 's':
            ys+= 1

hR = calcEntr(rt,rs,len(set))
hG = calcEntr(gt,gs,len(set))
hY = calcEntr(yt,ys,len(set))
IGCol = IG3(hS,r,hR,g,hG,y,hY,len(set))

# getting the IG for outline features, set includes only dashed (d) and solid (sld)
for x in range (0,len(set)):
    if set[x].out == 'd':
        d+= 1
        if set[x].shape == 't':
            dt+= 1
        elif set[x].shape == 's':
            ds+= 1
    elif set[x].out == 's':
        sld+= 1
        if set[x].shape == 't':
            sldt+= 1
        elif set[x].shape == 's':
            slds+= 1

hD = calcEntr(dt,ds,len(set))
hSLD = calcEntr(sldt,slds,len(set))
IGOut = IG2(hS,d,hD,sld,hSLD,len(set))

# getting the IG for dot features, set includes only dot (dt) and no (nd)
for x in range (0,len(set)):
    if set[x].dot == 'y':
        dot+= 1
        if set[x].shape == 't':
            dott+= 1
        elif set[x].shape == 's':
            dots+= 1
    elif set[x].dot == 'n':
        nd+= 1
        if set[x].shape == 't':
            ndt+= 1
        elif set[x].shape == 's':
            nds+= 1
            
hDOT = calcEntr(dott,dots,len(set))
hND = calcEntr(ndt,nds,len(set))
IGDot = IG2(hS,dot,hDOT,nd,hND,len(set))
# We have all three IG's for the first level in a list
Lev1IGs = [IGCol,IGOut,IGDot]

Lev1Attr = max(Lev1IGs)
# since there are only two levels, the parameters of the next level will be within an if condition for each attribute in the first level
#Adding the elements belonging to each feature of the level 1 attribute to their own list in order to run the same operations as before

if Lev1Attr == IGCol:
    redSet = []
    greenSet = []
    yellowSet = []

    for x in range (0,len(set)):
        if set[x].col == 'r':
            redSet.append(set[x])
        elif set[x].col == 'g':
            greenSet.append(set[x])
        elif set[x].col == 'y':
            yellowSet.append(set[x])
    redsetdashedtri = redsetsolidtri = redsetdashedsquare = redsetsolidsquare = 0
    for x in range (0,len(redSet)):
        if redSet[x].out == 'd':
            if redSet[x].shape == 't':
                redsetdashedtri += 1
            elif redSet[x].shape == 's':
                redsetdashedsquare += 1
        elif redSet[x].out == 's':
            if redSet[x].shape == 't':
                redsetsolidtri += 1
            elif redSet[x].shape == 's':
                redsetsolidsquare += 1 
    redsetdottri = redsetndottri = redsetdotsquare = redsetndotsquare = 0
    for x in range (0,len(redSet)):
        if redSet[x].dot == 'y':
            if redSet[x].shape == 't':
                redsetdottri += 1
            elif redSet[x].shape == 's':
                redsetdotsquare += 1
        elif redSet[x].dot == 'n':
            if redSet[x].shape == 't':
                redsetndottri += 1
            elif redSet[x].shape == 's':
                redsetndotsquare += 1     
    greensetdashedtri = greensetsolidtri = greensetdashedsquare = greensetsolidsquare = 0
    for x in range (0,len(greenSet)):
        if greenSet[x].out == 'd':
            if greenSet[x].shape == 't':
                greensetdashedtri += 1
            elif greenSet[x].shape == 's':
                greensetdashedsquare += 1
        elif greenSet[x].out == 's':
            if greenSet[x].shape == 't':
                greensetsolidtri += 1
            elif greenSet[x].shape == 's':
                greensetsolidsquare += 1 
    greensetdottri = greensetndottri = greensetdotsquare = greensetndotsquare = 0
    for x in range (0,len(greenSet)):
        if greenSet[x].dot == 'y':
            if greenSet[x].shape == 't':
                greensetdottri += 1
            elif greenSet[x].shape == 's':
                greensetdotsquare += 1
        elif greenSet[x].dot == 'n':
            if greenSet[x].shape == 't':
                greensetndottri += 1
            elif greenSet[x].shape == 's':
                greensetndotsquare += 1     
    yellowsetdashedtri = yellowsetsolidtri = yellowsetdashedsquare = yellowsetsolidsquare = 0
    for x in range (0,len(yellowSet)):
        if yellowSet[x].out == 'd':
            if yellowSet[x].shape == 't':
                yellowsetdashedtri += 1
            elif yellowSet[x].shape == 's':
                yellowsetdashedsquare += 1
        elif yellowSet[x].out == 's':
            if yellowSet[x].shape == 't':
                yellowsetsolidtri += 1
            elif yellowSet[x].shape == 's':
                yellowsetsolidsquare += 1
    yellowsetdottri = yellowsetndottri = yellowsetdotsquare = yellowsetndotsquare = 0
    for x in range (0,len(yellowSet)):
        if yellowSet[x].dot == 'y':
            if yellowSet[x].shape == 't':
                yellowsetdottri += 1
            elif yellowSet[x].shape == 's':
                yellowsetdotsquare += 1
        elif yellowSet[x].dot == 'n':
            if yellowSet[x].shape == 't':
                yellowsetndottri += 1
            elif yellowSet[x].shape == 's':
                yellowsetndotsquare += 1

    hred = calcEntr((redsetdashedtri+redsetsolidtri),(redsetdashedsquare+redsetsolidsquare),(len(redSet)))
    hreddashed = calcEntr(redsetdashedtri,redsetdashedsquare,(redsetdashedsquare+redsetdashedtri))
    hredsolid = calcEntr(redsetsolidtri,redsetsolidsquare,(redsetsolidsquare+redsetsolidtri))
    hreddot = calcEntr(redsetdottri,redsetdotsquare,(redsetdotsquare+redsetdottri))
    hredndot = calcEntr(redsetndottri,redsetndotsquare,(redsetndotsquare+redsetndottri))
    hgreen = calcEntr((greensetdashedtri+greensetsolidtri),(greensetdashedsquare+greensetsolidsquare),(len(greenSet)))
    hgreendashed = calcEntr(greensetdashedtri,greensetdashedsquare,(greensetdashedsquare+greensetdashedtri))
    hgreensolid = calcEntr(greensetsolidtri,greensetsolidsquare,(greensetsolidsquare+greensetsolidtri))
    hgreendot = calcEntr(greensetdottri,greensetdotsquare,(greensetdotsquare+greensetdottri))
    hgreenndot = calcEntr(greensetndottri,greensetndotsquare,(greensetndotsquare+greensetndottri))
    hyellow = calcEntr((yellowsetdashedtri+yellowsetsolidtri),(yellowsetdashedsquare+yellowsetsolidsquare),(len(yellowSet)))
    hyellowdashed = calcEntr(yellowsetdashedtri,yellowsetdashedsquare,(yellowsetdashedsquare+yellowsetdashedtri))
    hyellowsolid = calcEntr(yellowsetsolidtri,yellowsetsolidsquare,(yellowsetsolidsquare+yellowsetsolidtri))
    hyellowdot = calcEntr(yellowsetdottri,yellowsetdotsquare,(yellowsetdotsquare+yellowsetdottri))
    hyellowndot = calcEntr(yellowsetndottri,yellowsetndotsquare,(yellowsetndotsquare+yellowsetndottri))
    IGOutred = IG2(hred,(redsetdashedsquare+redsetdashedtri),hreddashed,(redsetsolidsquare+redsetsolidtri),hredsolid,(redsetdashedsquare+redsetdashedtri+redsetsolidsquare+redsetsolidtri))
    IGDotred = IG2(hred,(redsetdottri+redsetdotsquare),hreddot,(redsetndotsquare+redsetndottri),hredndot,(redsetdottri+redsetdotsquare+redsetndotsquare+redsetndottri))
    IGOutgreen = IG2(hgreen,(greensetdashedsquare+greensetdashedtri),hgreendashed,(greensetsolidsquare+greensetsolidtri),hgreensolid,(greensetdashedsquare+greensetdashedtri+greensetsolidsquare+greensetsolidtri))
    IGDotgreen = IG2(hgreen,(greensetdottri+greensetdotsquare),hgreendot,(greensetndotsquare+greensetndottri),hgreenndot,(greensetdottri+greensetdotsquare+greensetndotsquare+greensetndottri))
    IGOutyellow = IG2(hyellow,(yellowsetdashedsquare+yellowsetdashedtri),hyellowdashed,(yellowsetsolidsquare+yellowsetsolidtri),hyellowsolid,(yellowsetdashedsquare+yellowsetdashedtri+yellowsetsolidsquare+yellowsetsolidtri))
    IGDotyellow = IG2(hyellow,(yellowsetdottri+yellowsetdotsquare),hyellowdot,(yellowsetndotsquare+yellowsetndottri),hyellowndot,(yellowsetdottri+yellowsetdotsquare+yellowsetndotsquare+yellowsetndottri))
#Checking for leafs is done by checking if the entropy of a set is zero, which corresponds to a leaf
    redLeaf = greenLeaf = yellowLeaf = 0
    if hred == 0:
        if (redsetdashedtri+redsetsolidtri) == 0:
            redLeaf = 'Square'
        else:
            redLeaf = 'Triangle'
    if hgreen == 0:
        if (greensetdashedtri+greensetsolidtri) == 0:
            greenLeaf = 'Square'
        else:
            greenLeaf = 'Triangle'
    else:
        greenLeaf = 0
    if hyellow == 0:
        if (yellowsetdashedtri+yellowsetsolidtri) == 0:
            yellowLeaf = 'Square'
        else:
            yellowLeaf = 'Triangle' 
    else:
        yellowLeaf = 0
# I'm just gonna assume that the color attribute has the highest IG, and not fill out the other two cases, but theyre pretty much the same as the first one
# Comparing the IG's for the attributes in the red set and adding the appropriate elements to their final lists 
    redSetdot = []
    redSetndot = []
    redSetdashed = []
    redSetsolid = []

    if redLeaf == 0:
        if IGDotred>IGOutred:
            for x in range (0,len(redSet)):
                if redSet[x].dot == 'y':
                    redSetdot.append(redSet[x])
                elif redSet[x].dot == 'n':
                    redSetndot.append(redSet[x])
            if redSetdot[0].shape == 't':
                print('Red --> Dot --> Triangle')
                print('Red --> No Dot --> Square')
            else:
                print('Red --> Dot --> Square')
                print('Red --> No Dot --> Triangle')            
        elif IGOutred>IGDotred:
            for x in range (0,len(redSet)):
                if redSet[x].out == 'd':
                    redSetdashed.append(redSet[x])
                elif redSet[x].out == 's':
                    redSetsolid.append(redSet[x])
            if redSetdashed[0].shape == 't':
                print('Red --> Dashed --> Triangle')
                print('Red --> Solid --> Square')
            else:
                print('Red --> Dashed --> Square')
                print('Red --> Solid --> Triangle')
    else:
        print('Red --> ' + redLeaf)

# Comparing the IG's for the attributes in the green set and adding the appropriate elements to their final lists 

    greenSetdot = []
    greenSetndot = []
    greenSetdashed = []
    greenSetsolid = []
    if greenLeaf == 0:
        if IGDotgreen>IGOutgreen:
            for x in range (0,len(greenSet)):
                if greenSet[x].dot == 'y':
                    greenSetdot.append(greenSet[x])
                elif greenSet[x].dot == 'n':
                    greenSetndot.append(greenSet[x])
            if greenSetdot[0].shape == 't':
                print('Green --> Dot --> Triangle')
                print('Creen --> No Dot --> Square')
            else:
                print('Creen --> Dot --> Square')
                print('Green --> No Dot --> Triangle')            
        elif IGOutgreen>IGDotgreen:
            for x in range (0,len(greenSet)):
                if greenSet[x].out == 'd':
                    greenSetdashed.append(greenSet[x])
                elif greenSet[x].out == 's':
                    greenSetsolid.append(greenSet[x])
            if greenSetdashed[0].shape == 't':
                print('Green --> Dashed --> Triangle')
                print('Green --> Solid --> Square')
            else:
                print('Green --> Dashed --> Square')
                print('Green --> Solid --> Triangle')
    else:
        print('Green --> ' + greenLeaf)

    # Comparing the IG's for the attributes in the yellow set and adding the appropriate elements to their final lists 

    yellowSetdot = []
    yellowSetndot = []
    yellowSetdashed = []
    yellowSetsolid = []

    if yellowLeaf == 0:
        if IGDotyellow>IGOutyellow:
            for x in range (0,len(yellowSet)):
                if yellowSet[x].dot == 'y':
                    yellowSetdot.append(yellowSet[x])
                elif yellowSet[x].dot == 'n':
                    yellowSetndot.append(yellowSet[x])
            if yellowSetdot[0].shape == 't':
                print('Yellow --> Dot --> Triangle')
                print('Yellow --> No Dot --> Square')
            else:
                print('Yellow --> Dot --> Square')
                print('Yellow --> No Dot --> Triangle')            
        elif IGOutyellow>IGDotyellow:
            for x in range (0,len(yellowSet)):
                if yellowSet[x].out == 'd':
                    yellowSetdashed.append(yellowSet[x])
                elif yellowSet[x].out == 's':
                    yellowSetsolid.append(yellowSet[x])
            if yellowSetdashed[0].shape == 't':
                print('Yellow --> Dashed --> Triangle')
                print('Yellow --> Solid --> Square')
            else:
                print('Yellow --> Dashed --> Square')
                print('Yellow --> Solid --> Triangle')
    else:
        print('Yellow --> ' + yellowLeaf)

#this is the case for which the outline may have the highest IG
elif Lev1Attr == IGOut:
    solidSet = []
    dashedSet = []

    for x in range (0,len(set)):
        if set[x].out == 's':
            solidSet.append(set[x])
        elif set[x].out == 'd':
            dashedSet.append(set[x])

# this is the case for which the dot attribute may have the highest IG
else:
    dotSet = []
    ndotSet = []

    for x in range (0,len(set)):
        if set[x].dot == 'y':
            dotSet.append(set[x])
        elif set[x].dot == 'n':
            ndotSet.append(set[x])   
