# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:42:37 2019

@author: Yeally
"""
while(1):


    money =[]
    name = []
    print('欢迎使用AA制计算程序，author: Yeally (^_^)')
    people = eval(input('请输入参与消费人群总数，以回车结束：'))
    for p in range(people):
        single_name = (input('请输入第{}个人的名字，以回车结束：'.format(p+1)))
        single_money = eval(input('请输入{}出的钱，以回车介绍：'.format(single_name)))
        money.append(single_money)
        name.append(single_name)
    

    get = {}
    get_sort2 = []
    sum_trade = 0
    give_number = 0
    
    
    sum_money = sum(money)
    average_money = sum_money / len(name)
#    print('average:', average_money)
    
    for _ in money:
        if _ < average_money:
            give_number += 1
#    print('number of people whose money is less than average money: ', give_number)
    
    for n,m in zip(name,money):
        gt = round(m - average_money,3)
        get[n] = gt
    
    get_sort = sorted( get.items(),key = lambda x:x[1])  #将字典按升序排列
#    print('每个人应该得到得钱总数：', get_sort)
    
    for (a,b) in get_sort:
        get_sort2.append(list((a,b)))      #将列表里的元组元素转变为列表元素
    
    #print('get_sort2: ',get_sort2)
     
    i = 0
    own = 0           #当前面的人（孙等)所给的钱不足时所欠的数
    enough = 0        #当前面的人（孙等)所给的钱还有多余的钱的多余数
    k = len(money)
    for i in range(give_number):
        
        
        if own != 0:
            gap = abs(get_sort2[i][1]) -own
    #        print('gap', gap)
            if gap > 0:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(own)))
                get_sort2[i][1] += own
                k -= 1
                own = 0
            elif gap < 0:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                own = own - abs(get_sort2[i][1])
                get_sort2[i][1] += own
                continue
            else:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                own = own - abs(get_sort2[i][1])
                get_sort2[i][1] += own
                continue
        
                
            
        if (own == 0) and (enough == 0):
            
            decrease =  abs(get_sort2[i][1]) - abs(get_sort2[k-1][1])
    #        print('decrease', decrease)
            if decrease > 0:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[k-1][1])))
                enough = decrease
                k -= 1
            elif decrease < 0:
        #        get_sort2[k-1][1] -= get_sort[i][1]
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                own = abs(decrease)
                if own == 0:
                    k -= 1
            else:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                own = 0
                k -= 1
        #        if abs(get_sort[i+1]) > abs(decrease):
        #            print('{}给{}{}块钱'.format(get_sort[i+1][0], get_sort[k-1][0], abs(decrease)))
        #        sum_r_trade -= get_sort[i][1]
    
        if enough != 0:
            gap2 = abs(get_sort2[k-1][1]) - enough
            while abs(get_sort2[k-1][1]) - enough < 0:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[k-1][1])))
                enough -= abs(get_sort2[k-1][1])
                get_sort2[i][1] += abs(get_sort2[k-1][1])
                k -= 1
            if gap2 > 0:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(enough)))
                get_sort2[k-1][1] -= enough
                enough = 0
                continue
            if gap2 == 0:
                if k > give_number:
                    print('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(enough)))
                get_sort2[k-1][1] -= enough
                enough = 0
                k -= 1
                continue
        