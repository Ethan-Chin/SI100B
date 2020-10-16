import csv
def check(a):
    try:
        return int(a)
    except ValueError:
        try:
            return float(a)
        except ValueError:
            return a.strip()

class Row():
    __key ,__data ,__sortkey = [] , [] , []
    __PKey , index  = None , 0
    def __init__(self, keys, data, primary_key=None):
        if type(keys) != list or type(data) != list:
            raise TypeError
        elif len(keys) != len(data) or (primary_key is not None and primary_key not in keys):
            raise KeyError
        elif len(keys) == 0 or len(data) == 0:
            raise ValueError
        else:
            self.__key , self.__data = keys[:] , data
            self.__sortkey = keys[:]
            self.__sortkey.sort(key = change)
            if   primary_key != None:
                self.__PKey = str(primary_key)
            elif primary_key == None:
                self.__PKey = keys[0]

    def __getitem__(self, key):  #right
        condition = True
        for k in self.__key:

            if key == k:
                condition = False
        if condition:
            raise KeyError
        else:
            index = self.__key.index(key)
            return self.__data[index]

    def __setitem__(self, key, value):  #right
        if key not in self.__key:
            raise KeyError
        else:
            index = self.__key.index(key)
            self.__data[index] = value

    def __iter__(self):  #right
        return self

    def __next__(self): #right/maybe
        if self.index < len(self.__sortkey) :
            re = self.__sortkey[self.index]
            self.index += 1
            return re
        else :
            self.index = 0
            raise StopIteration

    def __len__(self):   #right
        return len(self.__data)

    def __lt__(self, other):  #right
        if type(other) != type(self) or self.__sortkey != other.__sortkey or self.__PKey != other.__PKey:
            raise TypeError
        else:
            key = self.__PKey
            if str(self[key]) < str(other[key]) :
                return True
        return False

    def keys(self):  #right
        return self.__sortkey

    def get_primary_key(self):  #right
        return str(self.__PKey)
    def testprint(self):  #this is a test function
        print(self.__key,'\n',self.__data)
def change(value):
        return str(value)

class Table():
    def __init__(self, filename, rows=None, keys=None, primary_key=None):
        filesystem , self.__tablename           = [] ,filename
        self.__row , self.__key , self.__index  = [] , [] , 0

        if rows is None:                         #rows是空，
            with open(filename,'r') as file:             #read in the table from the CSV file as specified in filename
                lines = file.readlines()   #The file will always be available in the file system.
                for i in range(0,len(lines)):    #对每一行（type is list）进行操作
                    lines[i] = lines[i].replace('\n','').split(",")#删掉换行符，去掉逗号，变成一个list，存有data
                    item = lines[i]      #减少代码复杂度，保留字符串的格式
                    for j in range(0,len(item)):                       #convert all numeral fields into an integer or floating number
                        item[j] = check(item[j])
                    filesystem.append(Row(lines[0],item,primary_key=primary_key))
            self.__key = lines[0]             #key 中的还是字符串
            self.__row = filesystem[1:]       #row 中的是Row(),data中数字就是数字

        elif rows is not None : #第二种考虑
            self.__row = rows[:]
            self.__key = keys[:]

        if primary_key == None:
            self.__PKey = str(self.__key[0])
        else:
            self.__PKey = str(primary_key)
            if self.__PKey not in self.__key:    # Raise a KeyError if primary_key does not exist in the table.
                raise KeyError                  # 无论是使用key还是用file，keys都会被存进到self.__key

        self.__sortrow = sorted(self.__row[:])
        self.__sortkey = self.__key[:]
        self.__sortkey.sort(key = change)

    def __iter__(self):#same
        return self

    def __next__(self):#same
        if self.__index < len(self.__sortrow):
            re = self.__sortrow[self.__index]
            self.__index += 1
            return re
        else :
            self.__index = 0
            raise StopIteration

    def __getitem__(self, key):  #same
        for r in self.__row :
            for k in self.__key :
                if r[k] == key :
                    return r
        raise ValueError

    def __len__(self):#same
        return len(self.__row)

    def get_table_name(self):#same
        return str(self.__tablename)

    def keys(self):#same
        return self.__sortkey[:]

    def get_primary_key(self):#same
        return str(self.__PKey)

    def export(self, filename=None):
        if filename == None:
            filename = self.__tablename
        f = open(filename,'w',newline='')
        writer = csv.writer(f)
        writer.writerow(self.__key)
        for line in self.__row:
            temp = []
            for c in range(len(line)):
                temp.append(line[self.__key[c]])
            writer.writerow(temp)
        f.close()
    def testprint(self):  #this is a test function
        print(self.__key)
        for v in range(len(self.__row)):
            print("-----",v)
            print(v,":")
            self.__row[v].testprint()

