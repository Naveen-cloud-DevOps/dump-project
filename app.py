from flask import Flask, request, jsonify, render_template_string
import mysql.connector

# Your existing DB config
db_config = {
    'host': 'veera.c5awqomecj30.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Cloud123',
    'database': 'dev'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/submit-order', methods=['POST'])
def submit_order():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    product = request.args.get('product')

    if not name or not email or not address or not product:
        return "Missing fields", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO orders (name, email, address, product) VALUES (%s, %s, %s, %s)",
            (name, email, address, product)
        )
        conn.commit()
        return redirect(f"/success?product={product}")
    except Exception as e:
        return f"Database error: {str(e)}", 500
    finally:
        cursor.close()
        conn.close()
