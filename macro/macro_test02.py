import time, win32con, win32api, win32gui, win32com
import datetime

# win기능 이용하기 위해 먼저 모듈 설치 필요함
# pip install pywin32
# 카톡창 RichEdit20W이였는데 RichEdit50W을 변경됨

# 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)


def kakao_sendtext(chatroom_name, text):

    hwndMain = win32gui.FindWindow(None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RichEdit50W", None)

    # 해당 창을 찾으면 hwndMain 값이 0보다 큼 없으면 0
    # 해당 창을 찾으면 hwndEdit 값이 0보다 큼 없으면 0
    print('hwndMain = %d' % (hwndMain))
    print('hwndEdit = %d' % (hwndEdit))

    if hwndMain <= 0:
        return False

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)
    return True


# 엔터
def SendReturn(hwnd):
    # TODO
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 채팅방 열기
def open_chatroom(chatroom_name: str = ''):
    # 채팅방 목록 검색
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx(hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_2, None, "Edit", None)

    # print('hwndkakao = %d' %(hwndkakao))
    # print('hwndkakao_edit1 = %d' %(hwndkakao_edit1))
    # print('hwndkakao_edit2_1 = %d' %(hwndkakao_edit2_1))
    # print('hwndkakao_edit2_2 = %d' %(hwndkakao_edit2_2))
    # print('hwndkakao_edit3 = %d' %(hwndkakao_edit3))

    # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1)
    SendReturn(hwndkakao_edit3)
    time.sleep(1)


def main():
    lst = [
        '윤진수1', '황정현', '정우현', '문성현 교육팀', '성시하 운영팀',
        '한주희', '운영팀 반정미'
    ]

    # lst = ['황정현','성시하 운영팀']
    text = "카톡발송 테스트 메시지 입니다. 신경쓰지 마세요 {:%Y%m%d_%H:%M:%S}".format(datetime.datetime.now())
    print("start =  {:%Y%m%d_%H:%M:%S}".format(datetime.datetime.now()))

    for cust_nm in lst:
        print('카카오톡 채팅방 열기 = %s' % (cust_nm))
        open_chatroom(cust_nm)
        if kakao_sendtext(cust_nm, text):
            print("발송성공")
        else:
            print("발송실패")

    print("end  =  {:%Y%m%d_%H:%M:%S}".format(datetime.datetime.now()))
    # # 채팅방 열기
    # kakao_title = "윤진수1"
    #

    # ## 채팅전송
    # text = "테스트 메시지 입니다. 신경쓰지 마세요4444"
    # kakao_sendtext(kakao_title, text)

if __name__ == '__main__':
    main()
