#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about nested loops


def main():
    # This function is about nested loops
    loop_number_r = 0
    loop_number_g = 0
    loop_number_b = 0

    # process
    for loop_number_r in range(256):
        for loop_number_g in range(256):
            for loop_number_b in range(256):
                # output
                print(
                    "RGB ({0},{1},{2})".format(
                        loop_number_r, loop_number_g, loop_number_b
                    )
                )

    print("\nDone.")


if __name__ == "__main__":
    main()
