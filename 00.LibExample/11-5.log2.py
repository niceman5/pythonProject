import logging
import logging.config
import json
import os
from pathlib import Path

if __name__ == '__main__':
    
    file_dir = 'C:\\DATA\\Study\\pythonProject\\00.LibExample\\file'
    fullname = os.path.join(file_dir,'logging.json')

    print(fullname)
    with open(fullname, 'rt') as f:
        config = json.load(f)

    logging.config.dictConfig(config)
    
    # config파일을 통해 설정을 불러 로그 기록
    # 화면과 파일에 출력한다.
    
    logger = logging.getLogger()
    logger.info("test!!!")

