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
   user = request.form.get("username")
   password = request.form.get("password")
   print(f"user:{user}, password:{password}")
   if user == "ran" and password == "123":
       logged_in_user = user
       return redirect("/students")
   return render_template("index.html")

@app.route("/students")
def students():    
   if not logged_in_user:
        return redirect("/")
    # check if logged in. if not redirect("/")
   return render_template("students.html", students = STUDENTS, logged_in_user=logged_in_user)

@app.route("/search")
def search():
    search = request.args.get("search")
    new_list = []
    print(f"search-{search}")
    for student in STUDENTS:
        print(f"student-{student}")

        if search in student["name"]:
            new_list.append(student)
    # new_list = [student for student in STUDENTS if search in student]   
    print(f"new_list-{new_list}")
    return render_template("students.html", students = new_list, logged_in_user=logged_in_user)

if __name__ == '__main__':
   app.run(debug=True, port=9000)
