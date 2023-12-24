VERSION = [0, 0, 0]


if __name__ == '__main__':
    with open('./version.txt', 'r+') as f:
        tmp = f.read().split('.')
        VERSION = [int(x) for x in tmp]
        VERSION[1] = VERSION[1] + 1

        with open('./version.txt', 'w') as f:
            f.write('.'.join(map(str, VERSION)))

    with open('./setup.cfg', 'r+') as f:
        lines = f.readlines()
        lines[3] = f"version = {'.'.join([str(x) for x in VERSION])}\n"

        with open('./setup.cfg', 'w') as r:
            r.writelines(lines)