class Query():
    def __init__(self, query):
        self.select  , self.filename = query['select'] , query['from']
        self.where   = []

        if query['where'] == []:
            self.where , self.find = [] , None
        else:
            self.where += [[str(w[1]) , str(w[2])] for w in query['where']]
            self.find = [str(w[0]) for w in query['where']]

        with open(self.filename) as file:
            self.message = file.readlines()
            self.message[0] = self.message[0].replace('\n','').split(",")
            for line in range(1,len(self.message)):
                item = self.message[line].replace('\n','').split(",")
                for i in range(0,len(item)):                 #convert all numeral fields into an integer or floating number
                    item[i] = check(item[i])
                self.message[line] = item[:]
        if self.message[0][0] not in self.select:
            self.select.append(self.message[0][0])
        self.select.sort()
        if self.select != None:
            for i in range(len(self.select)):#If any one of them does not exist, a KeyError should be raised;
                condition = True
                for j in self.message[0]:
                    if self.select[i] == j:
                        condition = False
                if condition:
                    raise KeyError
        if self.find != None:
            for i in range(len(self.find)):#If any one of them does not exist, a KeyError should be raised;
                condition = True
                for j in self.message[0]:
                    if self.find[i] == j:
                        condition = False
                if condition:
                    raise KeyError

    def as_table(self):
        Index , row , place , t  = [] , [] , [] , 0
        if self.find != None:
            place = [self.message[0].index(f) for f in self.find]
        for i in self.select:
            Index.append(self.message[0].index(i))
        for j in range(1, len(self.message)):
            condition = True
            for p in range(len(place)):
                if self.where[p][1].strip() == '==':
                    if str(self.message[j][place[p]]) != self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '!=':
                    if str(self.message[j][place[p]]) == self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '>':
                    if str(self.message[j][place[p]]) <= self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '<':
                    if str(self.message[j][place[p]]) >= self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '>=':
                    if str(self.message[j][place[p]]) < self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '<=':
                    if str(self.message[j][place[p]]) > self.where[p][0]:
                        condition = False
            if self.where == [] or condition:
                row.append([self.message[j][h] for h in Index])
                row[t] ,t = Row(self.select,row[t]) , t+1
        return Table(self.filename,row,self.select)

def get(key):
    return str(key[0])

