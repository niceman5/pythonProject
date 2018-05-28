# try/finally
# 예외 전달하고 싶지만 예외가 발생해도 정리코드를 실행하고 싶을때
# 대표적인 것이 파일 오픈하고 파일 핸들러 제대로 종료하는 작업

handle = open('/tmp/aaa.txt')
try:
    data = handle.read()        #Unicodedecode오류가 날수 있음
finally:
    handle.close()              #try이후 항상실행

#파일을 열때 나오는 에러는 finally블럭에서 처리되지 않아야 함으로 블럭 앞에서 open을 호출해야 한다.



# else블럭
# try블럭이 예외를 일으키지 않으면 else가 실행된다. else블럭을 사용하면 try블럭을 최소한으로 줄일수 있음
def load_json_ley(data, key):
    try:
        result_dic = json.load(data)    # ValueError가 날수 있음
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dic[key]          #KeyError가 날수 있음

# 데이터가 올바른 json데이터가 아니면 오류 발생. 이 예와는 except에서 처리됨. 디코딩이 성공하면 
# else블럭에 가서 key를 찾는다. key를 찾을때 예외가 일어나면 try밖에서 일어남으로 호출 코드까지 
오류가 전달된다.