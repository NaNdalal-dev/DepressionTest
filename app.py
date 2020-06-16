from flask import*
app=Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/',methods=['POST'])
def result():
	res=request.form
	
	if(len(res)==9):
		yes=0
		no=0
		for key,val in res.items():
			print(key,val)
			if(val=='yes'):
				yes+=1
			elif(val=='no'):
				no+=1
		print('yes:',yes)
		print('no:',no)
		if (yes<=3):
			return render_template('index.html',none_='You have mild depression.')
		elif (yes==4):
			return render_template('index.html',little='You have little depression.')
		elif(yes>=5):
			return render_template('index.html',desp='You have high depression.Please consult the doctor')
	else:
		return render_template('index.html',error='Error:You must fill all 8 questions.')
if __name__=='__main__':
	app.run(debug=True)