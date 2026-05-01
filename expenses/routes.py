from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from action_db import get_user_expenses, add_new_expense
import random

expenses_bp = Blueprint('expenses', __name__, template_folder='templates')
START_BAL = 500000.00

@expenses_bp.route('/index')
@login_required
def index():
    user_expenses = get_user_expenses(current_user)
    total_spent = sum(e.amount for e in user_expenses)
    remaining = START_BAL - total_spent
    labels = [e.item for e in user_expenses]
    values = [e.amount for e in user_expenses]
    rates = {'USD': round(random.uniform(39, 41), 2), 'EUR': round(random.uniform(42, 44), 2)}
    return render_template('index.html', total=remaining, expenses=user_expenses,
                           labels=labels, values=values, start_bal=START_BAL, rates=rates)

@expenses_bp.route('/add', methods=['POST'])
@login_required
def add_expense():
    item = request.form.get('item')
    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    add_new_expense(item, amount, category, current_user)
    return redirect(url_for('expenses.index'))