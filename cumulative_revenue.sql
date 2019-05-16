WITH RECURSIVE cte AS (
    SELECT MIN(CAST(completed_at AS DATE)) AS dt FROM `Order`
        UNION ALL
    SELECT dt + INTERVAL 1 DAY
        FROM cte
    WHERE dt + INTERVAL 1 DAY <= (SELECT MAX(CAST(completed_at AS DATE)) FROM `Order`)
), revenue AS (
    SELECT cte.dt, COALESCE(SUM(total_sum), 0) AS money
    FROM cte LEFT JOIN `Order` ON cte.dt = CAST(completed_at AS DATE)
    GROUP BY cte.dt
    ORDER BY cte.dt
) SELECT dt, money,
         SUM(money) OVER (PARTITION BY month(dt) ORDER BY dt) as total_money
FROM revenue;
