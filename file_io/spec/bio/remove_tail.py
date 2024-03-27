from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

import re
import warnings

from utils.timer import Timer


# 输入和输出文件路径
input_file = "test_data.fastq"
output_file = "output_file.fastq"

pattern = r'(^[ATCG]+[ATC])G+$'


def match_pattern(record: SeqRecord, verbose: bool = False):
    seq_str = str(record.seq)
    if not len(record) == 150:
        warnings.warn("Length of %s is %i, not 150 so not outputting" % (record.id, len(record)))
    # end = seq_str[-1]

    match = re.match(pattern, seq_str)

    if not match:
        status = '匹配失败'
        warnings.warn(status)
        seq_extracted = ''
    else:
        status = '匹配成功'
        seq_extracted = match.group(1)
        
    if verbose:
        print('///////////////////////////')
        print('序列ID:', record.id)
        print(status)
        print('原始数据的序列:', record.seq)
        print('去除末尾后序列:', seq_extracted)
        print('去除末尾后长度:', len(seq_extracted))
        print()
    return seq_extracted


def main():
    timer = Timer()

    # 遍历Fastq文件中的每一个序列
    for record in SeqIO.parse(input_file, "fastq"):
        # 检查序列的长度是否等于150
        match_pattern(record, verbose=True)

        # new_record = SeqRecord(seq=record.seq,
        #                        id=record.id,
        #                        name=record.name,
        #                        description="",
        #                        letter_annotations=record.letter_annotations,
        #                        annotations=record.annotations,
        #                        dbxrefs=record.dbxrefs,
        #                        features=record.features,
        #                        )
        SeqIO.write([record], output_file, "fastq")
    timer.end(verbose=True)


if __name__ == '__main__':
    main()
