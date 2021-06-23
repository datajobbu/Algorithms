-- 입양 시각 구하기(2)

-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 시간대 순으로 정렬해야 합니다.

WITH RECURSIVE TIME AS (
    SELECT 0 AS h
    UNION ALL
    SELECT h+1
    FROM time 
    WHERE h < 23
)
SELECT h AS "HOUR", COUNT(datetime) AS "COUNT"
FROM time
LEFT JOIN animal_outs ON h = hour(datetime)
GROUP BY h
ORDER BY h;