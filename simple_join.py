SELECT products.id, products.name, isbn, price, companies.id AS company_id, companies.name AS company_name FROM products LEFT JOIN companies WHERE products.company_id == companies.id