class JoinQuery(Query):
    def getfront(self,s):
        s = s.replace('.','.#!')
        return s.split('#!')[0]
    def __init__(self, joinquery):
        self.message , self.select , self.filename =  [] , joinquery['select'] ,'join.csv'
        self.where, temp , fm =  [] , [] , [self.getfront(s) for s in joinquery['from']]

        with open(joinquery['from'][0]) as f1:
            table1 = f1.readlines()
            table1=[t1.replace('\n','').split(",") for t1 in table1]
            for tt1 in table1:
                for ttt1 in range(len(tt1)):
                    tt1[ttt1] = str(tt1[ttt1]).strip(' ')

        with open(joinquery['from'][1]) as f2:
            table2 = f2.readlines()
            table2 = [t2.replace('\n','').split(",") for t2 in table2]
            for tt2 in table2:
                for ttt2 in range(len(tt2)):
                    tt2[ttt2] = str(tt2[ttt2]).strip(' ')

        if joinquery['where'] == []:  #无脑copy part1
            self.where , self.find = [] , None
        else:
            self.where += [[w[1] , w[2]] for w in joinquery['where']]
            self.find = [w[0] for w in joinquery['where']]
        table1[0] = [fm[0]+i for i in table1[0]]
        table2[0] = [fm[1]+i for i in table2[0]]

        if table1 != [] and table2 != []:
            self.message.append(table1[0]+table2[0])
            for t1 in range(1,len(table1)):
                for t2 in range(1,len(table2)):
                    if table1[t1][0] == table2[t2][0]:
                        temp.append(table1[t1]+table2[t2])
        elif table1 != [] and table2 == []:
            self.message = table1[0]
            temp = table1[1:]
        elif table == [] and table2 != []:
            self.message = table2[0]
            temp = table2[1:]
        temp.sort(key = get)
        self.message += temp[:]

        for line in range(1,len(self.message)): #无脑copy part2
            item = self.message[line]
            for i in range(0,len(item)):   #convert all numeral fields into an integer or floating number
                item[i] = check(item[i])
            self.message[line] = item[:]

        if self.message[0][0] not in self.select and table2[0][0] not in self.select: #无脑copy part3
            self.select.append(self.message[0][0])

        self.select.sort()
        if self.select != None:
            for i in range(len(self.select)):#If any one of them does not exist, a KeyError should be raised;
                condition = True
                for j in self.message[0]:
                    if self.select[i] == j:
                        condition = False
                if condition:
                    raise KeyError
        if self.find != None:
            for i in range(len(self.find)):#If any one of them does not exist, a KeyError should be raised;
                condition = True
                for j in self.message[0]:
                    if self.find[i] == j:
                        condition = False
                if condition:
                    raise KeyError
    def as_table(self):
        Index , row , place , t  = [] , [] , [] , 0
        if self.find != None:
            place = [self.message[0].index(f) for f in self.find]
        for i in self.select:
            Index.append(self.message[0].index(i))
        for j in range(1, len(self.message)):
            condition = True
            for p in range(len(place)):
                if self.where[p][1].strip() == '==':
                    if self.message[j][place[p]] != self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '!=':
                    if self.message[j][place[p]] == self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '>':
                    if self.message[j][place[p]] <= self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '<':
                    if self.message[j][place[p]] >= self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '>=':
                    if self.message[j][place[p]] < self.where[p][0]:
                        condition = False
                elif self.where[p][1].strip() == '<=':
                    if self.message[j][place[p]] > self.where[p][0]:
                        condition = False
            if self.where == [] or condition:
                row.append([self.message[j][h] for h in Index])
                row[t] ,t = Row(self.select,row[t]) , t+1
        row.sort(key = self.lo)
        return Table(self.filename,row,self.select)
    def lo(self,row):
        return row[self.message[0][0]]
