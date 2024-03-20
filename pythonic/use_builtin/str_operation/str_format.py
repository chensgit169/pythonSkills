import string

gilt_arg_str = string.Template("gilt_eps=${gilt_eps}")

print(gilt_arg_str.__format__(0.1))
