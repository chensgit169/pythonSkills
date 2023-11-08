f1 = open('test_large_data.fastq', 'w')
f0 = open('test.fastq', 'r')
data = f0.read()

for i in range(100):
    f1.write(data)
f1.close()
