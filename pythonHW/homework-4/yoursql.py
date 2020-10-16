class Row():

    def __init__(self, keys, data, primary_key=None):
        
        if type(keys) != list or type(data) != list or (primary_key and type(primary_key) != str):

            raise TypeError

        if len(keys) != len(data):

            raise KeyError

        if (not keys) or (not data):

            raise ValueError
        
        if primary_key and (primary_key not in keys):

            raise KeyError

        self.__index = sorted(keys.copy())

        if not primary_key:
            self.__primary_key = keys[0]

        else:
            self.__primary_key = primary_key


        for i in range(len(keys)):

            setattr(self, '_Row__'+str(keys[i]), data[i])

    def __getitem__(self, key):
        
        if key not in self.__index:
            raise KeyError

        return getattr(self, '_Row__' + key)

    def __setitem__(self, key, value):

        if key not in self.__index:
            raise KeyError
        
        setattr(self, '_Row__' + key, value)

    def __iter__(self):

        self.__count = 0
        
        return self

    def __next__(self):

        index = self.__count

        if index >= len(self.__index):

            raise StopIteration

        self.__count += 1

        return self.__index[index]


    def __len__(self):
        
        return len(self.__index)

    def __lt__(self, other):

        if (self.keys() != other.keys()) or (self.get_primary_key() != other.get_primary_key()):

            raise TypeError

        return self[self.get_primary_key()] < other[other.get_primary_key()]

    def keys(self):

        return self.__index.copy()

    def get_primary_key(self):

        return self.__primary_key

class Table():

    def __init__(self, filename, rows=None, keys=None, primary_key=None):


        self.__name = filename

        if rows and keys:
            self.__index = sorted(keys.copy())
            self.__rows = rows.copy()
            # self.__primary_key = keys[0]
            if not primary_key:
                self.__primary_key = keys[0]
            else:
                self.__primary_key = primary_key
                

        else:
            self.__rows = []
            with open(filename, 'r') as f:
                r = f.readlines()
                just = 0
                for i in range(len(r)):
                    r[i] = r[i].strip()
                    if not len(r[i]):
                        continue
                    result = r[i].split(',')
                    for ii in range(len(result)):
                        result[ii] = result[ii].strip()
                        if just:
                            if result[ii].isdigit():
                                result[ii] = int(result[ii])
                            elif '.' in result[ii]:
                                try:
                                    result[ii] = float(result[ii])
                                except:
                                    pass
                    if not just:
                        origin = result.copy()
                        print(result)
                        self.__index = sorted(result.copy())
                        if not primary_key:
                            self.__primary_key = origin[0]
                        else:
                            self.__primary_key = primary_key
                        just = 1
                    else:
                        self.__rows.append(Row(origin.copy(), result.copy(), self.__primary_key))




    def __iter__(self):
        
        self.__count = 0

        for i in range(len(self.__rows)):
            for ii in range(len(self.__rows) - i - 1):
                if self.__rows[ii+1] < self.__rows[ii]:
                    self.__rows[ii], self.__rows[ii+1] = self.__rows[ii+1], self.__rows[ii]


        return self

    def __next__(self):
        
        index = self.__count

        if index >= len(self.__rows):

            raise StopIteration

        self.__count += 1

        return self.__rows[index]

    def __getitem__(self, key):
        
        for i in self.__rows:
            if i[self.__primary_key] == key:
                return i

        raise ValueError
            

    def __len__(self):
        
        return len(self.__rows)

    def get_table_name(self):
        
        return self.__name

    def keys(self):

        return self.__index

    def get_primary_key(self):
        
        return self.__primary_key

    def export(self, filename=None):
        
        if not filename:

            filename = self.__name

        with open(filename, 'w') as f:

            for i in range(len(self.__index)):

                f.write(str(self.__index[i]))

                if i == len(self.__index) - 1:
                    f.write('\n')
                else:
                    f.write(',')
            
            for i in self.__rows:
                for ii in self.__index:

                    f.write(str(i[ii]))

                    if ii == self.__index[-1]:
                        f.write('\n')
                    else:
                        f.write(',')


