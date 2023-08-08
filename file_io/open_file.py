# -*- coding: utf-8 -*-
import numpy as np

"""
r  --  read
w  --  write
a  --  append

eb, wb, ab  -- in digital bit format
"""

f = open('../handle_files/test', 'w', encoding='utf-8')  # write
f.write('# write\n')
f.write('Hi~\n')
f.write(f'{np.arange(10)}')
f.close()

# f = open('test', 'a', encoding='utf-8')    # append
# f.write('I am here!\n')
# f.close()
#
# f = open('test', 'r', encoding='utf-8')   # read all
# print(f.read())
# f.close()
#
# f = open('test', 'r+', encoding='utf-8')   # read + write from at cursor
# f.readline()
# a = f.tell()  # location of cursor
# f.seek(a)
# f.write('---write from here---\n')
# f.close()
#
# f = open('test', 'a+', encoding='utf-8')   # read + append in the end
# f.seek(0)
# f.write('a+')
# print(f.read())
# f.close()
#
# f = open('test', 'w+', encoding='utf-8')     # overwrite + read
# f.write('------------------\n')
# a = f.tell()
# f.write('------------------\n')
# f.write('------------------')
#
# f.seek(a)
# f.write("add content here\n")
#
# f.seek(0)
# print(f.read())
# f.close()

#注：还有rU或r+U模式，"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
