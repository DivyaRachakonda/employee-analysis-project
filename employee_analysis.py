import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql__Divya15",
    database="employee_analysis"
)

# Average Salary by Department
query = """
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
"""

df = pd.read_sql(query, conn)

print(df)

plt.bar(df["department"], df["avg_salary"])
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()


# Employee Count by Department
query2 = """
SELECT department, COUNT(*) as total
FROM employees
GROUP BY department
"""

df2 = pd.read_sql(query2, conn)

plt.bar(df2["department"], df2["total"])
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.title("Employee Count by Department")
plt.show()


# Average Salary by City
query3 = """
SELECT city, AVG(salary) as avg_salary
FROM employees
GROUP BY city
"""

df3 = pd.read_sql(query3, conn)

plt.bar(df3["city"], df3["avg_salary"])
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.title("Average Salary by City")
plt.xticks(rotation=45)
plt.show()


# Top 10 Employees by Salary
query4 = """
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 10
"""

df4 = pd.read_sql(query4, conn)

print("\nTop 10 Employees by Salary:")
print(df4)


conn.close()