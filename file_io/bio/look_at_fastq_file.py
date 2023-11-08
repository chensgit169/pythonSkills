import re

file_name = "test_large_data.fastq"  # 路径
ok = True


pattern1 = r'(^[ATCG]+[ATC])G+$'
pattern2 = r'(^[ATCG]+[ACG])T+$'

with open(file_name, 'r') as f:
    line_num = len(f.readlines())
    print('文件%s, 总行数: %d' % (file_name, line_num))
    if not line_num % 4 == 0:
        print('文件行数不是4的倍数，请检查')
        ok = False

with open(file_name, 'r') as f:
    for i in range(line_num):
        line = f.readline()
        if i % 4 == 0:
            if not line.startswith('@'):
                print('第%d行不是@开头，请检查' % (i + 1), line)
                ok = False
        elif i % 4 == 1:
            if not (re.match(pattern1, line) or re.match(pattern2, line)):
                print('第%d行格式不匹配，请检查' % (i + 1), line)
                ok = False
        elif i % 4 == 2:
            if line == '+':
                print('第%d行不是+，请检查' % (i + 1), line)
                ok = False
        if not ok:
            break
        if i % (line_num // 100) == 0:
            print('进度:', i / line_num * 100, '%', sep='')

    print('检查完毕, 文件格式OK')
    # for i in range(line_num):
    #     line = f.readline()
    #     fs[i // (line_num // num)].write(line)
    #     if i % 1000000 == 0:
    #         print(i/line_num*100, '%', sep='')
