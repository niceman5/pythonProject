""" 숫자형 관련 확장함수
"""


def get_first_int(values, key, default=0):
    """dict에 있는 key값을 검색해서 있으면 해당 값을 리턴하고 없으면 default값을 return

    Args :
        values  : 대상 dict
        key : 찾으려는 key
        default : 기본 리턴값

    Returs :
        dict에 있는 기본 key에 value값을 리턴. 없으면 default값을 리턴

    """
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