class Query():


    def __init__(self, query):

        self.__chosen_rows = []
        self.__result_rows = []
        self.__select = query['select']
        self.__ori_table = Table(query["from"])


        if not query['where']:
            self.__chosen_rows = self.__ori_table

        for i in query['where']:

            if i == query['where'][0]:
                search = self.__ori_table
            else:
                search = self.__chosen_rows.copy()
                self.__chosen_rows.clear()

            key = i[0]
            val = i[1]
            opt = i[2]

            if opt == '==':

                for ii in search:

                    if ii[key] == val:
                        self.__chosen_rows.append(ii)
                
            elif opt == '>':

                for ii in search:

                    if ii[key] > val:
                        self.__chosen_rows.append(ii)
            
            elif opt == '<':
                
                for ii in search:

                    if ii[key] < val:
                        self.__chosen_rows.append(ii)

            elif opt == '>=':

                for ii in search:

                    if ii[key] >= val:
                        self.__chosen_rows.append(ii)

            elif opt == '<=':
                
                for ii in search:

                    if ii[key] <= val:
                        self.__chosen_rows.append(ii)

            elif opt == '!=':
                
                for ii in search:

                    if ii[key] != val:
                        self.__chosen_rows.append(ii)


    def as_table(self):

        for i in self.__chosen_rows:

            chara = []

            if self.__ori_table.get_primary_key() not in self.__select:
                self.__select.insert(0, self.__ori_table.get_primary_key())

            for ii in self.__select:
                chara.append(i[ii])

            self.__result_rows.append(Row(self.__select, chara, self.__ori_table.get_primary_key()))
        
        return Table(self.__ori_table.get_table_name(), self.__result_rows, self.__select, self.__ori_table.get_primary_key())




class JoinQuery(Query):

    def __init__(self, query):


        self.__ori_table0 = Table(query['from'][0])
        self.__ori_table1 = Table(query['from'][1])
        self.__where = query['where']
        self.__select = sorted(query['select'])
        self.__new_keys = []
        self.__new_pri_keys0 = self.__ori_table0.get_table_name().replace('.csv', '.'+str(self.__ori_table0.get_primary_key()))
        self.__new_pri_keys1 = self.__ori_table1.get_table_name().replace('.csv', '.'+str(self.__ori_table1.get_primary_key()))
        

        if self.__new_pri_keys0 not in self.__select:
            if self.__new_pri_keys1 not in self.__select:
                self.__select.append(self.__new_pri_keys0)
                self.__select.sort()
                self.__new_pri_key = self.__new_pri_keys0
            else:
                self.__new_pri_key = self.__new_pri_keys1
        else:
            self.__new_pri_key = self.__new_pri_keys0



        for i in self.__ori_table0.keys():

            self.__new_keys.append(self.__ori_table0.get_table_name().replace('.csv', '.'+str(i)))



        for i in self.__ori_table1.keys():

            self.__new_keys.append(self.__ori_table1.get_table_name().replace('.csv', '.'+str(i)))


        self.__new_rows = []
        for i in self.__ori_table0:

            for j in self.__ori_table1:

                newRow = []

                for ii in i:

                    newRow.append(i[ii])

                for jj in j:

                    newRow.append(j[jj])

                self.__new_rows.append(Row(self.__new_keys, newRow))

        self.__joint_table = Table('join.csv', self.__new_rows, self.__new_keys, self.__new_pri_key)

        delete = []

        for i in self.__joint_table:
            try:
                if i[self.__new_pri_keys0] != i[self.__new_pri_keys1]:
                    delete.append(i)
            except:
                delete.append(i)

        for i in delete.copy():
            self.__joint_table._Table__rows.remove(i)
        






    def as_table(self):

        delete = []

        for i in self.__joint_table:

            for ii in self.__where:

                if ii[2] == '==':
                    if i[ii[0]] != ii[1]:
                        delete.append(i)

                elif ii[2] == '<=':
                    if i[ii[0]] > ii[1]:
                        delete.append(i)


                elif ii[2] == '>=':
                    if i[ii[0]] < ii[1]:
                        delete.append(i)


                elif ii[2] == '<':
                    if i[ii[0]] >= ii[1]:
                        delete.append(i)

                elif ii[2] == '>':
                    if i[ii[0]] <= ii[1]:
                        delete.append(i)


                elif ii[2] == '!=':
                    if i[ii[0]] == ii[1]:
                        delete.append(i)
            i._Row__index = self.__select

        for i in delete.copy():

            self.__joint_table._Table__rows.remove(i)

        self.__joint_table._Table__index = self.__select

        return self.__joint_table
        




