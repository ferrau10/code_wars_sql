SELECT products.id, products.name, isbn, price, companies.id AS company_id, companies.name AS company_name FROM products LEFT JOIN companies WHERE products.company_id == companies.id

# from the code wars challenge: 
# https://www.codewars.com/kata/5802e32dd8c944e562000020/solutions/sql/me/best_practice


