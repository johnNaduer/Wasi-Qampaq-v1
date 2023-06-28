#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, jsonify
from models.state2 import state
from models.administrador2 import administrador
from models.administrator2 import administrator
from models.propiedad2 import propiedad
from models.espacio2 import espacio
from models.register2 import register
from models.tenant2 import tenant
from models.property2 import property2
from models.file2 import file2
import models
from flask_weasyprint import HTML, render_pdf
from flask_cors import CORS
import base64
import io

#from sqlalchemy.orm import session

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/espacios/<int:espacio_id>', methods=['DELETE'])
def delete_espacio(espacio_id):
    esp = models.estorage.get(espacio, espacio_id)

    if esp:
        models.estorage.delete(esp)
        return jsonify({'message': 'Espacio deleted successfully'})
    else:
        return jsonify({'message': 'Espacio not found'}), 404



@app.route('/add_espacio', methods=['POST'])
def add_espacio():
    id_propiedad = request.json.get('id_propiedad')
    numero = request.json.get('numero')
    descripcion = request.json.get('descripcion')
    precio = request.json.get('precio')
    disponibilidad = request.json.get('disponibilidad')

    new_espacio = espacio(
        id_propiedad=id_propiedad,
        numero=numero,
        descripcion=descripcion,
        precio=precio,
        disponibilidad=disponibilidad
    )

    models.estorage.new(new_espacio)

    return jsonify({'message': 'Espacio added successfully'})



# Ruta GET para obtener todos los espacios
@app.route('/espacios', methods=['GET'])
def get_espacios():
    espacios = models.estorage.all(espacio)

    if espacios:
        espacio_list = []
        for esp in espacios:
            espacio_data = {
                'id': esp.id,
                'id_propiedad': esp.id_propiedad,
                'numero': esp.numero,
                'descripcion': esp.descripcion,
                'precio': esp.precio,
                'disponibilidad': esp.disponibilidad
            }
            espacio_list.append(espacio_data)

        return jsonify(espacio_list)
    else:
        return jsonify([])



@app.route('/files/<int:id>', methods=['GET'])
def get_file(id):
    file = models.estorage.get(file2, id)  # Obtiene el archivo de la base de datos por su ID

    if file:
        response = make_response(file.archivo)
        response.headers.set('Content-Type', 'application/pdf')
        response.headers.set('Content-Disposition', 'attachment', filename='archivo.pdf')

        return response
    else:
        return jsonify({'message': 'Archivo no encontrado'})


@app.route('/files', methods=['GET'])
def get_files():
    files = models.estorage.all(file2)  # Obtiene todos los archivos almacenados en la base de datos

    file_list = []
    for file in files:
        file_data = {
            'id': file.id,
            'tenant_id'
            'archivo': base64.b64encode(file.archivo).decode('utf-8')  # Codifica los datos en base64
        }
        file_list.append(file_data)

    return jsonify({'files': file_list})


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')  # Obtiene el archivo del campo 'file' en la solicitud
    tenant_id = request.form.get('tenantId') #obtner el id del inquilino
    id = request.form.get('tenantId')

    if file and tenant_id:
        file_data = file.read()  # Lee los datos del archivo

        new_file = file2(id = id, archivo=file_data, tenant_id=tenant_id)  # Crea una nueva instancia del modelo File

        models.estorage.new(new_file)  # Agrega el nuevo archivo a la sesión de almacenamiento

        return jsonify({'message': 'Archivo cargado exitosamente'})
    else:
        return jsonify({'message': 'No se encontró el archivo'})



@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    prop = models.estorage.get(propiedad, property_id)

    if prop:
        models.estorage.delete(prop)
        return jsonify({'message': 'Property deleted successfully'})
    else:
        return jsonify({'message': 'Property not found'}), 404


@app.route('/add_property', methods=['POST'])
def add_property():
    id = request.json.get('id')
    id_administrator = request.json.get('id_administrator')
    name = request.json.get('name')
    direction = request.json.get('direction')
    phone = request.json.get('phone')
    description = request.json.get('description')

    new_property = propiedad(
        id = id,
        id_administrator=id_administrator,
        name=name,
        direction=direction,
        phone=phone,
        description=description
    )

    models.estorage.new(new_property)

    return jsonify({'message': 'Property added successfully'})


@app.route('/properties', methods=['GET'])
def get_properties():
    props = models.estorage.all(propiedad)

    if props:
        prop_list = []
        for prop in props:
            prop_data = {
                'id': prop.id,
                'id_administrator': prop.id_administrator,
                'name': prop.name,
                'direction': prop.direction,
                'phone': prop.phone,
                'description': prop.description
            }
            prop_list.append(prop_data)

        return jsonify(prop_list)
    else:
        return jsonify([])


