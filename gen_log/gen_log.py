import logging
import sys

#1,创建日志对象
log = logging.getLogger('test_logger')

#2，新建一个日志的格式化输出
form= logging.Formatter('%(asctime)s[%(levelname)s]%(message)s ')

#3.1，新建一个文件日志对象，需要制定保存文件名
file_handle = logging.FileHandler('testlog.log')
#3.2,为文件日志对象绑定格式
file_handle.setFormatter(form)

#4.1 ，新建一个流日志对象，需要指定绑定到哪个流上
console_handle = logging.StreamHandler(sys.stderr)
#4.2 ，为文件日志对象绑定格式
console_handle.setFormatter(form)

#5.1，把文件日志对象绑定到日志对象
log.addHandler(file_handle)
#5.2，把流日志对象绑定到日志对象
log.addHandler(console_handle)

#6，设定日志输出的级别：从低到高分别是
# DEBUG
# INFO
# ERROR
# WARNING
# CRITICAL
log.setLevel(logging.ERROR)

#7,开始输出日志错误
log.error('test in log')
log.warning('test in log')

