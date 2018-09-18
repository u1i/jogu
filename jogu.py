from bottle import Bottle, request, response, route
import subprocess, random, io

app = Bottle()

@app.error(404)
def error404(error):
    return "Nothing here, sorry"

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

@app.route('/api/url', method='GET')
def create_from_url():

    url = request.query['url']
    r = str(random.randint(1000,9999))

    pdf = "/tmp/" + r + ".pdf"
    output = subprocess.check_output(['wkhtmltopdf', url, pdf])

    with open(pdf, mode='rb') as file_handle:
        file_content = file_handle.read()
    file_handle.close()

    response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
    response.headers['Content-Disposition'] = 'attachment; filename="' + r +'.pdf"'

    return file_content

@app.route('/form', method="GET")
@app.route('/api/form', method="GET")
def render_form():

    return '''
<h1>HTML to PDF</h1>

<form action="/api/url" method="get">
  URL: <input type="text" name="url" value="http://www.sotong.io"><br>&nbsp;<br>
  <input type="submit" value="Convert and Download">
</form>
    '''

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
        "/form": {
            "get": {
                "operationId": "GET_form",
                "summary": "Form",
                "tags": [
                    "Testing"
                ],
                "description": "Renders a simple form for using the API",
                "responses": {
                    "default": {
                        "description": "",
                        "schema": {}
                    }
                }
            }
        },
        "/pdf": {
            "post": {
                "operationId": "POST_pdf",
                "summary": "Create PDF from HTML",
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
        },
        "/url": {
            "post": {
                "operationId": "POST_url",
                "summary": "Create PDF from URL",
                "tags": [
                    "PDF"
                ],
                "description": "Input a URL and get a PDF.",
                "consumes": [
                    "text/html"
                ],
                "produces": [
                    "application/pdf"
                ],
                "parameters": [
                    {
                        "name": "url",
                        "in": "query",
                        "type": "string"
                    }
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
