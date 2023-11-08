# coding: utf-8

import os
import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt

alphabet = [chr(i) for i in range(65, 91)]
cols = alphabet + [a + b for a in alphabet for b in alphabet]
cols = cols[1:101]

xs_200 = np.load('coordinates/200.npy')
xs_400 = np.load('coordinates/400.npy')
xs_600 = np.load('coordinates/600.npy')
coordinates = {'200': xs_200, '400': xs_400, '600': xs_600}


def main(name, num):
    xs = coordinates[num]
    os.makedirs(os.path.join('image', num, '线性开环%s%s' % (num, name), '有增后减'), exist_ok=True)
    os.makedirs(os.path.join('image', num, '线性开环%s%s' % (num, name), '一直减少'), exist_ok=True)

    file_root = os.path.join('raw_data', num, '线性开环%s%s' % (num, name))

    app = xw.App(visible=False, add_book=False)  # visible=True   显示Excel工作簿；False  不显示工作簿

    file_dir = os.path.join(file_root, '线性开环%s-cost-%s-list.xls' % (num, name))
    file_1 = os.path.join(file_root, '线性开环%s-%s-先减少后增加再减少.xls' % (num, name))
    file_2 = os.path.join(file_root, '线性开环%s-%s-一直减少.xls' % (num, name))

    wb1 = app.books.open(file_1)
    wb2 = app.books.open(file_2)
    wb = app.books.open(file_dir)

    # for wb_ in [wb, wb1, wb2]:
    #     for i in range(1, 101):
    #         wb_.sheets['Sheet1'].range('A' + str(i+1)).value = i

    sheet = wb.sheets['Sheet1']
    n_1, n_2 = 0, 0  # 用于计数两种数据的个数

    j_descending = np.zeros(100)
    for i, col in enumerate(cols):
        col_range = col + '2:' + col + '101'
        raw_data = sheet.range(col_range).value
        assert raw_data[-1] is not None

        # 分类
        data = np.array(raw_data)
        diff = data[1:] - data[:-1]
        descending = diff <= 1e-15
        # print(np.mean(descending))

        # 判据（均有效）
        # criterion = np.all(descending)
        criterion = np.mean(descending) > 0.99  # 一直减少的判据：下降频率高于99%认为是一直减少
        # criterion = not (np.min(raw_data) < raw_data[-1])  # 一直减少的判据（可选）

        if not criterion:
            n_1 += 1
            # wb1.sheets['Sheet1'].range(col + '1').value = str(i+1)
            save_img = os.path.join('image', num, '线性开环%s%s' % (num, name), '有增后减')
            # for j in range(100):
            #     wb1.sheets['Sheet1'].range(col + str(j+2)).value = raw_data[j]
        else:
            n_2 += 1
            # wb2.sheets['Sheet1'].range(col + '1').value = str(i+1)
            save_img = os.path.join('image', num, '线性开环%s%s' % (num, name), '一直减少')
            # for j in range(100):
            #     wb2.sheets['Sheet1'].range(col + str(j+2)).value = raw_data[j]
            j_descending += data


        # plt.plot(xs, data-np.mean(data))
        # plt.xlabel(r'$\mu$')
        # plt.ylabel('$J$')
        # plt.yscale('symlog')
        # plt.xscale('log')
        # plt.savefig(os.path.join(save_img, str(i+1) + '.png'))
        # plt.close()

    # # 写入数目
    # with open(os.path.join(file_root, '统计.txt'), 'w', encoding='utf-8') as f:
    #     f.write('一直减少：%s\n' % n_2)
    #     f.write('有增后减：%s\n' % n_1)
    j_descending /= n_2
    np.save(os.path.join(file_root, 'j_descending.npy'), j_descending)
    wb.save()
    wb1.save()
    wb2.save()
    wb1.close()
    wb2.close()
    wb.close()

    app.quit()


if __name__ == '__main__':
    for num in ['200', '400', '600']:
        for name in ['分段', '因果关系', '非因果关系']:
            main(name, num)
            print(name, num, 'done')
