<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
            <slot name="header">
                this is original header
            </slot>
            <button type="button" class="btn-close" @click="close">
                X
            </button>
            </header>
            <section class="modal-body">
            <slot name="body">
            </slot>
            </section>
            <footer class="modal-footer">
            <slot>
                this is the original footer
            </slot>
            <button type="button" class="btn-green" @click="close">
                close modal 
            </button>
            </footer>
        </div>
    </div>
</template>
<script>
export default {
    methods:{
        close(){
            this.$emit("close")
        }
    }
}
</script>
<style>

</style>