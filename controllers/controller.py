from app import app
from flask import render_template

from models.game_order import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="GameShop", orders=orders)

@app.route('/orders/<index>')
def single_order(index):
    order = orders[int(index)]
    return render_template('order.html', title="GameShop Order", order=order, floare="lalea")