

with open('PEP 484 – Type Hints.md', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line, flush=True)
        if line == '```':
            print(line, flush=True)

