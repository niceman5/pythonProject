
# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

file = open('D:\\PythonProject\\Project\\day20190504\\new.txt', 'w')

file.write("hahahaha\n")
file.write("hohohoho\n")
file.write("가나다")


file.close()
print('success!!!!')
