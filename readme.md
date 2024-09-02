# Utiles
    python3
    exit() para salir de la interfaz de python
# Instalación
    apt update
    sudo apt update
    sudo apt -y upgrade
# Verificar Instalación de python
    python3 -V
    Instalación de gestor de paquetes de dependencias
    sudo apt insstall -y python3-pip
   
# Verificar Instalación del gestor
    pip3 -V
# Dependencias en entorno profesional
    apt install -y build-essential libssl-dev libffi-dev python3-dev
# VSCode 
## Extensiones
    Python
    Wsl

# Game Project
    ```sh
    cd game
    python3 main.py
    ```
# App Project
    ```sh   
    git clone
    python3 -m venv env    
    source env/bin/activate
    cd app
    pip3 install -r requirements.txt
    python3 main.py
    ```
# Web Server Project 
    ```sh   
    git clone
    python3 -m venv env    
    source env/bin/activate
    cd web-server
    pip3 install -r requirements.txt
    uvicorn main:app --reload
    ```   
# Task Tracker Project
    ```sh   
    git clone
    python3 -m venv env    
    source env/bin/activate
    cd task-tracker
    pip3 install -r requirements.txt
    ``` 
## Commans of task tracker project
    ```sh  
    python3 main.py add "Example Description"
    python3 main.py list
    python3 main.py list [done|todo|in-progress]
    ``` 
    




## Referencias
https://fastapi.tiangolo.com/advanced/custom-response/?h=custom+re#html-response

# Recursos para trabajar con pip3
*  [pypi](https://pypi.org/)
## Comandos utiles con pip3
     pip3 freeze (arbol de librerías de entorno de python global)
     which pip3
     which python3
# Manejar ambientes con python-venv
Tener ambiente aislado de solos paquetes ques se utilicen en el proyecto.
    sudo apt install -y python3-venv
     python3 -m venv my-env
     source my-env/bin/activate
     deactivate
     pip3 install matplotlib
## Archivo requirements.txt
pip3 freeze > requirements.txt
pip3 install -r requirements.txt