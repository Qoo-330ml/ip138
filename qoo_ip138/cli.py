from __future__ import annotations

import argparse
import json
from datetime import datetime

from .client import qoo_ip138
from . import __version__


def main() -> int:
    parser = argparse.ArgumentParser(description="qoo-ip138 Python API/CLI")
    parser.add_argument("--ip", type=str, dest="ip", action="store", help="ip address")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    if not args.ip:
        parser.print_help()
        return 1

    result = qoo_ip138(args.ip)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"qoo-ip138 IP 地理信息查询 ver {__version__}")
        for key, value in result.items():
            print(f"{key}: {value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())