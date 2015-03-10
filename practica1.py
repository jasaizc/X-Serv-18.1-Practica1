#!/usr/bin/python
import webapp
class contentApp (webapp.webApp):

    tabla = ""
    conteo = 0;
    diccionario = {}

    def parse(self, request):
        recurso = request.split()[1]
        metodo = request.split()[0]
        if metodo == "POST":
            cuerpo = request.split("\r\n\r\n", 1)[1]
        else:
            cuerpo = ""
        return (metodo, recurso, cuerpo)

    def process(self, resourceName):
        formulario = "<form action='http://localhost:1234/' method='POST' enctype='text/plain'>Introduzca el Valor y pulse Enter: <input type='text'name='url'></form>"
        httpCode = "404 NOT FOUND"                
        htmlBody = "<html><body>PAGINA NO ENCONTRADA</body></html>"+ "\r\n" 	 
        metodo, recurso, cuerpo = resourceName
        if metodo == "GET":        
            if recurso == "/":
                httpCode = "200 OK"                
                htmlBody = "<html><body><h1>ACORTADOR DE URL's</h1><p>" + formulario  + self.tabla + "</p></body></html>\r\n"	
                
            else:
                try:
                    numero = int(recurso[1:])
                except:
                     httpCode = "404 NOT FOUND"                
                     htmlBody = "<html><body>PAGINA NO ENCONTRADA</body></html>"+ "\r\n" 	
                for num in self.diccionario.values():
                    if numero == self.diccionario.values()[num]:
                        httpCode = "200 OK"
                        htmlBody = "<html> <head><html><head><meta http-equiv='Refresh' content='0; url= " + self.diccionario.keys()[num] +"'></head><body></body></html></head><body></body></html>\r\n" 
                        break
        elif metodo == "POST":
            cuerpo = cuerpo.split('=', 1)[1]
            if not cuerpo.startswith('http'):
                cuerpo = ("http://" + cuerpo[:-2] + "/")
            if not (self.diccionario.has_key(cuerpo)):
                print str(cuerpo)
                self.diccionario[cuerpo] = self.conteo
                numero = self.conteo
                self.tabla = self.tabla + "<div><a href= " 'http://localhost:1234/' + str(numero) + "> http://localhost:1234/" + str(numero) + "</a>.................<a href = " + str(cuerpo)   +  ">" + str(cuerpo)  + "</a>  </div>"
                self.conteo = self.conteo + 1                 
            else:
                numero = self.diccionario[cuerpo]              
            print self.diccionario
            httpCode = "200 OK"
            htmlBody = "<html><body>Acortada, la nueva Direccion es: <div><a href= " 'http://localhost:1234/' + str(numero) + "> http://localhost:1234/" + str(numero) + "</a>.................<a href = " + str(cuerpo)   +  ">" + str(cuerpo)  + "</a></div></body></html>"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
