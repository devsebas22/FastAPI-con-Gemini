Requerimientos Funcionales:

 El sistema debe permitir al usuario ingresar un prompt a través de la interfaz del servidor de FastAPI

 El sistema debe enviar el prompt recibido al modelo LLM y recibir una respuesta generada por el modelo. 

 El sistema debe conectarse al modelo Gemini a través de la API proporcionada 

 El sistema debe manejar posibles errores durante la comunicación con el modelo LLM, como fallos de conexión o problemas con la generación de contenido, y devolver mensajes de error informativos al usuario.

 El sistema debe ofrecer una interfaz mínima que permita a los usuarios interactuar con el 


Requerimientos No Funcionales:

El sistema debe responder a cualquier solicitud del usuario  en un tiempo máximo de 3 segundos.

El sistema debe ser capaz de manejar hasta 1000 solicitudes concurrentes sin degradar el desempeño.

El 100% de las credenciales deben estar almacenadas en variables de entorno y nunca ser expuestas en el código fuente o registros.

El código debe estar documentado adecuadamente, con comentarios explicativos en al menos el 80% de las funciones y bloques complejos.

El sistema debe garantizar un tiempo de actividad del 99.9% durante el mes.
