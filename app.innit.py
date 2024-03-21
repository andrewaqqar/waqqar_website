from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask('waqqar')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://waqqarusername:waqqarpassword@waqqardbserver.postgres.database.azure.com:5432/waqqardb'
app.config['SECRET_KEY'] = 'waqqar_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.waqqar.ae'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'andre@waqqar.ae'
app.config['MAIL_PASSWORD'] = 'waqqar_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'andre@waqqar.ae'

db = SQLAlchemy(app)
mail = Mail(app)

from waqqar include routes
