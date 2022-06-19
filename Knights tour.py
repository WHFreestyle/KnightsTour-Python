import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

class spot_innit:
    def __init__(self,x,y,poss_spots):
        self.x = x
        self.y = y
        self.poss_spots = poss_spots
    


sp = [1,1]
visited1 = 0
path1 = []
done= False
spots = [None] * 26

    
def possible_spots(start):
    i = []
    if (start[0]-2)>0 and (start[1]-1)>0:
        i.append([start[0]-2,start[1]-1])
    if (start[0]-2)>0 and (start[1]+1)<6:
        i.append([start[0]-2,start[1]+1])
        
    if (start[0]-1)>0 and (start[1]-2)>0:
        i.append([start[0]-1,start[1]-2])    
    if (start[0]-1)>0 and (start[1]+2)<6:
        i.append([start[0]-1,start[1]+2])
        
    if (start[0]+2)<6 and (start[1]-1)>0:
        i.append([start[0]+2,start[1]-1])
    if (start[0]+2)<6 and (start[1]+1)<6:
        i.append([start[0]+2,start[1]+1])

    if (start[0]+1)<6 and (start[1]-2)>0:
        i.append([start[0]+1,start[1]-2])
    if (start[0]+1)<6 and (start[1]+2)<6:
        i.append([start[0]+1,start[1]+2])
    return i


for x in range(1,6):
    for y in range(1,6):
        spots[(y-1)*5+x]= spot_innit(x,y, possible_spots([x,y]))
    
def main_program(pos, path, visited):
    global done
    if done:
        return
    
    visited += 1
    
    
    path.append(pos)
    if visited == 25:
        print(path)
        for z in range(1,26):
            temp = path[:z]
            for x in range(1,6):
                    print()
                    for y in range(1,6):
                        if [x,y] in temp[:-1]:
                            color.write("#", "STRING")
                        elif [x,y] == temp[-1]:
                            
                            color.write("#", "KEYWORD")
                        else:
                            color.write("#","COMMENT")
            print()
            print()

        done=True
        
        
    some = spots[(pos[1]-1)*5+pos[0]].poss_spots
    if some:
        for x in some:
            if x not in path:
                
                
                main_program(x,path, visited)
    del path[-1]
    return



main_program(sp,path1, visited1)



