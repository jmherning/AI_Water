from argparse import ArgumentParser, Namespace

from etl_water_mark import main as etl_wm
from water_mark import setup_data_wrapper as setup_data


def mkdata_wrapper(args: Namespace) -> None:
    etl_wm()
    setup_data(args)


if __name__ == '__main__':
    p = ArgumentParser()
    sp = p.add_subparsers()
    # TODO: Come up with a better help description
    mk_data = sp.add_parser('mkdata', help='Make data')
    mk_data.add_argument('size', type=int, help='side of imgaes')
    mk_data.add_argument(
        'environment', help='One word describing the environment'
    )
    mk_data.add_argument('dataset', help='Name of dataset')
    mk_data.add_argument('epoch', help='Neural network for generating masks')
    mk_data.set_defaults(func=mkdata_wrapper)

    args = p.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        p.print_help()
