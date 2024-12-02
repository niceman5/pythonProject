"""문자열관련된 확장함수
"""
def to_str(bytes_or_str):
    """ 외부 프로그램이나 데이터에서 str이나 byte는 입력받아 pythn에서 사용하는 기본 코드인 utf-8로 변경
    
    Args :
        bytes_or_str  : 외부 프로그램이나 데이터를 통해 받은 문자열
        
    Returs : 
        str 인스턴스
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str    
    return value    

def to_bytes(bytes_or_str):
    """ 외부 프로그램이나 데이터에서 str이 아닌 문자열 주고 받을때 bytes형태로 변환
    
    Args :
        bytes_or_str  : 외부 프로그램이나 데이터를 통해 받은 문자열
        
    Returs : 
        bytes 인스턴스
    """    
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str    
    return value

def get_first_str(values, key, default=''):
    """dict에 있는 key값을 검색해서 있으면 해당 값을 리턴하고 없으면 default값을 return
    
    Args :
        values  : 대상 dict
        key :찾으려는 key
        default : 기본 리턴값
        
    Returs : 
        dict에 있는 기본 key에 value값을 리턴. 없으면 default값을 리턴
    
    """
    found = values.get(key, [''])
    if found[0] :
        found = found[0]
    else:
        found = default
    return found