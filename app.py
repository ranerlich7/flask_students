from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
STUDENTS = [
    {"name":"Ran", "phone": "050-4445555"},
    {"name":"Or", "phone": "053-9995555"},
    {"name":"Binyamin", "phone": "052-43345555"}]
logged_in_user = ""

@app.route("/", methods=["GET","POST"])
def index():
   global logged_in_user
   message = ""
   if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")
        print(f"user:{user}, password:{password}")
        if user == "ran" and password == "123":
            logged_in_user = user
            return redirect("/students")
        else:       
            message = "Error in login"
   return render_template("index.html", message=message)

@app.route("/students")
def students():    
   if not logged_in_user:
        return redirect("/")
    # check if logged in. if not redirect("/")
   return render_template("students.html", students = STUDENTS, logged_in_user=logged_in_user)

@app.route("/search")
def search():
    search = request.args.get("search")
    phone = request.args.get("phone")
    new_list = []
    print(f"search-{search} phone-{phone}")
    for student in STUDENTS:
        print(f"student-{student}")        
        if search in student["name"] and phone in student["phone"]:
            new_list.append(student)
    # new_list = [student for student in STUDENTS if search in student]   
    print(f"new_list-{new_list}")
    return render_template("students.html", students = new_list, logged_in_user=logged_in_user)


@app.errorhandler(404)
def page_not_found(error):
    # Custom logic for handling 404 errors
    return render_template('404.html'), 404


if __name__ == '__main__':
   app.run(debug=True, port=9000)
