import time, win32con, win32api, win32gui, win32com

# win기능 이용하기 위해 먼저 모듈 설치 필요함
# pip install pywin32
# 카톡창 RichEdit20W이였는데 RichEdit50W을 변경됨

# # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
kakao_title = "윤진수"

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

## 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    
## 핸들 
hwndMain = win32gui.FindWindow(None, kakao_title)    
hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RichEdit50W", None)
hwndListControl = win32gui.FindWindowEx(hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

print(hwndMain)
print(hwndEdit)
print(hwndListControl)

## 채팅전송
text = "테스트 메시지 입니다. 신경쓰지 마세요"
kakao_sendtext(text)

