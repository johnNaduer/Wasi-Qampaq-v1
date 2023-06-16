<template>
    <div>
        <div class="card">
            <div class="card-header text-center text-3x1">
                Inquilinos
            </div>
            <button class="my-5 py-1 bg-green-600 rounded cursor-pointer">
                                    Agregar
            </button>
            <div class="card-body">
                <table class="rounded-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Correo</th>
                            <th>Teléfono</th>
                            <th>Fecha de inicio</th>
                            <th>Nombre de la propiedad</th>
                            <th>Número de espacio</th>
                            <th class="backgraund-color: red">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="persona in personas" :key="persona.id">
                            <td>{{ persona.id }}</td>
                            <td>{{ persona.nombre }}</td>
                            <td>{{ persona.apellido }}</td>
                            <td>{{ persona.correo }}</td>
                            <td>{{ persona.telefono }}</td>
                            <td>{{ persona.fecha_inicio }}</td>
                            <td>{{ persona.nom_propiedad }}</td>
                            <td>{{ persona.num_espacio }}</td>
                            <td>
                                <button type="" class="my-5 py-1 bg-green-600 rounded cursor-pointer">
                                    Editar
                                </button>
                                <button class="my-5 py-1 bg-red-600 rounded cursor-pointer">
                                    Eliminar
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>   
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                personas: [
                    { id: 1, nombre: 'Juan', apellido: "Pablo", correo: 'juan@example.com', telefono: "925345678", fecha_inicio: "23/08/2023", nom_propiedad:"propiedad de juan", num_espacio:"123"},
                    { id: 2, nombre: 'María', apellido: "Antonio", correo: 'maria@example.com',telefono: "925345678", fecha_inicio: "23/08/2023", nom_propiedad:"propiedad de juan", num_espacio:"123"},
                    { id: 3, nombre: 'Pedro', apellido: "Ramirez", correo: 'pedro@example.com',telefono: "925345678", fecha_inicio: "23/08/2023", nom_propiedad:"propiedad de juan", num_espacio:"123"},
                ]        
            };
        }
    };
</script>
<style scoped>
    table.rounded-table {
    width: 100%;
    border-collapse: collapse;
    border-radius: 10px;
    overflow: hidden;
    }

    th, td {
    border: 1px solid #ccc;
    padding: 8px;
    }

    th {
    background-color: #28AEC1;
    }

    button {
    margin-right: 5px;
    }
</style>
