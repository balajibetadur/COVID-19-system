from flask import Flask,render_template,request
app = Flask(__name__)
import pickle



file1=open('model.pkl','rb')
clf = pickle.load(file1)
file1.close()

@app.route('/',methods=["GET","POST"])
def prob():
    if request.method=="POST":
        # try:
            fe=request.form
            fever2=float(fe['fever'])
            fever=round(fever2)
            age=int(fe['age'])
            pain=int(fe['pain'])
            nose=int(fe['nose'])
            breath=int(fe['breath'])

            user_input=[[fever,age,pain,nose,breath]]
            prob3=clf.predict(user_input)
            
            return render_template('result.html',o_inf=o_inf)
        # except:
        #     return render_template('index.html')
            
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
