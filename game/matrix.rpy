init python:
    import random
    class matrix:
        def __init__(self,xscale,yscale):
            self.xscale=xscale
            self.yscale=yscale
            self.matrix=[[0]*xscale for _ in range(yscale)]

        def change(self):
            _matrix=[]
            for xpos in range(self.xscale):
                _matrix.append([(self.matrix[ypos])[xpos] for ypos in range(len(self.matrix))])
            self.matrix=_matrix

        def move(self,inverse=False):#True 就是向右合并/向下合并
            for k in range(len(self.matrix)):
                _list =(self.matrix[k]).copy()
                if inverse:
                    _list.reverse()
                _xxlist = [i for i in _list if i !=0] #去掉所有0
                if not _xxlist:
                    continue
                for i in range (len(_xxlist)-1):
                    if _xxlist[i]==_xxlist[i+1]:
                        _xxlist[i]*=2
                        _xxlist[i+1]=0  
                _xxlist = [i for i in _xxlist if i !=0] #去掉所有0
                while len(_xxlist)!=len(_list):
                    _xxlist.append(0)
                if inverse:
                    _xxlist.reverse()
                self.matrix[k]=_xxlist.copy()



        def try_move(self,inverse=False):#True 就是向右合并/向下合并 #检测用
            isfull = self.isfull()
            if isfull ==False:
                return False
            for k in range(len(self.matrix)):
                _list =self.matrix[k].copy()
                if inverse:
                    _list.reverse()
                _xxlist = [i for i in _list if i !=0] #去掉所有0
                for i in range (len(_xxlist)-1):
                    if _xxlist[i]==_xxlist[i+1]:
                        return False
            return True

        def damn(self): #gg
            if self.try_move()==False or self.try_move(inverse=True)==False: 
                return False
            self.change()
            if self.try_move()==False or self.try_move(inverse=True)==False:
                self.change()
                return False
            self.change()
            return True

        def set(self,locate,num):
            xpos,ypos = locate
            (self.matrix[ypos])[xpos]=num

        def random_num(self):
            can =[2,2,2,2,2,2,2,4,4,4]
            avail=[]
            if self.isfull()==True:
                return
            for ypos,line in enumerate(self.matrix):
                for xpos,num in enumerate(line):
                    if num == 0:
                        avail.append((xpos,ypos))
            target = random.choice(avail)
            value = random.choice(can)
            self.set(target,value) 
            return                 

        def isfull(self):
            for line in self.matrix:
                if 0 in line:
                    return False
            return True

        def myprint(self):
            for line in self.matrix:
                print(line,end="\n")

        @property
        def maxnum(self):
            _maxnum=0
            for line in self.matrix:
                if _maxnum<max(line):
                    _maxnum=max(line)
            return _maxnum




    # 在命令行中游玩
    # a = matrix(4,4)
    # a.random_num()
    # a.random_num()
    # a.myprint()
    # while a.damn()==False:
        # direct=input("wasd?")
        # if direct == 'a':
            # a.move()
        # elif direct == "d":
            # a.move(True)
        # elif direct == "w":
            # a.change()
            # a.move()
            # a.change()
        # else:
            # a.change()
            # a.move(True)
            # a.change()  
        # a.random_num()
        # a.myprint()




