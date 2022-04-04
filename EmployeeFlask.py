from flask import Flask, render_template

app=Flask(__name__)

@app.route('/Empdetails')
def welcome():
    return render_template("Empdetails.html")
@app.route('/search')
def Gallery_page():
    return render_template("search.html")
@app.route('/update')
def Gallery_page():
    return render_template("update.html")
@app.route('/delete')
def Gallery_page():
    return render_template("delete.html")



if __name__=="__main__":
    app.run()