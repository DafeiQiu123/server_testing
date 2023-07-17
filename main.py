from flask import Flask, render_template,send_file

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('testing.html')

@app.route('/preview_document')
def preview_document():
    pdf_path = 'static/itin.pdf'
    return send_file(pdf_path, mimetype='application/pdf')

@app.route('/download_document')
def download_document():
    docx_path = 'static/itin.docx'
    return send_file(docx_path, as_attachment=True)
if __name__ == "__main__":
    app.run()


