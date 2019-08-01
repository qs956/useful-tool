#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__CreatTime__ = r'2019/07/29'
__Author__    = r'罗梓颖'
__Email__     = r'qs956@163.com'
__Location__  = r'South China Normal University,GuangZhou China'
__Github__    = r'https://github.com/qs956'
__Filename__  = r'批量文件重命名.py'

import os

file_ignore = set([
__Filename__,
])
end_ignore = set()

if __name__ == '__main__':
	file_list = os.listdir(r'./')
	front = input(r'输入文件前缀,从前缀后开始从0开始编号:')
	ignore_end  = input(r'输入忽略的后缀,逗号分隔,不带.:')
	ignore_file = input(r'输入忽略的文件名(含后缀),逗号分隔:')
	for i in ignore_file.split(','):
		file_ignore.add(i)
	for i in ignore_end.split(','):
		end_ignore.add(i)
		
	for i in range(len(file_list)):
		if file_list[i] in file_ignore:
			continue
		end = file_list[i].split('.')[-1]
		if end in end_ignore:
			continue
		name = front + str(i) + r'.' + end
		os.rename(file_list[i],name)