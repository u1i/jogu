from bottle import Bottle, request, response, route
import subprocess, random, io

app = Bottle()

@app.error(404)
def error404(error):
    return "Nothing here, sorry :("

@app.route('/api/pdf', method='POST')
def create_from_html():

    r = str(random.randint(1000,9999))
    f = "/tmp/" + r + ".html"
    with io.open(f, 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(request.body.read()))
    outfile.close()

    pdf = "/tmp/" + r + ".pdf"
    output = subprocess.check_output(['wkhtmltopdf', f, pdf])

    with open(pdf, mode='rb') as file_handle:
        file_content = file_handle.read()
    file_handle.close()

    response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
    response.headers['Content-Disposition'] = 'attachment; filename="test.pdf"'

    return file_content

@app.get('/swagger')
def swagger():

	swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "",
        "title": "jogu",
        "description": "Create PDFs from HTML input"
    },
    "basePath": "/api",
    "paths": {
        "/pdf": {
            "post": {
                "operationId": "POST_pdf",
                "summary": "Create PDF",
                "tags": [
                    "PDF"
                ],
                "description": "Input some HTML (including images, CSS and all!) and get a PDF.",
                "consumes": [
                    "text/html"
                ],
                "produces": [
                    "application/pdf"
                ],
                "responses": {
                    "default": {
                        "description": "",
                        "schema": {}
                    }
                }
            }
        }
    },
    "definitions": {}
}'''
	return swagger
