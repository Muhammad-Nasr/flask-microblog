from app import db
from app.errors import errors
from flask import render_template


@errors.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@errors.errorhandler(500)
def internal_error(error):

    db.session.rollback()
    return render_template('errors/500.html'), 500