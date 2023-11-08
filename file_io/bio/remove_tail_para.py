from Bio import SeqIO

from utils.timer import Timer
from remove_tail import match_pattern, input_file

import ray

# 初始化Ray
ray.init()

# 将其迁移到一个Ray任务中
parallel_match = ray.remote(match_pattern)


def main():
    timer = Timer()

    # 使用Ray并行化调用函数
    result_ids = [parallel_match.remote(record)
                  for record in SeqIO.parse(input_file, "fastq")]
    results = ray.get(result_ids)
    # print(results)
    timer.end(verbose=True)

    # 关闭Ray
    ray.shutdown()

    # # 遍历Fastq文件中的每一个序列
    # for record in SeqIO.parse(input_file, "fastq"):
    #     # 检查序列的长度是否等于150
    #     assert isinstance(record, SeqRecord)
    #     if len(record) == 150:
    #         assert isinstance(record.seq, Seq)
    #         match_pattern(record)
    #         SeqIO.write([record], output_file, "fastq")
    #     else:
    #         warnings.warn("Length of %s is %i, not 150 so not outputting" % (record.id, len(record)))


if __name__ == '__main__':
    main()