@app.route('/administrators/<int:administrator_id>', methods=['DELETE'])
def delete_administrator(administrator_id):
    admin = models.estorage.get(administrator, administrator_id)

    if admin:
        models.estorage.delete(admin)
        return jsonify({'message': 'Administrator deleted successfully'})
    else:
        return jsonify({'message': 'Administrator not found'}), 404


@app.route('/add_administrator', methods=['POST'])
def add_administrator():
    name_administrador = request.json.get('name_administrador')
    apellidos_administrador = request.json.get('apellidos_administrador')
    dni = request.json.get('dni')
    email = request.json.get('email')
    phone = request.json.get('phone')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    new_admin = administrator(
        name_administrador=name_administrador,
        apellidos_administrador=apellidos_administrador,
        dni=dni,
        email=email,
        phone=phone,
        start_date=start_date,
        end_date=end_date
    )

    models.estorage.new(new_admin)

    return jsonify({'message': 'Administrator added successfully'})


@app.route('/administrators', methods=['GET'])
def get_administrators():
    admins = models.estorage.all(administrator)

    if admins:
        admin_list = []
        for admin in admins:
            admin_data = {
                'id': admin.id,
                'name_administrador': admin.name_administrador,
                'apellidos_administrador': admin.apellidos_administrador,
                'dni': admin.dni,
                'email': admin.email,
                'phone': admin.phone,
                'start_date': admin.start_date,
                'end_date': admin.end_date
            }
            admin_list.append(admin_data)

        return jsonify(admin_list)
    else:
        return jsonify([])


@app.route('/tenants/<int:tenant_id>', methods=['DELETE'])
def delete_tenant(tenant_id):
    tenants = models.estorage.get(tenant, tenant_id)

    if tenants:
        models.estorage.delete(tenants)
        return jsonify({'message': 'Tenant deleted successfully'})
    else:
        return jsonify({'message': 'Tenant not found'}), 404


@app.route('/tenants', methods=['GET'])
def get_tenants():
    tenants = models.estorage.all(tenant)

    if tenants:
        tenant_list = []
        for tenant1 in tenants:
            tenant_data = {
                'id': tenant1.id,
                'name': tenant1.name,
                'first_last_name': tenant1.first_last_name,
                'second_last_name': tenant1.second_last_name,
                'dni': tenant1.dni,
                'phone': tenant1.phone,
                'email': tenant1.email,
                'start_date': tenant1.start_date,
                'end_date': tenant1.end_date,
                'espacio_numero': tenant1.espacio_numero,
                'id_propiedad': tenant1.id_propiedad
            }
            tenant_list.append(tenant_data)

        return jsonify(tenant_list)
    else:
        return jsonify([])    

@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    name = request.json.get('name')
    first_last_name = request.json.get('first_last_name')
    second_last_name = request.json.get('second_last_name')
    dni = request.json.get('dni')
    phone = request.json.get('phone')
    email = request.json.get('email')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date') 
    espacio_numero = request.json.get('espacio_numero')
    id_propiedad = request.json.get('id_propiedad')

    new_tenant = tenant(
        name=name,
        first_last_name=first_last_name,
        second_last_name=second_last_name,
        dni=dni,
        phone=phone,
        email=email,
        start_date=start_date,
        end_date=end_date,
        espacio_numero=espacio_numero,
        id_propiedad=id_propiedad
    )

    models.estorage.new(new_tenant)

    return jsonify({'message': 'Tenant added successfully'})

@app.route("/register", methods=['POST'])
def register_user():
    # Obtener los datos enviados desde Modal.vue
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    password_2 = request.json.get('password_2')

    # Crear una instancia del modelo register
    new_register = register(name=name, email=email, password=password, password_2=password_2)

    # Guardar el registro en la base de datos
    models.estorage.new(new_register)

    return jsonify({'message': 'Usuario registrado correctamente'})

@app.route('/login', methods=['POST'])
def login_user():
    """ obtener los datos enviados desde LoginView.vue """
    email = request.json.get('email')
    password = request.json.get('password')

    """ buscar el usuario en el modelo register por su correo electronico """

    user = models.estorage.get_user_by_email(email)
    if user is not None and user.password == password:
        return jsonify({'message': 'Inicio de sesion exitoso'})
    else:
        return jsonify({'message': 'credenciales incorrectas'})


@app.route("/")
def index():
    states = models.estorage.all(state)
    return render_template("index.html", states=states)

if __name__ == '__main__':
    app.run(port=5001)
