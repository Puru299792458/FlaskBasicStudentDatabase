from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World"


@app.route('/age/<int:age>')
def show_age(age):
  return 'Age is %d' % age


@app.route('/admin')
def hello_admin():
  return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
  return "Hello %s as Guest"% guest



@app.route('/hi/<name>')
def say_hi(name):
  return "helo %s " % name



if __name__=='__main__':
  app.run()


