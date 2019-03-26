# import Module01
import Module02


if __name__ == "__main__":

    try:
        print("Main모듈실행")
        # m = Module01.Module01()
        # m.showName()

        m2 =Module02.Module02()
        m2.showName()
    except Exception as e:
        print(e)
    finally:
        print("종료")

