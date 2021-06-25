-- 1. WHEN ~ THEN 절: 컬럼명에 해당하는 데이터가 조건에 합당할 경우 해당 조건의 결과 반환
-- 2. ELSE 절: 상위 조건에 모두 합당하지 않을 경우 ELSE의 결과 반환

-- 예시
SELECT (CASE test_col WHEN 'A' THEN 1
                      WHEN 'B' THEN 2
                      WHEN 'C' THEN 3
                      ELSE 4
        END) AS test_col
FROM case_test;
