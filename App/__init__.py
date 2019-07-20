import os
from flask import Flask, render_template
from . import database, auth, blog
from App.auth import login_required


def create_app(test_config=None):
   # create and configure the app
   app = Flask(__name__, instance_relative_config=True)
   app.config.from_mapping(
      SECRET_KEY='mysecretkeydevelopmentversion',
      DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
   )

   # Blueprint register's
   database.init_app(app)
   app.register_blueprint(auth.bp)
   app.register_blueprint(blog.bp)
   app.add_url_rule('/', endpoint='index')

   if test_config is None:
      # load the instance config, if it exists, when not testing
      app.config.from_pyfile('config.py', silent=True)
   else:
      # load the test config if passed in
      app.config.from_mapping(test_config)

   # ensure the instance folder exists
   try:
      os.makedirs(app.instance_path)
   except OSError:
      pass

   # a simple page that says hello
   @app.route('/')
   @login_required
   def index():
      return render_template('blog/index.html')

   return app