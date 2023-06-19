<template>
    <div class="p-4">
        <div class="card">
            <h2 class="text-2xl font-bold mb-4 text-center">Tenants</h2>
            <div>
                <ModalView />
        </div>
            <div class="card-body">
                <table id="data" class="w-full bg-white rounded-lg shadow-lg">
                    <thead>
                        <tr>
                            <th class="px-6 py-4 bg-blue-500 text-white">ID</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Name</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Surname</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Second Surname</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">DNI / Inmigration Card</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Phone</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Email</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Start Date</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Final Date</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Espace-ID</th>
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
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border"></td>
                            <td class="px-6 py-4 border">
                                <div class="flex justify-end">
                                    <ModalEditView />
                                    <ModalDeleteView />
                                </div>
                            </td>    
                        </tr>
                    </tbody>
                </table>
            </div>   
        </div>
    </div>
</template>

<script setup>
import ModalView from '../components/ModalView.vue';
import ModalDeleteView from '../components/ModalDeleteView.vue';
import ModalEditView from '../components/ModalEditView.vue';
</script>

