import matplotlib.pyplot as plt

f = open('mpl_default_color.txt', 'w')
for i in range(10):
    line = plt.plot([-i, -i])
    color = line[0].get_color()
    f.write(color + '\n')
    line[0].set_label(color)

plt.legend()
plt.savefig('mpl_default_color.png', dpi=160)