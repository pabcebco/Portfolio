-- Este código muestra el facturado por Actor y Mes --
-- Para esta querie he empleado el esquema "sakila", preinstalado en MySQL --

USE sakila;
SELECT 
	year(p.payment_date) as Año, month(p.payment_date) as Mes, a.first_name as Nombre, a.last_name as Apellido, SUM(p.amount) as Facturado
FROM actor as a
	JOIN film_actor USING (actor_id)
    JOIN inventory USING (film_id)
    JOIN rental USING (inventory_id)
    JOIN payment as p USING (rental_id)
GROUP BY Año, Mes, a.actor_id
ORDER BY Año, Mes, Facturado DESC
