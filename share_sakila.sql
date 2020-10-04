-- Permite calcular la cuota de venta por categoría y mes --
-- Para estas pruebas estoy utilizando el esquema "sakila", preinstalado en MySQL--

SELECT 
	month(p.payment_date) as MES, 
    c.name as CATEGORIA,
    SUM(p.amount) as TOTAL,
    SUM(p.amount)/AVG(TotMes)*100 as SHARE
FROM payment as p
	LEFT JOIN rental USING (rental_id)
	LEFT JOIN inventory USING (inventory_id)
	LEFT JOIN film_category USING (film_id)
	LEFT JOIN category as c USING (category_id)
    LEFT JOIN 
		(SELECT
		month (p2.payment_date) as messq1, 
        SUM(p2.amount) as TotMes
		FROM payment as p2
		GROUP BY month (p2.payment_date) ) as sq1 
        ON month (p.payment_date) = messq1
GROUP BY MES, CATEGORIA
ORDER BY MES, SHARE DESC;
