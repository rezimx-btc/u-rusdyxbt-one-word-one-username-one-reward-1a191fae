"""One Word, One Username, One Reward — entry.

Prints our own make.fun username, one word, nothing else.
"""

import os

USERNAME = "rezimx01"  # our own make.fun username: one word, 9 chars, <= 30


def main() -> None:
    print(USERNAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "username.txt"), "w", encoding="utf-8") as f:
            f.write(USERNAME)


if __name__ == "__main__":
    main()
