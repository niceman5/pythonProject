# Precondition:
# '00:00' <= time <= '23:59'

from datetime import time

def time_converter(time_str):
    lst = time_str.split(':')
    # print(lst)
    now = time(int(lst[0]), int(lst[1]))
    if now.hour == 0:
        time_str = '{0}:{1:0>2d}'.format(12, now.minute) + ' a.m.'
    elif now.hour < 12:
        time_str = '{0}:{1:0>2d}'.format(now.hour, now.minute) + ' a.m.'
    elif now.hour == 12:
        time_str = '{0}:{1:0>2d}'.format(now.hour, now.minute) + ' p.m.'
    else:
        new_hour = now.hour - 12
        time_str = '{0}:{1:0>2d}'.format(new_hour, now.minute) + ' p.m.'

    # print('time_str=', time_str)
    return time_str


# def time_converter(time):
#     h, m = map(int, time.split(':'))
#     return f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m."

#
# def time_converter(time):
#     h, m = map(int, time.split(':'))
#     if h < 12:
#         ampm = 'a.m.'
#     else:
#         ampm = 'p.m.'
#     if h > 12:
#         h -= 12
#     elif h == 0:
#         h = 12
#     return '%d:%02d %s' % (h, m, ampm)


# def time_converter(str_time):
#     hours, minutes = map(int, str_time.split(':'))
#     am_or_pm = ['a.m.', 'p.m.'][hours >= 12]
#     return f'{(hours-1) % 12+1}:{minutes:02} {am_or_pm}'
if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")