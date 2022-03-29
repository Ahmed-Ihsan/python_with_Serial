from flask import Flask,jsonify,request
from flask import render_template
import ast
from static import sql_python
import main_port


app = Flask(__name__)
labels = []
values = []

x1, x2, x3 = 0 ,0,0
sql_python.create_SQL(['Ibraheem Thair','Suhaib Mukdad','Sedik Suhaib'], [x1,x2,x3])
def add_point(data,x1_,x2_,x3_):
        if type(data) is int :
                data = str(data)
        if '1' in data or 'ibraheem' in data:
                x1_ += 1
        elif '2' in data or 'suhaib' in data:
                x2_ += 1
        elif '3' in data or 'sedik' in data:
                x3_ += 1
        return x1_ , x2_ , x3_

@app.route("/")
def get_chart_page():
        global labels,values
        return render_template('chart.html', values=values, labels=labels)

@app.route('/refreshData')
def refresh_graph_data():
        global labels, values
        labels =[]
        values = []
        data = sql_python.read_sql()
        for i in data:
                labels.append(i[0])
                values.append(i[1])
        print(labels , values)
        return jsonify(sLabel=labels, sData=values)

@app.route('/updateData/<data>', methods=['GET','POST'])
def update_data(data):
        global labels, values,x1,x2,x3
        print(data)
        x1,x2,x3 = add_point(data,x1,x2,x3)
        sql_python.create_SQL(['Ibraheem Thair','Suhaib Mukdad','Sedik Suhaib'], [x1,x2,x3])
        return "success",201

if __name__ == "__main__":
        app.run(port=5002)
                                            
