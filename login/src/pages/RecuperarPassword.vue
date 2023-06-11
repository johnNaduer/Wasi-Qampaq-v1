<script setup></script>

<template>
    <div class="flex justify-center">
        <form action="" class=" border-2 border-sky-500 w-72 rounded-md p-7 text-center">
            <h1 class="text-3xl pb-5">Register</h1>
            <div class="pb-3">
                <label for="name" class="block">Ingrese su nombre</label>
                <input type="text" placeholder="nombre" id="name" class="border-2 border-black rounded px-2 py-1">
            </div>

            <div class="pb-3">
                <label for="correo" class="block">Ingrese su Correo</label>
                <input type="text" placeholder="correo" id="correo" class="border-2 border-black rounded px-2 py-1">
            </div>

            <div class="pb-3">
                <label for="password" class="block">Ingrese su contraseña</label>
                <input type="password" placeholder="Contraseña" id="password" class="border-2 border-black rounded px-2 py-1">
            </div>

            <div class="pb-3">
                <label for="repassword" class="block">Repite su contraseña</label>
                <input type="password" placeholder="Contraseña" id="repassword" class="border-2 border-black rounded px-2 py-1">
            </div>
        </form>
    </div>
</template>