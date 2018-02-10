# Build Order

def setup(depen, proj_dict):
    # initialize dictionary
    for i in projects:
        proj_dict[i] = []

    # setup graph of dependencies
    for i in depen:
        proj_dict[i[1]].append(i[0])

    build = []
    num_dep = []

    for i in proj_dict:
        num_dep.append((i, len(proj_dict[i])))

    i = 0
    while i < len(num_dep):
        for i in range(i, len(num_dep)-1):
            min_val = min(num_dep[i], num_dep[i+1])

        num_dep
        i += 1



if __name__ == '__main__':

    projects = ['a', 'b', 'c', 'd', 'e', 'f']

    # direct graph of dependencies
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    # build order
    output = ['f', 'e', 'a', 'b', 'd', 'c']

    setup(dependencies, {})