class AggQuery(Query):

    def __init__(self, query):

        self.__select = query['select']
        self.__pars_select = []
        self.__ori_table = Table(query['from'])
        self.__group_by = query['group_by']
        self.__where = query['where']
        self.__group_obj = []
        self.__group_val = {}
        self.__newrows = []


        for i in self.__select.copy():
            if 'AVG(' in i:
                i = i.replace('AVG(', '')
                i = i.replace(')', '')
                i = ['AVG', i]
            elif 'SUM(' in i:
                i = i.replace('SUM(', '')
                i = i.replace(')', '')
                i = ['SUM', i]
            elif 'MAX(' in i:
                i = i.replace('MAX(', '')
                i = i.replace(')', '')
                i = ['MAX', i]
            elif 'MIN(' in i:
                i = i.replace('MIN(', '')
                i = i.replace(')', '')
                i = ['MIN', i]

            self.__pars_select.append(i)
        

        delete = []

        for i in self.__ori_table:

            for ii in self.__where:

                if ii[2] == '==':
                    if i[ii[0]] != ii[1]:
                        delete.append(i)

                elif ii[2] == '<=':
                    if i[ii[0]] > ii[1]:
                        delete.append(i)


                elif ii[2] == '>=':
                    if i[ii[0]] < ii[1]:
                        delete.append(i)
    

                elif ii[2] == '<':
                    if i[ii[0]] >= ii[1]:
                        delete.append(i)

                elif ii[2] == '>':
                    if i[ii[0]] <= ii[1]:
                        delete.append(i)
                

                elif ii[2] == '!=':
                    if i[ii[0]] == ii[1]:
                        delete.append(i)


        for i in delete.copy():

            self.__ori_table._Table__rows.remove(i)
        
        for i in self.__ori_table:

            if i[self.__group_by] not in self.__group_obj:

                self.__group_obj.append(i[self.__group_by])
        
        self.__group_val = self.__group_val.fromkeys(self.__group_obj, [])



        for i in self.__pars_select:  # i 是解析后的需要的操作和操作对象

            if type(i) == list:  # 确保 i 是解析的list
                for ii in self.__group_obj: # ii是合并后的行的名字，也是行合并的指标

                    temp = []

                    for iii in self.__ori_table: # iii 是大table里面的每一行

                        if iii[self.__group_by] == ii:

                            temp.append(iii[i[1]])

                    if i[0] == 'AVG':
                        value = (sum(temp) / len(temp))
                    elif i[0] == 'SUM':
                        value = sum(temp)
                    elif i[0] == 'MAX':
                        value = max(temp)
                    elif i[0] == 'MIN':
                        value = min(temp)


                    self.__group_val[ii] = self.__group_val[ii] + [value]
            

        

        for i, j in self.__group_val.items():

            newrow = [i]

            for jj in j:

                newrow.append(jj)

            self.__newrows.append(Row(self.__select, newrow))



        self.__new_table = Table(self.__ori_table.get_table_name(), self.__newrows, self.__select)



    def as_table(self):

        return self.__new_table



















        


