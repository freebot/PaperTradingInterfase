from flask import Blueprint, render_template, request
from alpaca import createMarketOrder

pages = Blueprint('pages', __name__)

@pages.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        ordertype = request.form.get('ordertype')
        ticker = request.form.get('ticker')
        qty = request.form.get('qty')
        orderside = request.form.get('side')
        if ordertype == 'market':
            createMarketOrder(ticker, qty, orderside, ordertype)
            return render_template('index.html')
        
    return render_template('index.html')