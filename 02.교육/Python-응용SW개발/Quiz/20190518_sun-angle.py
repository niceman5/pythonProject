# 1시간 15도
# 1분 0.25도
# 12-180도

# import dateutil.parser

def sun_angle(time):
    dt = time.split(':')
    # print(dt)
    value = int(dt[0]) * 60 + int(dt[1])
    # print(value)
    if value < 360 or value > 1080:
        time = "I don't see the sun!"
    else:
        time = (value - 360) * 0.25
    # print('time:', time)
    return time

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")