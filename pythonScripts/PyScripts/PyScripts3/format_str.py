'%c' % 97   # 将９７根据ascii码转换成字符
'%s is %s years old' % ('bob', 25)  # %s使用str()转换成字符串
'%s is %d years old' % ('bob', 25)  # %d使用int()转换成整数
'%d' % 25.6  # 输出25
'%o' % 10  # 转成８进制输出
'%#o' % 10 # 转成带前缀的８进制输出
'%#x' % 10 # 转成带前缀的16进制输出
'%e' % 100000 # 科学计数法
'%f' % (5 / 3)  # 浮点数输出
'%4.2f' % (5 / 3) # 总宽度是４，小数位占２位
"%12s%8s" % ('name', 'age') # name占１２个宽度，右对齐
"%-12s%-8s" % ('name', 'age') # name占１２个宽度，左对齐

"%*s%*s" % (-10, 'name', -5, 'age') # 两个星号用后面的数字取代
"%+d" % 10   # 在正数前面显示+
"%+d" % -10  # 负数前面仍是-
'% d' % 10   # 在正数前面添加空格
'% d' % -10  # 负数前面无空格
'%010d' % 5  # 数字５占１０个宽度，前面用０填充







