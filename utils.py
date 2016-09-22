# -*- coding: utf-8 -*- 
import xlwt





def zhengli():
    keshi_jibing_xiangqing = open('/Users/imac/Downloads/名医百科/科室_疾病_详情.txt', 'r')
    keshi_jibing_xiangqing_xiugai = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_修改.txt', 'w')
    keshi_jibing_xiangqing_quandui = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_全对.txt', 'w')
    keshi_jibing_xiangqing_list = keshi_jibing_xiangqing.readlines()
    for keshi_jibing_xiangqing_one in keshi_jibing_xiangqing_list:
        keshi_jibing_xiangqing_list_one = keshi_jibing_xiangqing_one.split('__')
        if len(keshi_jibing_xiangqing_list_one) == 5:
            keshi_jibing_xiangqing_xiugai.write(keshi_jibing_xiangqing_one)
        else:
            keshi_jibing_xiangqing_quandui.write(keshi_jibing_xiangqing_one)
    
    keshi_jibing_xiangqing_xiugai.close()
    keshi_jibing_xiangqing_quandui.close()
    print '完毕'


keshi_jibing_xiangqing_quandui = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_全对.txt', 'r')
keshi_jibing_xiangqing_len = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_len.txt', 'r')

list_len = list(set(keshi_jibing_xiangqing_len.readlines()))
print   '====  '+str(len(list_len))
for list_len_one in list_len:
    print list_len_one,

a_10=0
a_8=0
a_9=0
a_17=0
a_16=0
a_18=0
a_13=0
a_12=0
a_11=0
a_7=0
a_5=0
a_15=0
a_14=0
a_6=0
a_20=0
a_48=0
# path_one_list =['/Users/imac/Downloads/名医百科/%s.txt','/Users/imac/Downloads/名医百科/%s.txt','/Users/imac/Downloads/名医百科/%s.txt','/Users/imac/Downloads/名医百科/%s.txt','/Users/imac/Downloads/名医百科/%s.txt']
path_suff ='.txt'
path_one ='/Users/imac/Downloads/名医百科/%s.txt'
def write_xls(list_data,name):
    write_txt =open(path_one % name,'w')
    for one_doctor in list_data:
        write_txt.write(one_doctor)

    write_txt.close()
list15=[]
list14=[]
list13=[]
list12=[]
list11=[]
list10=[]
list9=[]
for one in keshi_jibing_xiangqing_quandui:
    len_my =len(one.split('__'));
    if len_my>14:
        list15.append(one)       
    elif   len_my==14:
        list14.append(one)
    elif   len_my==13:
        list13.append(one)
    elif   len_my==12:
        list12.append(one) 
    elif len_my==11:
        list11.append(one)
    elif    len_my==7:
        list10.append(one)
    elif    len_my<7:
        list9.append(one)

write_xls(list15,'含有14个以上词条')
write_xls(list14,'含有14个词条')
write_xls(list13,'含有13个词条')
write_xls(list12,'含有12个词条')
write_xls(list11,'含有11个词条')
write_xls(list10,'含有7个词条')
write_xls(list9,'含有7个以下词条')
    


        
        
#     keshi_jibing_xiangqing_len.write(str(len(one.split('__')))+'\n')
    
keshi_jibing_xiangqing_quandui.close()
keshi_jibing_xiangqing_len.close()
# keshi_jibing_xiangqing.close()





