from flask import Flask,send_file, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
import os

#import magic
 
app = Flask(__name__)
 
UPLOAD_FOLDER = os.getcwd() + '/uploads/'
 
app.secret_key = "Cairocoders-Ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['json', 'csv', 'xlsx'])
 
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
@app.route('/')
def upload_form():
 return render_template('bdaproject-frontend.html')
 
@app.route('/', methods=['POST'])

def upload_file():
 if request.method == 'POST':
        # check if the post request has the files part
  if 'files[]' not in request.files:
   flash('No file part')
   return redirect(request.url)
  files = request.files.getlist('files[]')
  count =0
  for file in files:
   if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    count+=1
    flash('File(s) successfully uploaded')
  if(count==2):  
    import Script
    val=Script.main()
    if(val==1):
      delete()
  else: 
    flash('Incorrect number of files inputted') 
    
  #return send_from_directory(directory=filepath, filename="filename")
  return redirect('/')

@app.route('/download')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	path = os.getcwd()+"/censored_values.csv"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)

def delete():
  

  import shutil
  uploads_dir=os.getcwd()+"/uploads/"
  
  for filename in os.listdir(uploads_dir):
      file_path = os.path.join(uploads_dir, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              os.unlink(file_path)
          elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))
  
   
if __name__ == '__main__':
 app.run(debug=False)