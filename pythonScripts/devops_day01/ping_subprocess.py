#!/usr/bin/env  python3
"""#coding=UTF-8
[root@V0 devops_day01]# type  lscpu 
lscpu 是 /usr/bin/lscpu
[root@V0 devops_day01]# rpm   -qf  /usr/bin/lscpu
util-linux-2.23.2-43.el7.x86_64

[root@V0 devops_day01]# lscpu |grep  -i cpu
CPU op-mode(s):        32-bit, 64-bit
CPU(s):                2
On-line CPU(s) list:   0,1
CPU 系列：          6
CPU MHz：             3191.994
NUMA 节点0 CPU：    0,1
  Central  Progressing  Unit 中央处理器，
是一块超大规模的集成电路，是一台计算机的运算核心和控制核心
CPU包括 运算器，高速缓冲存储器，总线

操作系统调度器：拆分CPU为一段段时间的运行片，轮流分配给不同的程序
进程 是 cpu 资源分配 的最小单位
线程 是 cpu 调度     的最小单位

CPU调度的是线程, 系统为进程分配资源，不对线程分配资源
多个CPU多个任务: 
在同一时间点运行多个线程, 哪个线程在哪个CPU执行，跟操作系统和CPU本身的设计有关
多线程，实际上是计算机多种资源(cpu,网络, 内存,硬盘,显示器等)的并行运用，
与CPU的数量没关系
"""
import	 sys, os, time, threading, subprocess

print('\033[31;40;1m__name__  is %s\n\033[0m' % __name__)

def  invoke():
  date = time.strftime('%Y年*%m月*%d日 %H时:%M分:%S秒',time.localtime())
  return   '%s\n-------**** %f' %  (date, time.time())

def  ping(host):
  '''-c   #Count 指定要被发送（或接收）的回送信号请求的数目，由 Count 变量指出。 
     -w   #timeout 这个选项仅和 -c 选项一起才能起作用。
它使 ping 命令以最长的超时时间去等待应答（发送最后一个信息包后）
      -i  #Wait 在每个信息包发送之间等待被 Wait 变量指定的时间（秒数）。
缺省值是在每个信息包发送之间等待 1 秒'''

  hostping = 'ping  -c2  -w0.4  -i0.2  %s &> /dev/null' %  host
  rc = subprocess.call( hostping , shell = True)
  if rc == 0 :
    return  'host %s: is up' % host
  else:
    print('返回值 是 %d' % rc )
    return  'host %s: is down' % host


if __name__ == '__main__':
  print('\033[30;43;1m sys.argv[0]  is %s\n\033[0m' % sys.argv[0])
  hosts = ['192.168.0.%d' % ip for  ip in  range(9, 14)]
  print(hosts)
  start = time.time()
  for  ip  in  hosts:
    print(ping(ip))

  print(time.time() - start)

#host 192.168.0.12: is up
#返回值 是 1
#host 192.168.0.13: is down
#6.657872438430786


