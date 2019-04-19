#!/usr/bin/env  python3
"""#coding=UTF-8
"""
import	 sys, os, time
def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s\n-------**** %f' %  (date, time.time())

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)
pid = os.fork()
print(type(pid), pid, time.time(), sep= ' --- ')
print(invoke(),end = '\n\n')
##第一个等级顺序: 先执行父pid,     再执行子pid ;
# 第二个等级顺序: 然后先执行父代码,后执行子代码
#time.time()结果:
# .225619 子代码 > .225483 父代码  >  .225416 子pid > .2253447 父pid
#程序运行先后顺序1 :父pid;  2 :子pid;  3 :父代码; 4 :子代码
#>>> .225619 > .225483 > .225416 > .2253447
#True
#>>>  

if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s \033[0m' % sys.argv[0])
#[root@V0 devops_day01]# python3   forkzombie.py 
#__name__  is __main__
#
#<class 'int'> --- 1904 --- 1555551613.2253447 #父进程号1904
#2019年*04月*18日 09时:40分:13秒
#-------**** 1555551613.225483    #父进程执行的结果.225483
#
#<class 'int'> --- 0 --- 1555551613.225416  #子进程号 0
# sys.argv[0]  is forkzombie.py 
#2019年*04月*18日 09时:40分:13秒 
#-------**** 1555551613.225619  #子进程执行的结果.225619 
#
# sys.argv[0]  is forkzombie.py 



