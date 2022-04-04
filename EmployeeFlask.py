from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def hello():
    return "Hello"
@app.route('/Empdetails')
def welcome():
    return render_template("Empdetails.html")
# @app.route('/search')
# def search_page():
#     return render_template("search.html")
# @app.route('/update')
# def update_page():
#     return render_template("update.html")
# @app.route('/delete')
# def delete_page():
#     return render_template("delete.html")



if __name__=="__main__":
    app.run()