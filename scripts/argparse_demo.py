#!/usr/bin/env python3
import argparse
import json
import sys

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Demo argparse that prints parsed args and unknown args."
    )

    # Example args – add/remove as you wish
    parser.add_argument("--name", required=True, help="Your name")
    parser.add_argument("--env", choices=["dev", "uat", "prod"], default="dev", help="Environment")
    parser.add_argument("--count", type=int, default=1, help="A number")
    parser.add_argument("--payload-json", help="JSON string payload")

    # Parse known + capture unknown
    known_args, unknown_args = parser.parse_known_args(argv)

    # Pretty print
    print("=== Known args ===")
    print(json.dumps(vars(known_args), indent=2, sort_keys=True))

    print("\n=== Unknown args (leftover tokens) ===")
    print(json.dumps(unknown_args, indent=2))

    # If payload-json was provided, try to decode to show it’s valid JSON
    if known_args.payload_json:
        print("\n=== Decoded payload-json ===")
        try:
            obj = json.loads(known_args.payload_json)
            print(json.dumps(obj, indent=2, sort_keys=True))
        except json.JSONDecodeError as e:
            print(f"(warning) payload-json is not valid JSON: {e}")

if __name__ == "__main__":
    main()
