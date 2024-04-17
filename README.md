# Tarea de LLM

# Iniciando 
A continuación se indican una serie de instruciones para bajar y ejecutar el proyecto de manera exitosa:

Es **importante**❗tener instalado: 
- [GIT](https://git-scm.com) : Control de versiones.
- [PYTHON](https://www.python.org/): Lenguaje de programación

 # Arquitectura 📄 
Esta arquitectura parece ser un sistema modular diseñado para interactuar con modelos de procesamiento de lenguaje natural (NLP) y recuperación de información (IR) utilizando la biblioteca LangChain, así como servicios externos como OpenAI y Pinecone. Se divide en tres clases principales: main.py, RagMemoryVector.py y [RagPinecone.py, cada una con su conjunto de funcionalidades específicas.

1. [main.py](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/main.py):
   
    * Esta clase utiliza la biblioteca LangChain para interactuar con modelos de aprendizaje automático de lenguaje, especialmente un modelo preentrenado llamado LLMChain.
    * Importa clases y funciones necesarias de LangChain, como LLMChain, OpenAI, y PromptTemplate.
    * Establece una clave de API de OpenAI como variable de entorno para autenticar las solicitudes de servicio.
    * Crea un modelo de llamada que se utiliza para formular preguntas al modelo LLMChain, con un marcador de posición para la pregunta.
    * Realiza una pregunta específica sobre la teoría de la ciencia de Popper al modelo LLMChain y muestra la respuesta generada por el modelo.
    
2. [RagMemoryVector.py](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/RagMemoryVector.py):
  
    * Esta clase utiliza la biblioteca LangChain para una variedad de tareas relacionadas con el procesamiento de lenguaje natural (NLP) y la recuperación de información (IR).
    * Importa bibliotecas como BeautifulSoup (bs4) para el procesamiento de documentos HTML, y módulos específicos de LangChain como ChatOpenAI, WebBaseLoader, OpenAIEmbeddings, etc.
    * Configura la clave de API de OpenAI como variable de entorno.
    * Descarga documentos en línea utilizando WebBaseLoader y BeautifulSoup.
    * Divide el texto de los documentos en partes más pequeñas para facilitar el procesamiento y la generación de vectores semánticos.
    * Crea vectores semánticos utilizando OpenAIEmbeddings y los almacena en un almacenamiento optimizado llamado Chroma.
    * Configura modelos de chat como ChatOpenAI para generar respuestas a preguntas.
    * Configura un pipeline de procesamiento de texto que incluye recuperación de información, modelo de lenguaje y análisis de salida.
    * Utiliza el pipeline configurado para formular una pregunta específica y obtener una respuesta del modelo de lenguaje conversacional.

3. [RagPinecone.py](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/RagPinecone.py):
   
    * Utiliza LangChain y Pinecone para cargar texto, crear vectores semánticos y realizar búsquedas similares a través de documentos.
    * Importa clases y funciones necesarias de LangChain y Pinecone.
    * Configura claves de API de OpenAI y Pinecone como variables de entorno.
    * Carga documentos desde un archivo de texto y los divide en partes más pequeñas para procesamiento.
    * Produce vectores semánticos utilizando OpenAIEmbeddings y los almacena en un índice de Pinecone.
    * Realiza búsquedas de documentos relacionados utilizando Pinecone y muestra el contenido del documento más similar a una pregunta dada.
    
 # Instalación ⬇️ y Ejecución🪄
* Los siguiente comando le permitira clonar el repositorio de manera local:
  ~~~
  git clone https://github.com/SantiagoMelo0104/AREP-LAB9.git
  ~~~
* Para este ejemplo usaremos el IDE de Pycharm :
* Una vez clonado el proyecto se pude abrir desde un editor de código como Pycharm para editar porque se debe poner las siguientes:
  * PINECONE_API_KEY --> Esta la obtenemos al crear una cuenta en https://www.pinecone.io/
    ![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/2d8b8ca6-9ec3-43da-94d0-cabc6e38ec99)
  * OPENAI_API_KEY --> Esta es proporcinada por el profesor

* Se debe instalar los paquetes que esta en el archivo [requirements.txt](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/requirements.txt) con el siguiente comando o al abrir en pycharm da la opción de descargar:
  ~~~
  pip install -r requirements.txt
  ~~~
  ![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/e69c55bb-31c8-4191-8cab-5b9192d6eb13)

* Una vez clonado y configurado en cada , ubicamos y Para ejecutar el proyecto podemos hacerlo presionando cualquiera de los recuadros a continuación
![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/2f8d83d7-23d3-414b-984b-c533ded8a9b7)

 # Pruebas 
- En [main.py](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/main.py):
  
  ![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/2f8d83d7-23d3-414b-984b-c533ded8a9b7)
  
- En [RagMemoryVector.py](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/RagMemoryVector.py):

  ![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/831dd4fe-8694-4fe1-867b-a3dd49045f1a)
  
- En [RagPinecone.py](https://github.com/SantiagoMelo0104/AREP-LAB9/blob/Master/RagPinecone.py):

 # Autor 
Santiago Naranjo Melo [SantiagoMelo0104](https://github.com/SantiagoMelo0104)


code3
![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/1a8bf903-6b8d-487c-bdc7-58c506832d11)
![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/59b4f24c-2a0b-4159-ac26-d96f509e2b59)
![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/adf7d727-7b56-4925-b11c-029eb816f990)
![imagen](https://github.com/SantiagoMelo0104/AREP-LAB9/assets/123812833/49da5427-bdec-4946-ab98-60eb3a581188)






