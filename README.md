# SQL Beginner Challenge #5: Remove Duplicates with DISTINCT

**Difficulty:** Beginner  
**Estimated time:** 5–10 minutes  
**Concepts:** `DISTINCT`, unique values, de-duplication  

This challenge teaches how to remove duplicate values from query results using the `DISTINCT` keyword—a common requirement in reporting and data preparation.

---

## 🧠 The Problem

A product manager asks:

> “Which product categories do we currently have?”

They don’t want a list of products. They want a **unique list of categories**, without duplicates.

---

## 📊 Table Schema

### `products`

| Column Name | Type      | Description |
|------------|-----------|-------------|
| product_id | INTEGER   | Unique product ID |
| name       | TEXT      | Product name |
| category   | TEXT      | Product category |
| price      | DECIMAL   | Product price |
| stock_qty | INTEGER   | Units in stock |
| created_at | TIMESTAMP | Creation timestamp |

---

## 🧪 Sample Data

| product_id | name                 | category     | price  |
|-----------:|----------------------|--------------|-------:|
| 101 | Wireless Mouse      | Accessories | 24.99 |
| 102 | Mechanical Keyboard | Accessories | 89.00 |
| 103 | 27-inch Monitor     | Displays    | 229.99 |
| 104 | USB-C Hub           | Accessories | 34.50 |
| 105 | Laptop Stand        | Workspace   | 39.99 |

---

## ✅ Requirements

Your query must:

- Return a unique list of `category`
- Use the `DISTINCT` keyword
- Return only one column
- Not use `GROUP BY`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here

