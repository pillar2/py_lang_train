#!/bin/env python3
import urllib3
from datetime import datetime as dt
from datetime import timedelta
import json

debug = 3
c_deb = 0

one_week = timedelta(days=7)
base_url = 'http://sapiv2.www.social-touch.com/2/search/statuses/limited.json?'
mobiles=['荣耀畅玩4C','荣耀6','荣耀X2','华为mate7','华为P8','华为P7']
mobiles_livetime = list()
#mobiles_livetime.append((dt.strptime('2015年4月1日','%Y年%m月%d日'),dt.now())) #荣耀畅玩4C
#mobiles_livetime.append((dt.strptime('2014年6月1日','%Y年%m月%d日'),dt.strptime('2015年6月1日','%Y年%m月%d日'))) #荣耀6
#mobiles_livetime.append((dt.strptime('2013年3月1日','%Y年%m月%d日'),dt.now())) #荣耀X2
#mobiles_livetime.append((dt.strptime('2014年8月1日','%Y年%m月%d日'),dt.strptime('2015年8月1日','%Y年%m月%d日'))) #华为mate7
#mobiles_livetime.append((dt.strptime('2015年4月1日','%Y年%m月%d日'),dt.now())) # 华为P8

mobiles_livetime.append((dt.strptime('2015年04月19','%Y年%m月%d'),dt.strptime('2015年10月25','%Y年%m月%d') + one_week))#荣耀畅玩4C
mobiles_livetime.append((dt.strptime('2014年06月09','%Y年%m月%d'),dt.strptime('2015年08月17','%Y年%m月%d') + one_week))#荣耀6
mobiles_livetime.append((dt.strptime('2015年02月25','%Y年%m月%d'),dt.strptime('2015年11月25','%Y年%m月%d') + one_week))#荣耀X2
mobiles_livetime.append((dt.strptime('2014年08月22','%Y年%m月%d'),dt.strptime('2015年10月8','%Y年%m月%d') + one_week))#华为mate7
mobiles_livetime.append((dt.strptime('2015年03月29','%Y年%m月%d'),dt.strptime('2015年10月25','%Y年%m月%d') + one_week))# 华为P8
mobiles_livetime.append((dt.strptime('2014年04月07','%Y年%m月%d'),dt.strptime('2015年09月13','%Y年%m月%d') + one_week))# 华为P7


base_param_dict = {'count':1,'page':1,'dup':0,'antispam':0,'keyid':10,'keyuid':2534826257}

http = urllib3.PoolManager()
for index,mobile in enumerate(mobiles):
	param_dict = base_param_dict.copy()
	param_dict['q'] = mobile
	m_livetime = mobiles_livetime[index]
	s_date = m_livetime[0]
	e_date = m_livetime[1]
	while s_date < e_date:
		next_week = s_date + one_week
		param_dict['starttime'] = int(s_date.timestamp())
		param_dict['endtime'] = int(next_week.timestamp())
		param_url = urllib3.request.urlencode(param_dict)
		r = http.request('GET', base_url + param_url )
		json_res = json.loads(r.data.decode('utf-8'))
		t_num = 0
		if 'total_number' in json_res:
			t_num = json_res['total_number']
		print(mobile,s_date.strftime('%Y/%m/%d'),t_num)

		s_date = next_week
