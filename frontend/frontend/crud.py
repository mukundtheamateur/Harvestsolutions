from flask import *  
import sqlite3  


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None
        
         
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html");  
 
@app.route("/add")  
def add():  
    return render_template("add.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            phonenumber = request.form["phonenumber"]  
            adharnumber = request.form["adharnumber"]  
            area = request.form["area"]  
            cropg = request.form["cropg"]  
            cropr = request.form["cropr"]  
            nitrogen = request.form['nitrogen']
            phosphorous = request.form['phosphorous']
            pottasium = request.form['pottasium']
            ph = request.form['ph']
            rainfall = request.form['rainfall']
            state = request.form['state']
            city = request.form['city']
            # city = request.form.get("city")
            # temperature, humidity = weather_fetch(city)
            with sqlite3.connect("fdetail.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into FDetails (name, phonenumber, adharnumber, area, cropg, cropr, nitrogen, phosphorous, pottasium, ph, rainfall, state, city) values (?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,phonenumber,adharnumber,area,cropg,cropr,nitrogen,phosphorous,pottasium,ph,rainfall,state,city))  
                con.commit()  
                msg = "Data successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("fdetail.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from FDetails")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 
 
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("fdetail.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from FDetails where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  
  
if __name__ == "__main__":  
    app.run(debug = True)  