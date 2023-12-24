VERSION = [0, 24, 0]


if __name__ == '__main__':
    VERSION[1] += 1

    with open('../../setup.cfg', 'r+') as f:
        lines = f.readlines()
        lines[3] = f"version = {'.'.join([str(x) for x in VERSION])}\n"

        with open('../../setup.cfg', 'w') as r:
            r.writelines(lines)
