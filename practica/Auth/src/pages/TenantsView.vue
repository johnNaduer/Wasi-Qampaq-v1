<template>
    <div class="p-4">
        <div class="card">
            <h2 class="text-2xl font-bold mb-4 text-center">Tenants</h2>
            <div>
                <button @click="addData(index)" class="px-4 py-2 bg-green-500 text-white rounded mr-2 hover:bg-green-600 transition-colors duration-200 ease-in-out">Agregar</button>
            </div>
            <div class="card-body">
                <table id="data" class="w-full bg-white rounded-lg shadow-lg">
                    <thead>
                        <tr>
                            <th class="px-6 py-4 bg-blue-500 text-white">Name</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Surname</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Second Surname</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">DNI/Inmigration Card</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Phone</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Email</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Start Date</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Final Date</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Property-ID</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border">
                                <div class="flex justify-end">
                                    <button @click="editData(index)" class="px-4 py-2 bg-green-500 text-white rounded-full mr-2 hover:bg-green-600 transition-colors duration-200 ease-in-out">Editar</button>
                                    <button @click="deleteData(index)" class="px-4 py-2 bg-red-500 text-white rounded-full hover:bg-red-600 transition-colors duration-200 ease-in-out">Eliminar</button>
                                </div>
                            </td>    
                        </tr>
                    </tbody>
                </table>
            </div>   
        </div>
    </div>
</template>
<script>
    
</script>
<style scoped>

</style>
