from flask import Flask, request, jsonify, make_response
from models import db, User, Expense
import csv
from io import StringIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('name') or not data.get('mobile'):
        return jsonify({'message': 'Invalid input'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(email=data['email'], name=data['name'], mobile=data['mobile'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or not data.get('description') or not data.get('amount') or not data.get('user_id') or not data.get('split_method') or not data.get('split_details'):
        return jsonify({'message': 'Invalid input'}), 400

    if not User.query.get(data['user_id']):
        return jsonify({'message': 'User not found'}), 404

    if data['split_method'] == 'Percentage' and sum(data['split_details'].values()) != 100:
        return jsonify({'message': 'Percentages must add up to 100'}), 400

    new_expense = Expense(description=data['description'], amount=data['amount'], user_id=data['user_id'], split_method=data['split_method'], split_details=data['split_details'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'}), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'email': user.email, 'name': user.name, 'mobile': user.mobile}), 200

@app.route('/expense/user/<int:user_id>', methods=['GET'])
def get_user_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([{'description': expense.description, 'amount': expense.amount, 'split_method': expense.split_method, 'split_details': expense.split_details} for expense in expenses]), 200

@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    expenses = Expense.query.all()
    return jsonify([{'description': expense.description, 'amount': expense.amount, 'user_id': expense.user_id, 'split_method': expense.split_method, 'split_details': expense.split_details} for expense in expenses]), 200

@app.route('/balance_sheet', methods=['GET'])
def download_balance_sheet():
    expenses = Expense.query.all()
    balance_sheet = []

    for expense in expenses:
        user = User.query.get(expense.user_id)
        balance_sheet.append({
            'user': user.name,
            'email': user.email,
            'description': expense.description,
            'amount': expense.amount,
            'split_method': expense.split_method,
            'split_details': expense.split_details
        })

    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['User', 'Email', 'Description', 'Amount', 'Split Method', 'Split Details'])
    cw.writerows([(row['user'], row['email'], row['description'], row['amount'], row['split_method'], row['split_details']) for row in balance_sheet])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == '__main__':
    app.run(debug=True)
