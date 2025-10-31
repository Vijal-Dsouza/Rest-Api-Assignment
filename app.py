from flask import request, jsonify
from db_config import app, db
from models import Customer, Product, Order
from datetime import datetime

# ---------------------- Customers ----------------------
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    new_customer = Customer(**data)
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer added successfully"}), 201


@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(customer, key, value)
    db.session.commit()
    return jsonify({"message": "Customer updated successfully"})


@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify({col.name: getattr(customer, col.name) for col in customer.__table__.columns})


# ---------------------- Products ----------------------
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"})


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({col.name: getattr(product, col.name) for col in product.__table__.columns})


# ---------------------- Orders ----------------------
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    data['OrderDate'] = datetime.now()
    new_order = Order(**data)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order added successfully"}), 201


@app.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(order, key, value)
    db.session.commit()
    return jsonify({"message": "Order updated successfully"})


@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({col.name: getattr(order, col.name) for col in order.__table__.columns})


# ---------------------- Order History ----------------------
@app.route('/order_history/<customer_id>', methods=['GET'])
def get_order_history(customer_id):
    orders = Order.query.filter_by(CustomerID=customer_id).all()
    if not orders:
        return jsonify({"error": "No orders found for this customer"}), 404
    result = []
    for order in orders:
        result.append({
            "OrderID": order.OrderID,
            "OrderDate": order.OrderDate,
            "RequiredDate": order.RequiredDate,
            "ShippedDate": order.ShippedDate,
            "ShipCountry": order.ShipCountry
        })
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
