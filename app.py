from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for checkout page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Route for success page
@app.route('/success')
def success():
    return render_template('success.html')

# Optional: Handle form POST
@app.route('/submit-order', methods=['POST'])
def submit_order():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    # Optional: Save to database
    product = request.args.get('product')  # Pass product if needed
    return redirect(url_for('success', product=product))  # Redirect with product

if __name__ == '__main__':
    app.run(debug=True)
