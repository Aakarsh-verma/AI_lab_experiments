# R is a set of restrictions
# this functions colors the given city with the given color
# returns false if not possible, returns the set of new restrictions if possible

def addColor(R, city, color):
    ans = []
    for rr in R:
        res = checkRestriction(rr, city, color)
        if res == False:
            return False
        elif res is None:
            continue
        else:
            ans.append(res)
    return ans
        
# checks if the restrition rr allows the given city to have the given color
# returns false if not possible, otherwise returns the new restriction
def checkRestriction(rr, city, color):
    #finding the index of the city (saved to index)
    index = -1
    other = -1
    if rr[0] == city:
        index = 0
        other = 1
    elif rr[1] == city:
        index = 1
        other = 0
    else:
        return rr

    if not isinstance(rr[other], int):
        return [rr[other], color]

    # other component is a color
    if (color != rr[other]):
        return None
    else:
        return False


# solving the CSP by variable elimination
# recursive structure: ci is the city index to be colored (0 = bc, 1 = ab, etc)
# n is the number of colors
# citys is a list of citys
# if coloring is possible returns the city-> color map, otherwise False
def solveCSP(citys, n, R, ci):
    if (ci == 0):
        # in the beginning any color can be assigned to the first city, lets say 1
        newR = addColor(R, citys[0], 1)
        if (newR == False):
            return False
        ans = {citys[0]:1}
        res = solveCSP(citys, n, newR, 1)
        if (res == False):
            return False
        ans.update(res)
        return ans
    elif (ci == len(citys)):
        return {}

    # branching over all possible colors for citys[ci]
    for color in range (1,n+1):
        ans = {citys[ci]:color}
        newR = addColor(R, citys[ci], color)
        if (newR == False):
            continue
        res = solveCSP(citys, n, newR, ci+1)
        if (res == False):
            continue
        #print(ans)
        #print(res)
        #print("============")
        ans.update(res)
        return ans

    # no choice for the current city
    return False


# main program starts
# ===================================================

n=5 #int(input("Enter the number of color"))
colors = [i for i in range(1,n+1)]
#print(colors)

# creating map of canada
# cmap[x] gives the neighbors of the city x
cmap = {
    'ab': ["bc", "nt", "sk"],
    'bc': ["yt", "nt", "ab"],
    'mb': ["sk", "nu", "on"],
    'nb': ["qc", "ns", "pe"],
    'ns': ["nb", "pe"],
    'nl': ["qc"],
    'nt': ["bc", "yt", "ab", "sk", "nu"],
    'nu': ["nt", "mb"],
    'on': ["mb", "qc"],
    'pe': ["nb", "ns"],
    'qc': ["on", "nb", "nl"],
    'sk': ["ab", "mb", "nt"],
    'yt': ["bc", "nt"],
}

# CSP restrictions
# each restriction is modeled as a pair [a,b] which means the city a's
# color is not equal to b, where b is either a color (a number 1 to n) or
# another city. Examples ['bc', 'ab'] means the color of bc should
# not be equal to ab -- ["bc",4] means the color of bc should not be 4
# R is the list of restrictions

R = []

# initiaitiong restrictions based on the city neighborhood

for x, value in cmap.items():
    for y in value:
        R.append([x,y])

# initiating a list of citys
citys = [p for p in cmap]
#print(solveCSP(citys, 3, R, 0))

while(1):
    num=int(input("Enter number of the color? "))
    print(solveCSP(citys, num, R, 0))