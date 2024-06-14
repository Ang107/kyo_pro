import sys


def main(lines: list[str]):
    s, t = lines[0].split()
    s_split_slash = s.split("/")
    t_split_slash = t.split("/")
    same_dir_cnt = 0
    for i, j in zip(s_split_slash, t_split_slash):
        if i == j:
            same_dir_cnt += 1
        else:
            break
    s_split_slash = s.split("/")
    ans = (len(s) - same_dir_cnt) + (len(t) - same_dir_cnt)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
