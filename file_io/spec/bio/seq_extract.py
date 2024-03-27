import re
import os
from time import time

import pandas as pd

fastq_file_name = "test_large_data.fastq"  # 原始fastq文件路径
excel_dir = 'extracted_excels'  # 存储表格的路径
excel_name = 'extracted'  # 表格文件名
os.makedirs(excel_dir, exist_ok=True)

# 需要提取的条目
columns = ['序列ID', '序列长度', '序列数据', '序列质量分数', '末尾碱基(机器自动补全,已去除)']

# DNA序列模式（正则表达式）
pattern = {'G': r'(^[ATCG]+[ATC])G+$',
           'T': r'(^[ATCG]+[ACG])T+$',
           'A': r'(^[ATCG]+[TCG])A+$',  # 没有补齐过的
           'C': r'(^[ATCG]+[TCG])C+$',  # 没有补齐过的
           }


class Timer:
    """
    计时器
    """

    def __init__(self):
        self.start_time = time()
        self.end_time = time()

    def end(self, verbose: bool = False):
        self.end_time = time()
        used_time = self.end_time - self.start_time
        if verbose:
            print(f"Used time: {used_time:.3f}s")
        return used_time

    @classmethod
    def start(cls):
        return cls()


def save_to_excel(data, excel_name_):
    """
    保存提取到的数据到Excel表格
    """
    df = pd.DataFrame(data=data,
                      columns=columns)
    df.to_excel(excel_name_, index=False)


def extract_data(lines, i: int, verbose: bool = False):
    """
    从4行中提取一条DNA序列相关信息
    """
    assert len(lines) == 4

    # ID
    seq_id = lines[0].split(' ')[0][1:]

    # DNA序列数据
    line_seq = lines[1]
    which = line_seq[-1]
    match = re.match(pattern[which], line_seq)
    if not match:
        raise RuntimeError('匹配失败, 请检查文件第%d行' % (4 * (i+1) + 2))
    else:
        if which in ['G', 'T']:
            seq = match.group(1)
        else:
            seq = line_seq

    seq_len = len(seq)
    if seq_len + 2 <= len(line_seq):
        seq += 2 * which  # 对自动补全的碱基保留2个
        seq_len = len(seq)

    # 分隔符
    assert lines[2] == '+', '分隔符异常, 请检查文件第%d行' % (4 * (i+1) + 3)

    # Quality Score序列
    seq_quality = lines[3][:seq_len]

    if verbose:
        print('///////////////////////////')
        print('序列ID:', seq_id)
        print('原始数据的序列:', line_seq)
        print('去除末尾后序列:', seq)
        print('去除末尾后长度:', seq_len)
        print()

    # '序列ID', '序列长度', '序列数据', '序列质量分数', '末尾碱基(机器自动补全,已去除)'
    return [seq_id, seq_len, seq, seq_quality, which]


def main(verbose: bool = False):
    """
    Args:
        verbose: 是否实时打印处理信息
    """
    timer = Timer()
    data = []
    k = 1

    # 获取行数并确认为4的倍数
    with open(fastq_file_name, 'r') as f:
        line_num = len(f.readlines())
        print('文件%s, 总行数: %d' % (fastq_file_name, line_num))
        assert line_num % 4 == 0, '文件行数不是4的倍数，请检查'

    timer.end(verbose=verbose)

    with open(fastq_file_name, 'r') as f:
        for i in range(line_num // 4):
            # 提取数据
            lines = [f.readline().strip() for _ in range(4)]
            seq_data = extract_data(lines, i, verbose)
            seq_len = seq_data[1]
            if 118 <= seq_len <= 152:  # 按长度筛选
                data.append(seq_data)

            # 每积累十万条数据写入一个excel
            if len(data) == 100000:
                file_name = excel_name+'_%d.xlsx' % k  # 这里可以更改Excel文件名
                k += 1
                print('进度:', 4 * i / line_num * 100, '%', sep='')
                print('写入文件%s...' % file_name)
                save_to_excel(data, os.path.join(excel_dir, file_name))
                data = []
                timer.end(verbose=verbose)

            file_name = excel_name + '_%d.xlsx' % k



if __name__ == '__main__':
    main(verbose=True)
