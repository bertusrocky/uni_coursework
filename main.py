from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/booking')
@login_required
def booking():
  name = current_user.name
  return render_template('booking.html', name=current_user.name)