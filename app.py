from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)

# Secret key for session management (Flask needs this for security)
app.secret_key = 'your_secret_key'

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'cake123'

# Read orders from JSON file
def read_orders():
    with open('orders.json', 'r') as file:
        return json.load(file)

# Write orders back to the JSON file
def write_orders(orders):
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

# Home route (admin login page)
@app.route('/')
def login_page():
    return render_template('admin-login.html')

# Admin login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return redirect(url_for('status_page'))  # Redirect to status page on successful login
    else:
        flash('Wrong username or password')  # Flash message if login fails
        return redirect(url_for('login_page'))  # Redirect back to login page

# Status page route
@app.route('/status')
def status_page():
    orders = read_orders()  # Get all orders from orders.json
    return render_template('status.html', orders=orders)

# Route to update order status
@app.route('/update_status/<int:order_id>', methods=['POST'])
def update_status(order_id):
    new_status = request.form['status']  # Get the new status from the form
    orders = read_orders()  # Get the list of orders

    # Find the order by ID and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = new_status
            break

    write_orders(orders)  # Save the updated orders back to the file
    return redirect(url_for('status_page'))  # Redirect back to the status page

if __name__ == '__main__':
    app.run(debug=True)
