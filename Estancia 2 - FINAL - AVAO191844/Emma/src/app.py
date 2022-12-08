from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL 
from flask_login import LoginManager,login_user,logout_user,login_required
from config import config

#MODELOS --------------------------------
from models.ModelUser import ModelUser

#ENTIDADES -------------------------------
from models.entities.User import User

app = Flask(__name__)

db=MySQL(app)

login_manager_app = LoginManager(app)
@login_manager_app.user_loader

def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def inicio():
    return render_template('iniciar.html')

@app.route('/index')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User(0,request.form['username'],request.form['password'])

        logged_user=ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else: 
                flash("Contraseña Incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/nuevo')
def nuevo():
    return render_template('nuevoUsuario.html')

@app.route('/modificar')
def modificar():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM usuario')
    info = cur.fetchall()
    return render_template('modificarUsuarioF.html',contacts = info)

@app.route('/add_contact', methods =['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contra = request.form['contra']
        cur = db.connection.cursor()
        cur.execute('INSERT INTO usuario (nombre,apellido,contra) VALUES (%s,%s,%s)',(nombre,apellido,contra))
        db.connection.commit()
        flash ('Nuevo usuario, guardado satisfactoriamente')
        return redirect(url_for('nuevo'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE idUsuario = {0}'.format(id))
    info = cur.fetchall()
    return render_template('modificarUsuario.html', contact = info[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contra = request.form['contra']
        cur = db.connection.cursor()
        cur.execute("UPDATE usuario SET nombre = %s, apellido = %s, contra = %s WHERE idUsuario = %s",(nombre,apellido,contra,id))
        db.connection.commit()
        flash('Contacto actualizado satisfactoriamente')
        return redirect(url_for('modificar'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = db.connection.cursor()
    cur.execute('DELETE FROM usuario WHERE idUsuario = {0}'.format(id))
    db.connection.commit()
    flash ('Usuario eliminado satisfactoriamente')
    return redirect(url_for('modificar'))

@app.route('/detector')
def detector():
    return render_template('procesamientoA.html')

@app.route('/protected')
@login_required

def protected():
    return "<h1>Esta es la ruta protegida</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__ == '__main__':  
    app.config.from_object(config['development'])
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run(port = 5000, debug= True)