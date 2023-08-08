import tensornetwork as tn
from tensornetwork import contract
from tensornetwork.visualization.graphviz import to_graphviz

# 创建两个张量
A = tn.Node([[1, 2], [3, 4]])
B = tn.Node([[5, 6], [7, 8]])

# 将它们连接成一个四阶张量
C = tn.contract(A[0], B[0])
D = tn.contract(A[1], B[1])
T = tn.contract(C, D)

# 绘制张量网络
graph = to_graphviz(T)
graph.format = 'png'
graph.render('tensor_network')
