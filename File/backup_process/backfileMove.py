"""
backup파일을 관리하는 프로세스

[ROOT]의 의 위치에 db백업이 실시간으로 이루어진다.
 - FULL 백업 : DATABASE전체 백업및 로그백업
    --> 1일 1회 : 04시에 전체 배업됨
 - DIFF(차등) 백업 : FULL백업이후의 DB의 증감분만 백업
    --> 1시간마다 실행됨    
 - LOG 백업 : 차등백업이후 transaction의 기록임
    --> 10분단위 실행됨

- 백업복원시 처리방법은 
    마지막일자의 FULL백업 + 
    마지막시간의 DIFF백업 + 
    마집막시간 DIFF이후의 LOG백업들
    
* 백업파일 처리방법
1) 이 배치는 05시에 실행된다    
2) 05시에 현재 04시 FULL백업 이전에 생성된 백업파일들 삭제한다.
3) 현재일의 FULL백업을 일자별 백업에 복사한다.
4) 실행하는 요일이 일욜일이면 일자별백업을 주간백업에 복사한다.
5) 일자별 백업은 일주일치만 유지하고 삭제한다.
6) 주간백업은 4주차만 유지하고 삭제한다.
7) 모든 과정은 LOG파일에 기록을 남긴다.

작성자 : UCRM 김태훈
작성일 : 2023-05-01

수정이력)
"""
import tomllib
import os
import log
import shutil
from datetime import datetime, timedelta
from distutils.dir_util import copy_tree

# 최초 실행시 설정 파일을 읽어서 전역변수 config에 설정한다.
try:
    conf_file = "E:\\pythonProject\\File\\backup_process\\config.toml"
    # conf_file = "D:\\00.Dev\\PythonPorject\\File\\backup_process\\config.toml"        
    with open(conf_file, "rb") as f:    
        config = tomllib.load(f)
except:
    print("설정 파일을 찾울수 없습니다.")
    print("파일 = " + conf_file)
    exit(1)        

# 로그파일을 설정. 로그 생성위치를 지정한다.
logger = log.get_logger(name="BACKUP_MOVE", log_dir=config['LOG']['PATH'])

# main함수
def main():    
    # logger.info(config)              
    logger.info('main_process')
    
    root_path = config['ROOT']['PATH']      # 백업파일이 있는 path
    daily_path = config['DAILY']['PATH']    # 일자별 full 백업이 복사될 path
    weekly_path = config['WEEKLY']['PATH']  # 주간 full 백업이 복사될 path
    base_dt = '{:%Y%m%d}'.format(datetime.now()) + '_040000'    
    
    # test용코드 
    base_dt = '20230502_040000'
    logger.info("backup file path = " + root_path)
    
    # daily 디렉토리가 있는지 검사하고 없으면 생성한다.
    dest_dir = daily_path + "\\" + '{:%Y%m%d}'.format(datetime.now())
    weekly_dir = weekly_path + "\\" + '{:%Y%m%d}'.format(datetime.now())
    if os.path.isdir(dest_dir) == False :
        os.mkdir(dest_dir)           
    
    # 전체 파일 리스트를 구한다.
    file_full_list = os.listdir(root_path)
    file_list = []
    
    # BAK인 목록과 TRN목록을 구해 통합 리스트를 만든다.
    file_list += [file for file in file_full_list if file.endswith(".BAK")]    
    file_list += [file for file in file_full_list if file.endswith(".TRN")]
    # logger.info('전체 파일 리스트 ')
    # logger.info(file_list)
    logger.info('처리 기준일시 :' + base_dt)
    
    for file_name in file_list:        
        name1 = file_name.split("(")
        name2 = name1[1].split(")")
        logger.info("처리대상 파일명 : %s  날짜값 : %s" % (file_name, name2[0]) )
        
        src_file = root_path + "\\" + file_name
        dest_file = dest_dir + "\\" + file_name
        
        # 현재 기준일자 이전의 파일들을 모두 삭제한다.
        if  base_dt > name2[0] :
            try:                
                os.remove()    
            except OSError as e:
                logger.info("File remove Error: %s [%s]" % (src_file, e.strerror))    
                exit(1)
            logger.info("기준일 이전 파일 -> 삭제")
            continue
        
        # 삭제하지 않는 파일중 full백업파일은 일자백업 폴더에 복사한다.
        if file_name.find("_FULL.") > 0 :
            try :                
                shutil.copy2(src_file, dest_file)
            except e:
                logger.info("File Copy Error: %s -> %s [%s]" % (src_file, dest_file, e.strerror))    
                exit(1)
                
            logger.info("full backup file - daily 폴더로 복사")    
    
    # 일단위 백업은 7일치만 유지하게 하고 나머지는 삭제한다.
    # daily 폴더의 일자별 폴더를 읽어 7일경과한 폴더는 삭제한다.
    logger.info("="* 20 + "DAILY 디렉토리 정리" + "="* 20)
    before_one_week = '{:%Y%m%d}'.format(datetime.now() - timedelta(weeks=1))
    logger.info("DAILY 폴더 정리 기준 : " + before_one_week)
    with os.scandir(daily_path) as dirs:
        for dir_name in dirs:
            if before_one_week > dir_name.name:
                logger.info("삭제할 대상 폴더 :" + dir_name.name)
                try:
                    shutil.rmtree(daily_path + "\\" + dir_name.name)
                except e:
                    logger.info("폴더 삭제 Error: %s [%s]" % (daily_path + "\\" + dir_name.name, e.strerror))    
                    exit(1)         
                logger.info("삭제할 완료!!")
    
    # 이 프로그램이 실행하는 요일이 일요일이면 주간 백업에 일자 폴더를 복사하고 주간백업은 4주차만 유지한다.
    # 월요일 : 0 ~ 일요일 6
    if datetime.now().weekday() == 6:
        logger.info("="* 20 + "WEEKLY 디렉토리 정리" + "="* 20)
        before_four_week = '{:%Y%m%d}'.format(datetime.now() - timedelta(weeks=4))
        logger.info("WEEKLY 폴더 정리 기준 : " + before_four_week)
                
        try:
            copy_tree(dest_dir, weekly_dir )
        except e:
            logger.info("weekly 폴더 복사 Error: %s -> %s  [%s]" % (dest_dir, weekly_dir, e.strerror))    
            exit(1)         
        logger.info("주간 폴더 복사 완료!!")        
        
        # 4주이상 경과한 폴더를 삭제한다. 
        with os.scandir(weekly_path) as dirs:
            for dir_name in dirs:
                logger.info(dir_name.name)        
                if before_four_week > dir_name.name:
                    logger.info("삭제할 대상 폴더 :" + dir_name.name)
                    try:
                        shutil.rmtree(weekly_path + "\\" + dir_name.name)
                    except e1:
                        logger.info("폴더 삭제 Error: %s [%s]" % (weekly_path + "\\" + dir_name.name, e1.strerror))    
                        exit(1)         
                    logger.info("삭제할 완료!!")        

# main 시작점을 시작하게 한다.
if __name__ == "__main__":    
	main() 