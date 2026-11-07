import sqlite3
import pandas as pd
conn = sqlite3.Connection('data.sqlite')

# # ------------ Substituting JOIN with Subqueries ------------ 
# query1 = """
# SELECT lastName, firstName, officeCode
# FROM employees
# JOIN offices
#     USING(officeCode)
# WHERE country = "USA"
# """
# print(pd.read_sql(query1, conn))

# # Using subquery instead of join
# query2 = """
# SELECT lastName, firstName, officeCode
# FROM employees
# WHERE officeCode IN (SELECT officeCode
#                      FROM offices
#                      WHERE country = "USA")
# """
# print(pd.read_sql(query2, conn))

# # ------------ Subqueries for Filtering Based on Aggregation ------------ 
# query3 = """
# SELECT lastName, firstName, officeCode
# FROM employees
# WHERE officeCode IN (
#         SELECT officeCode
#         FROM offices
#         JOIN employees
#             USING(officeCode)
#         GROUP BY 1
#         HAVING COUNT(employeeNumber) >= 5
# )
# """
# print(pd.read_sql(query3, conn))


# # ------------ Chaining Aggregates ------------ 
# query4 = """
# SELECT AVG(customerAvgPayment) AS averagePayment
# FROM (
#     SELECT AVG(amount) AS customerAvgPayment
#     FROM payments
#     JOIN customers
#         USING(customerNumber)
#     GROUP BY customerNumber
# )
# """
# print(pd.read_sql(query4, conn))

# ------------ Foreign Key Reference ------------ 
query5 = """
SELECT lastName, firstName, employeeNumber
FROM employees
WHERE employeeNumber IN (
        SELECT salesRepEmployeeNumber
        FROM customers
        WHERE country = "USA"
)
"""
print(pd.read_sql(query5, conn))

conn.close()