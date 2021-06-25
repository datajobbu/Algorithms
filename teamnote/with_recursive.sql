-- 1. 메모리 상에 가상의 테이블을 저장
-- 2. 재귀 커리를 이용하여 실제로 테이블을 생성하거나 데이터 삽입을 하지 않아도
--    가상 테이블을 생성할 수 있음.

-- 예시
WITH RECURSIVE cte AS (
    SELECT 1 AS h
    UNION ALL
    SELECT h+1 FROM cte WHERE h<5
)

SELECT * FROM cte;

