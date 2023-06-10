<template>
    <div class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
        <div class="bg-white p-8">
            <form action="" @submit.prevent=""
                class="border-2 border-white bg-white w-96 flex justify-center flex-col p-5 rounded-md shadow-xl shadow-gray-300">
                <input type="text" placeholder="Nombres y Apellidos"
                    class="border-gray-400 border px-3 py-1 rounded-md mb-5">
                <input type="gmail" placeholder="Correo electrónico"
                    class="border-gray-400 border px-3 py-1 rounded-md mb-5">
                <input type="password" placeholder="Contraseña" class="border-gray-400 border px-3 py-1 rounded-md mb-5">
                <input type="password" placeholder="Repite Contraseña"
                    class="border-gray-400 border px-3 py-1 rounded-md mb-5">
                <button class="mt-5 bg-green-500 text-xl py-3 rounded text-white font-semibold mb-3">
                    Crear cuenta nueva
                </button>
                <button  @click="closeModal">Cerrar</button>
            </form>
        </div>
    </div>
</template>

<script setup>

defineProps({
    closeModal: Function
}) 
</script>
