![](https://raw.githubusercontent.com/u1i/jogu/master/img/jlogo_small.png)

# jogu - The Letterpress API

### Send HTML ...
`curl -o out.pdf -X POST http://localhost:8080/api/pdf -d '<h1>Hello this is a test</h1><img src="http://www2.sotong.io/static/tintin.jpg"><a href="https://github.com/u1i/jogu">generated by jogu</a>'`

### ... and get a PDF!

![](https://raw.githubusercontent.com/u1i/jogu/master/img/jogu3.png)

### Run with Docker

docker run -d -p 8080:8080 u1ih/jogu:latest

[Dockerhub](https://hub.docker.com/r/u1ih/jogu/)

### Use the API

[Swagger File](swagger.json)


### Acknowledgements 

This API is using the [wkhtmltopdf](https://wkhtmltopdf.org/) library and a base docker image built by [Sebastian Beuke](https://github.com/madnight/docker-alpine-wkhtmltopdf)

