#!/usr/bin/env python3
"""Normalize basic Azerbaijan legal citation fields into a compact string."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Format a compact Azerbaijan legal citation.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--article")
    parser.add_argument("--number")
    parser.add_argument("--date")
    parser.add_argument("--version")
    parser.add_argument("--url")
    args = parser.parse_args()

    parts = [args.title]
    if args.number:
        parts.append(f"No. {args.number}")
    if args.date:
        parts.append(args.date)
    if args.article:
        parts.append(f"Art./Sec. {args.article}")
    if args.version:
        parts.append(f"version/amended through {args.version}")
    if args.url:
        parts.append(args.url)

    print(", ".join(parts) + ".")


if __name__ == "__main__":
    main()
