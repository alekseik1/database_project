WITH RECURSIVE cte AS (
    SELECT MIN(CAST(completed_at AS DATE)) AS dt FROM `Order`
        UNION ALL
    SELECT dt + INTERVAL 1 DAY
        FROM cte
    WHERE dt + INTERVAL 1 DAY <= (SELECT MAX(CAST(completed_at AS DATE)) FROM `Order`)
) SELECT cte.dt, COALESCE(SUM(`Order`.total_sum)/COUNT(DISTINCT `Order`.user_id), 0) as ARPPU
FROM `Order` RIGHT JOIN cte ON CAST(`Order`.completed_at AS DATE) = cte.dt
GROUP BY cte.dt ORDER BY cte.dt;