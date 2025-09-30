####
from flask import Flask, render_template
import os
import platform
from datetime import datetime
import getpass

app = Flask(__name__)

@app.route('/')
def index():
    info = {
        "Sistema_Operativo": platform.system() + " " + platform.release(),
        "Fecha_Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Ruta": os.getcwd(),
        "Usuario": getpass.getuser()
    }
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
