import pathlib


WORKPATH = pathlib.Path(__file__).parent.parent.parent


def resolve_path(file_path: str) -> str:
    match WORKPATH.name:
        case "mediascraper": return str(WORKPATH) + file_path
        case _: return f".{file_path}"


def get_version():

    with open(resolve_path('/version.txt'), 'r+') as f:
        tmp = f.read().split('.')
    return [int(x) for x in tmp]


VERSION = get_version()


if __name__ == '__main__':
    VERSION[1] = VERSION[1] + 1

    with open(resolve_path('/version.txt'), 'w') as d:
        d.write('.'.join(map(str, VERSION)))

    with open(resolve_path('/setup.cfg'), 'r+') as f:
        lines = f.readlines()
        lines[3] = f"version = {'.'.join([str(x) for x in VERSION])}\n"

        with open(resolve_path('/setup.cfg'), 'w') as r:
            r.writelines(lines)
