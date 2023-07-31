from flask import Flask, render_template, request
import requests
import smtplib


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)





my_email = "navinfeb15@gmail.com"
password = "jcaoopqflfpnaoei"
to_email = "navinfeb15@gmail.com"

            
            
@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST','GET'])
def contact():
    if request.method == "POST":
        
        message = f'''
            Name : {request.form['name']}
            Email : {request.form['email']}
            Phone : {request.form['phone']}
            Message : {request.form['message']}
            '''
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=to_email, msg=message)
            
        return render_template("contact.html", submitted=True)
    
    elif request.method == "GET":
        return render_template("contact.html", submitted=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)








if __name__ == "__main__":
    app.run(debug=True, port=5001)


