from flask import Flask, render_template

app = Flask(__name__)




        
# Datos para cada día
cronograma_dia29 = [["Liderazgo para Sostenibilidad y regeneración","Luis Enrique Henao Gamboa","Paraninfo","8:00","9:45 "],
                    ["Ecoguardian es: protege, previene y soluciona","Tecnológico Comfenalco","Posgrados","8:00 ","9:45 "],
                    ["Reunión Red Iddeal","","Audiovisuales","8:00","9:45"],
                    ["Diseño de un juego para enseñar educación ambiental","U Nacional","Salón 7","8:00","8:20"],
                    ["Diseño de un juego para enseñar economía circular","U Nacional","Salón 7","8:20","8:40"],
                    ["Escape room para la enseñanza de tecnologías usadas en logística de almacenes","UTP","Salón 7","8:40","9:00"],
                    ["La lúdica como herramienta transformadora en la educación superior sistematización de la experiencia en la Universidad de la Amazonia","Universidad de la Amazonia","Salón 7","9:00 ","9:20 "],
                    ["Gamificación y gratitud: un enfoque práctico desde la investigación","UCP","Salón 7","9:20 ","9:40 "],
                    ["Refrigerio","","","9:45","10:15"],
                    ["La fábrica que nunca duerme: un ejemplo de eficacia","Universidad Antioquia","Paraninfo","10:15","12:00"],
                    ["Detectives de la calidad","Tecnológico Comfenalco","Posgrados ","10:15","12:00"],
                    ["Decide antes de que quiebres ejercicio lúdico enfocado a los indicadores económicos","UIS","Audivisuales","10:15","12:00"],
                    ["Crossover Tower","UTP","Salón 7","10:15","12:00"],
                    ["Almuerzo libre","","","12:00","14:00"],
                    ["Fabrica Lean: Calidad y eficiencia en la Industria textil","Universidad Santo Tomás","Paraninfo","14:00","15:35"],
                    ["El viaje de la calidad","Tecnológico Comfenalco","Posgrados ","14:00","15:35"],
                    ["La Contratación Del Siglo: Estrategia Pedagógica Basada En El Razonamiento Matemático Aplicado A La Solución De Problemas","UIS","Audivisuales","14:00","15:35"],
                    ["Aircraft Ops","UTP","Salón 7","14:00","15:35"],
                    ["Refrigerio","","","15:35","16:15"],
                    ["Aprendiendo a asignar los recursos limitados con programación lineal","Universidad Santo Tomás","Paraninfo","16:15","17:00"],
                    ["La tiendita financiera","Tecnológico Comfenalco","Posgrados ","16:15","17:00"],
                    ["Empacando, llenando y ganando","UIS","Audivisuales","16:15","17:00"],
                    ["Mesa de Dinero","UTP","Salón 7","16:15","17:00"]]

cronograma_dia30 = [["prueba","Luis Enrique Henao Gamboa","Paraninfo","8:00","9:45 "],
                    ["Ecoguardian es: protege, previene y soluciona","Tecnológico Comfenalco","Posgrados","8:00 ","9:45 "],
                    ["Reunión Red Iddeal","","Audiovisuales","8:00","9:45"],
                    ["Diseño de un juego para enseñar educación ambiental","U Nacional","Salón 7","8:00","8:20"],
                    ["Diseño de un juego para enseñar economía circular","U Nacional","Salón 7","8:20","8:40"],
                    ["Escape room para la enseñanza de tecnologías usadas en logística de almacenes","UTP","Salón 7","8:40","9:00"],
                    ["La lúdica como herramienta transformadora en la educación superior sistematización de la experiencia en la Universidad de la Amazonia","Universidad de la Amazonia","Salón 7","9:00 ","9:20 "],
                    ["Gamificación y gratitud: un enfoque práctico desde la investigación","UCP","Salón 7","9:20 ","9:40 "],
                    ["Refrigerio","","","9:45","10:15"],
                    ["La fábrica que nunca duerme: un ejemplo de eficacia","Universidad Antioquia","Paraninfo","10:15","12:00"],
                    ["Detectives de la calidad","Tecnológico Comfenalco","Posgrados ","10:15","12:00"],
                    ["Decide antes de que quiebres ejercicio lúdico enfocado a los indicadores económicos","UIS","Audivisuales","10:15","12:00"],
                    ["Crossover Tower","UTP","Salón 7","10:15","12:00"],
                    ["Almuerzo libre","","","12:00","14:00"],
                    ["Fabrica Lean: Calidad y eficiencia en la Industria textil","Universidad Santo Tomás","Paraninfo","14:00","15:35"],
                    ["El viaje de la calidad","Tecnológico Comfenalco","Posgrados ","14:00","15:35"],
                    ["La Contratación Del Siglo: Estrategia Pedagógica Basada En El Razonamiento Matemático Aplicado A La Solución De Problemas","UIS","Audivisuales","14:00","15:35"],
                    ["Aircraft Ops","UTP","Salón 7","14:00","15:35"],
                    ["Refrigerio","","","15:35","16:15"],
                    ["Aprendiendo a asignar los recursos limitados con programación lineal","Universidad Santo Tomás","Paraninfo","16:15","17:00"],
                    ["La tiendita financiera","Tecnológico Comfenalco","Posgrados ","16:15","17:00"],
                    ["Empacando, llenando y ganando","UIS","Audivisuales","16:15","17:00"],
                    ["Mesa de Dinero","UTP","Salón 7","16:15","17:00"]]
# 2. Función de procesamiento (global)
def process_cronograma(cronograma_base):
    cronograma = []
    for item in cronograma_base:
        actividad = {
            'nombre': item[0],
            'encargado': item[1],
            'salon': item[2],
            'inicio': item[3].strip(),
            'fin': item[4].strip(),
            'participantes': 0,
            'es_especial': item[0] in ["Refrigerio", "Almuerzo libre"]
        }
        cronograma.append(actividad)
    return cronograma

# 3. Rutas (globales)
@app.route('/')  # Ruta PRINCIPAL que muestra las pestañas
def index():
    return render_template('base.html')  # Template con navegación

@app.route('/dia29')  # Ruta del primer día
def dia29():
    return render_template('dia29.html', cronograma=process_cronograma(cronograma_dia29))

@app.route('/dia30')  # Ruta del segundo día
def dia30():
    return render_template('dia30.html', cronograma=process_cronograma(cronograma_dia30))

# 4. Bloque principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
