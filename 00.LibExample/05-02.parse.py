import sys
import argparse

parser = argparse.ArgumentParser(description="샘플 명령어")
# 문자열을 입력받는 -s option
parser.add_argument('-s', '--string', type=str, help="문자열 표시", required=True)
# 수치를 입력받는 -n option
parser.add_argument('-n', '--num', type=int, help='반복할 숫자를 입력하세요', default=2)

args = parser.parse_args()
print(args)