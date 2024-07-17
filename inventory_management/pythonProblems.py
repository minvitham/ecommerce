# ############PYTHON CODE TEST############################

# #######FIRST PROBLEM
lst = [1,2,3,4]
def modify_list(lst):
    list_2 = []
    if len(lst)>0:
        for i in range (len(lst)):
            if i != len(lst) -1:
                r = (lst[i]*i) + lst[i+1]
            else:
                r = (lst[i]*i) + lst[0]
            list_2.append(r)
    return list_2

print(modify_list(lst))

#######SECOND PROBLEM

str1 = 'aabcccccaaa'

def compress_string(str1):
    count = 1
    str2 = ''
    for i in range(1,len(str1)):
        if str1[i-1] == str1[i]:
            count +=1
        else:
            str2 = str2 + str1[i-1]
            if count>1:
                str2 += str1(count)
            count = 1
        str2 += str1(count)
    return str2
print(compress_string(str1))


##### DS Design
class NumberStore:
    
    def __init__(self,lst):
        self.lst = lst
    def add(self,num):
        return lst.append(num)
        
    def get_first_unique(self):
        dict_1 = {}
        
        for i in lst:
            if i in dict_1:
                dict_1[i] +=1
            else:
                dict_1[i] = 1
        lis = []
        for key in dict_1.keys():
            if dict_1[key] <= 1:
                lis.append(key)
        #return dict_1
        if len(lis)>0:
            return key
        else:
            return 'no unique value'


store = NumberStore([1,2,3])
store.add(22)
print(store.get_first_unique())