from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
with open(r"D:\Celebal_practice_flask\model.pkl",'rb') as f:
    model = pickle.load(f)

@app.route("/test", methods = ['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        req_json = request.json
        
        prediction = model.predict(pd.DataFrame(req_json, index=[0]))
        d = ["null"]
        if prediction == 1.0:
            d[0] = "Will Rain Tomorrow" 
        else:
            d[0] = "Will Not Rain Tomorow"    
        return d    


        

        

if __name__ == "__main__":
    app.run(debug=True)
