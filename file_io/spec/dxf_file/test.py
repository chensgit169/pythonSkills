import ezdxf
import matplotlib.pyplot as plt
import numpy as np

from ezdxf.entities.line import Line
from ezdxf.entities.text import Text
from ezdxf.entities.lwpolyline import LWPolyline


def extract_polyline_coordinates(dxf_file_path):
    doc = ezdxf.readfile(dxf_file_path)
    msp = doc.modelspace()

    polyline_coordinates = []
    line_coordinates = []
    for entity in msp:
        if isinstance(entity, LWPolyline):
            # entity.dxftype() == 'LWPOLYLINE'
            points = [(point[0], point[1]) for point in entity.get_points()]
            polyline_coordinates.extend(points)
        elif entity.dxftype() == 'POLYLINE':
            for point in entity.points():
                polyline_coordinates.append((point[0], point[1]))  # 提取(x, y)坐标数据
        elif isinstance(entity, Line):
            start_point = entity.dxf.start
            end_point = entity.dxf.end
            start_point = (start_point[0], start_point[1])
            end_point = (end_point[0], end_point[1])
            print(start_point, end_point)
            line_coordinates.append(start_point)  # 起始点坐标
            line_coordinates.append(end_point)  # 终止点坐标
        elif entity.dxftype() == 'TEXT':
            # 文本标注暂先略过
            assert isinstance(entity, Text)
            # print(entity.dxf.insert[0])
            # print(entity.dxf.insert[1])
            # print(entity.dxf.text)
        else:
            print('Unknown type of entity in .xdf file:', entity.dxftype())
    return line_coordinates


if __name__ == "__main__":
    dxf_file_path = "oblens.dxf"
    coordinates = extract_polyline_coordinates(dxf_file_path)
    # coordinates += [coordinates[0]]

    coordinates = np.array(coordinates).T
    plt.plot(coordinates[0], coordinates[1], '*')
    plt.show()
