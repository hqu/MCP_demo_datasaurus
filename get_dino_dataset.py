from __future__ import annotations

import json
from urllib.request import urlopen


API_URL = "https://hqu.github.io/MCP_demo_datasaurus/api/datasets/dino.json"


def main() -> None:
    with urlopen(API_URL, timeout=20) as response:
        data = json.load(response)

    print(f"Dataset: {data['dataset']}")
    print(f"Point count: {data['summary']['count']}")
    print(f"X range: {data['summary']['x']['min']} to {data['summary']['x']['max']}")
    print(f"Y range: {data['summary']['y']['min']} to {data['summary']['y']['max']}")
    print("First five points:")

    for point in data["points"][:5]:
        print(f"  x={point['x']}, y={point['y']}")


if __name__ == "__main__":
    main()