class AggQuery(Query):
    def __init__(self, Aggquery):
        self.__select                  =  self.ForSelect( Aggquery['select'] )   #select有函数
        self.__where , zry             =  Aggquery['where']    , []         #where无函数
        self.gb          ,self.__from  =  Aggquery['group_by'] , Aggquery['from']
        lines   , row    ,Index        =  [] , [] ,  []
        with open(self.__from) as file:
            lines = file.readlines()
            lines[0] = lines[0].replace('\n','').split(",")
            for line in range(1,len(lines)):
                item = lines[line].replace('\n','').split(",")
                for i in range(0,len(item)):                 #convert all numeral fields into an integer or floating number
                    item[i] = check(item[i])
                lines[line] = item[:]
        for i in self.__select:
            for j in range(len(lines[0])):
                if i[1] == lines[0][j]:
                    Index.append(j)
        for i in range(0,len(lines)):
            row.append([lines[i][j] for j in Index])

        for i in range(len(self.__where)):
            index = row[0].index(self.__where[i][0])
            for j in range(1,len(row)):
                condition = True
                if self.__where[i][2].strip() == '==':
                    if str(row[j][index]) != self.__where[i][1]:
                        condition = False
                elif self.__where[i][2].strip() == '!=':
                    if str(row[j][index]) == self.__where[i][1]:
                        condition = False
                elif self.__where[i][2].strip() == '>':
                    if str(row[j][index]) <= self.__where[i][1]:
                        condition = False
                elif self.__where[i][2].strip() == '<':
                    if str(row[j][index]) >= self.__where[i][1]:
                        condition = False
                elif self.__where[i][2].strip() == '>=':
                    if str(row[j][index]) < self.__where[i][1]:
                        condition = False
                elif self.__where[i][2].strip() == '<=':
                    if str(row[j][index]) > self.__where[i][1]:
                        condition = False
                if condition:
                    zry.append(row[j])
        if self.__where == []:
            zry = row[1:]
        yjw , pond = [] , []
        self.gb_index = [self.__select[i][1] for i in range(len(self.__select))].index(self.gb)
        zry = self.ChangeRow(zry)
        for i in range(0,len(zry)):
            if zry[i][self.gb_index] not in pond:
                yjw.append(zry[i])
                pond.append(zry[i][self.gb_index])
        self.key = Aggquery['select']
        self.yjw = [Row(self.key,i) for i in yjw]

    def ForSelect(self,Aggselect):
        NewSelect = []
        for A_s in Aggselect:
            A_s = A_s.replace(')','')
            if 'AVG(' in A_s:
                NewSelect.append(['A',A_s.replace('AVG(', '')])#A means average
            elif 'SUM(' in A_s:
                NewSelect.append(['S',A_s.replace('SUM(', '')])#S means sum
            elif 'MAX(' in A_s:
                NewSelect.append(['M',A_s.replace('MAX(', '')])#M means max
            elif 'MIN(' in A_s:
                NewSelect.append(['m',A_s.replace('MIN(', '')])#m means min
            else:
                NewSelect.append(['N',A_s])#N means nothing
        return NewSelect

    def ChangeRow(self,row):
        pond , num = [] , []
        for i in range(0,len(row)):
            if row[i][self.gb_index] not in pond:
                pond.append(row[i][self.gb_index])
        for i in range(0,len(pond)):
            n = 0
            for j in row:
                if j[self.gb_index] == pond[i]:
                    n += 1
            num.append(n)
        for i in range(len(self.__select)):
            if self.__select[i][0] == 'A':
                A = []
                for j in range(len(pond)):
                    A += [sum(row[t][i] for t,h in enumerate(row) if h[self.gb_index] == pond[j])/num[j]]
                for p in range(len(pond)):
                    for j in row:
                        if j[self.gb_index] == pond[p]:
                            j[i] = A[p]
            elif self.__select[i][0] == 'S':
                S = []
                for j in range(len(pond)):
                    S += [sum(row[t][i] for t,h in enumerate(row) if h[self.gb_index] == pond[j])]
                for p in range(len(pond)):
                    for j in row:
                        if j[self.gb_index] == pond[p]:
                            j[i] = S[p]
            elif self.__select[i][0] == 'M':
                M = []
                for j in range(len(pond)):
                    M += [max(row[t][i] for t,h in enumerate(row) if h[self.gb_index] == pond[j])]
                for p in range(len(pond)):
                    for j in row:
                        if j[self.gb_index] == pond[p]:
                            j[i] = M[p]
            elif self.__select[i][0] == 'm':
                m = []
                for j in range(len(pond)):
                    m += [min(row[t][i] for t,h in enumerate(row) if h[self.gb_index] == pond[j])]
                for p in range(len(pond)):
                    for j in row:
                        if j[self.gb_index] == pond[p]:
                            j[i] = m[p]
        return row

    def as_table(self):
        return  Table(self.__from,self.yjw,self.key)
