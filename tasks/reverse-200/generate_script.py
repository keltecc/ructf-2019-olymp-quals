#!/usr/bin/python3

import sys


def generate(flag):
    script = []
    script.append('echo "[*] Hello! Please, enter the flag"; read flag;')

    for i, x in enumerate(flag):
        script.append('if [ "${{flag:{0}:1}}" == "{1}" ]; then'.format(i, x))
    
    script.append('echo "[+] Correct flag :)"; exit 0;')
    script.append('fi; ' * len(flag))
    script.append('echo "[-] Wrong flag :("; exit 1;')
    
    return ' '.join(script)


def main():
    if len(sys.argv) < 2:
        print('usage: {} <your_flag> [esc]'.format(sys.argv[0]))
        sys.exit(-1)

    flag = sys.argv[1]
    script = generate(flag)

    if len(sys.argv) >= 3:
        script = script.replace('"', '\\"')
    
    print(script)


if __name__ == '__main__':
    main()
