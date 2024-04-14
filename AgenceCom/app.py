from flask import Flask, render_template, url_for, request, session, redirect
from flask_bcrypt import Bcrypt
from employees.employee import Employee
from employees.employee_dao import EmployeeDao
from departments.department import Department
from departments.department_dao import DepartmentDao
from users.user import User
from users.user_dao import UserDao


app = Flask(__name__)
app.secret_key='secretkey'
bcrypt = Bcrypt(app) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    message=None
    user=None
    req = request.form
    if request.method == "POST":
        full_name = req['full_name']
        username = req['username']
        password = req['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        if full_name=="" or username=="" or password=="":
            message="error"
        else:
            user = User(full_name,username,hashed_password)
            message = UserDao.create(user)
        #print(message)
    return render_template(f'register.html', message=message,user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    req= request.form
    message = None
    user = None
    if request.method == "POST":
        username = req['username']
        password = req['password']
        if username == '' or password == '':
            message = 'error'
        else:
            (message,user) =  UserDao.get_one(username,password)
            if message=='Success' and user != None:
                if bcrypt.check_password_hash(user[3], password):
                    session['username'] = user[2]
                    session['full_name'] = user[1]
                    return redirect(url_for('home'))
                else:
                    message = 'Username or password is incorrect.'
            else:
                message = 'Username or password is incorrect.'
        print(message)
            
    return render_template("login.html",message=message,user=user)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/employee")
def employees():
    if 'username' not in session:
        return redirect(url_for('login'))
    employees = EmployeeDao.get_all()
    return render_template("employe.html", employees=employees)

@app.route("/add-employee",methods=["POST","GET"])
def add_employee():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message = None
    employee = None
    if request.method == "POST":
        last_name = req['last_name']
        first_name = req['first_name']
        badge_number = req['badge_number']
        position = req['position']
        department = req['department']
        
        if last_name=="" or first_name=="" or badge_number=="" or position=="" or department=="":
            message="error"
        else:
            employee = Employee(last_name,first_name,badge_number,position,department)
            message = EmployeeDao.add(employee)
        #print(message)
    return render_template("add_employe.html",employee=employee,message=message)

@app.route("/departments")
def departments():
    if 'username' not in session:
        return redirect(url_for('login'))
    departments = DepartmentDao.list_all()
    return render_template("departments.html", departments=departments)

@app.route("/add-departments",methods=["POST","GET"])
def add_departments():
    req = request.form
    message = None
    department = None
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        name = req['name']
        location = req['location']
        head = req['head']
        if name=="" or location=="" or head=="":
            message="error"
        else:
            department = Department(name,location,head)
            message = departmentDao.create(department)
    return render_template("add_departments.html",message=message,department=department)