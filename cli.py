from datetime import timedelta
from flow_client import settings, sig_gen
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("-n", "--name", help="name of flow")
    parser.add_argument("-u", "--url", help="flow url")
    parser.add_argument("-d", "--days", type=float, help="num days is sig is valid")
    parser.add_argument(
        "-s", "--seconds", type=float, help="num seconds is sig is valid"
    )

    args = parser.parse_args()

    if args.seconds is None and args.days is None:
        print("using default duration")
        valid_for = settings.VALID_FOR
    else:
        print(f"days is {args.days} and seconds is {args.seconds}")
        valid_for = timedelta(
            days=0 if args.days is None else args.days,
            seconds=0 if args.seconds is None else args.seconds,
        )

    if args.name is not None:
        if args.name not in settings.FLOWS:
            print("no such flow")
            exit()
        url = settings.FLOWS[args.name]
    elif args.url is not None:
        url = args.url
    else:
        name = next(iter(settings.FLOWS.keys()))
        print(f"defaulting to {name}")
        url = settings.FLOWS[name]

    request = sig_gen.gen_sig_url(url, valid_for)
    print(request.url)


if __name__ == "__main__":
    main()
