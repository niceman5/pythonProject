/*
조직 정보를 가지고 있는 원본 테이블 <표 1>로부터 계층구조 형태로 표현한 <표 2>의 결과를 출력하는 SQL을 작성하세요.
*/

DECLARE @TMP_LIST TABLE
(
	cd		CHAR(2)
,	nm		VARCHAR(100)
,	pcd		CHAR(2)
,	flg		INT
,	ord		INT
);

WITH dept(cd, nm, pcd, flg, ord) AS
(
	SELECT 10, '구루비닷넷', null, 1, 1			--FROM dual
	UNION ALL SELECT 11, '직할'    , 10, 0, 1	--FROM dual
	UNION ALL SELECT 12, '감사팀'  , 11, 1, 1	--FROM dual
	UNION ALL SELECT 13, '기획처'  , 10, 1, 2	--FROM dual
	UNION ALL SELECT 14, '기획팀'  , 13, 1, 1	--FROM dual
	UNION ALL SELECT 15, '총무팀'  , 13, 1, 2	--FROM dual
	UNION ALL SELECT 16, '영업처'  , 10, 1, 3	--FROM dual
	UNION ALL SELECT 17, '영업1팀' , 16, 1, 1	--FROM dual
	UNION ALL SELECT 18, '영업2팀' , 16, 1, 2	--FROM dual
	UNION ALL SELECT 19, '사업소'  , 10, 0, 4	--FROM dual
	UNION ALL SELECT 20, '서울지점', 19, 1, 1	--FROM dual
	UNION ALL SELECT 24, '관할'    , 20, 0, 1	--FROM dual
	UNION ALL SELECT 21, '관리파트', 24, 1, 1	--FROM dual
	UNION ALL SELECT 22, '개발파트', 24, 1, 2	--FROM dual
	UNION ALL SELECT 23, '부산지점', 19, 1, 2	--FROM dual
)
INSERT INTO @TMP_LIST
SELECT * FROM dept;

/*
<리스트 1>은 구루비닷넷이라는 회사의 조직정보(DEPT) 테이블입니다. 이 조직정보 테이블에는 조직코드(CD), 조직명(NM), 상위조직코드(PCD), 실조직여부(FLG), 조직서열(ORD) 
정보가 저장돼 있습니다. 상위조직코드는 조직코드를 참조하는 자기 참조 구조입니다. 이 자기 참조 구조를 이용해 <표 2>의 조직도를 출력하는 문제입니다. 그런데 조직 
중에는 실제 존재하지 않는 가조직이 포함돼 있습니다. 가조직은 팀 단위 부서(팀/지점)의 조직 레벨은 통일하기 위해 관리되고 있는 정보입니다. 
<표 1>에서 직할, 사업소, 관할 등이 여기에 해당합니다. 실조직여부 항목에서 1은 실조직을, 0은 가조직을 의미합니다. 가조직은 시스템 관리상의 
목적으로 만들어진 조직이므로, 실제 조직도에는 있어서는 안 됩니다.

조직도는 사용자가 보기 좋도록 조직 레벨과 부모조직코드를 함께 표시합니다. 조직명의 경우에는 조직레벨에 맞게 들여쓰기 형태로 ‘└’ 기호와 
함께 표시돼야 합니다. 또한 조직도는 조직서열에 따라 순서대로 출력돼야 합니다. 지금부터 계층쿼리를 이용해 이 문제를 풀어볼까요.
*/
SELECT * FROM @TMP_LIST