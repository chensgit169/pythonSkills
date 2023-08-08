from pprint import pprint

args = {'s': 23123123123131, 'lalalallala': 2}
f = open('args.txt', 'w')
pprint(args, stream=f, indent=4)