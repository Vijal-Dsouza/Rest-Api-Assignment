from db_config import db

class Customer(db.Model):
    __tablename__ = 'customers'
    CustomerID = db.Column(db.String(5), primary_key=True)
    CompanyName = db.Column(db.String(40))
    ContactName = db.Column(db.String(30))
    ContactTitle = db.Column(db.String(30))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))


class Product(db.Model):
    __tablename__ = 'products'
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(40))
    SupplierID = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer)
    QuantityPerUnit = db.Column(db.String(20))
    UnitPrice = db.Column(db.Numeric(10, 2))
    UnitsInStock = db.Column(db.SmallInteger)
    UnitsOnOrder = db.Column(db.SmallInteger)
    ReorderLevel = db.Column(db.SmallInteger)
    Discontinued = db.Column(db.Boolean)


class Order(db.Model):
    __tablename__ = 'orders'
    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.String(5), db.ForeignKey('customers.CustomerID'))
    EmployeeID = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime)
    RequiredDate = db.Column(db.DateTime)
    ShippedDate = db.Column(db.DateTime)
    ShipVia = db.Column(db.Integer)
    Freight = db.Column(db.Numeric(10, 2))
    ShipName = db.Column(db.String(40))
    ShipAddress = db.Column(db.String(60))
    ShipCity = db.Column(db.String(15))
    ShipRegion = db.Column(db.String(15))
    ShipPostalCode = db.Column(db.String(10))
    ShipCountry = db.Column(db.String(15))

    customer = db.relationship('Customer', backref='orders')
