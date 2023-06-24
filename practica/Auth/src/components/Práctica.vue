
<template>
    <div>
      <form>
        <label for="name">Nombre:</label>
        <input type="text" id="name" v-model="newItem.name">
  
        <label for="surname">Apellido:</label>
        <input type="text" id="surname" v-model="newItem.surname">
  
        <label for="email">Correo electrónico:</label>
        <input type="email" id="email" v-model="newItem.email">
  
        <label for="startDate">Fecha de inicio:</label>
        <input type="date" id="startDate" v-model="newItem.startDate">
  
        <label for="endDate">Fecha final:</label>
        <input type="date" id="endDate" v-model="newItem.endDate">
  
        <label for="spaceNumber">Número de Espacio:</label>
        <input type="number" id="spaceNumber" v-model="newItem.spaceNumber">
  
        <label for="dni">DNI:</label>
        <input type="text" id="dni" v-model="newItem.dni">
  
        <button type="button" @click="addItem">Agregar</button>
      </form>
  
      <button type="button" @click="generatePDF">Imprimir en PDF</button>

      <ul>
        <li v-for="(item, index) in items" :key="index">
          {{ item.name }} {{ item.surname }} - {{ item.email }} - {{ item.startDate }} - {{ item.endDate }} - {{ item.spaceNumber }} - {{ item.dni }}
          <button type="button" @click="deleteItem(index)">Borrar</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import jsPDF from 'jspdf';
  
  export default {
    data() {
      return {
        items: [],
        newItem: {
          name: '',
          surname: '',
          email: '',
          startDate: '',
          endDate: '',
          spaceNumber: '',
          dni: ''
        }
      };
    },
    methods: {
      addItem() {
        this.items.push({ ...this.newItem });
        this.newItem.name = '';
        this.newItem.surname = '';
        this.newItem.email = '';
        this.newItem.startDate = '';
        this.newItem.endDate = '';
        this.newItem.spaceNumber = '';
        this.newItem.dni = '';
      },
      deleteItem(index) {
        this.items.splice(index, 1);
      },
      generatePDF() {
        const doc = new jsPDF();
        
        // Agregar imagen de fondo
        const imgUrl = 'https://png.pngtree.com/thumb_back/fw800/background/20220218/pngtree-paper-document-background-image_959676.jpg';
        doc.addImage(imgUrl, 'JPEG', 0, 0, doc.internal.pageSize.getWidth(), doc.internal.pageSize.getHeight());
  
        doc.setFontSize(18);
        doc.text('Información del Inquilino', 50, 30);
  

        let yOffset = 50;
        this.items.forEach((item, index) => {
          doc.setFontSize(12);
          
          doc.text(20, yOffset, `Nombre: ${item.name}`);
          doc.text(20, yOffset + 10, `Apellido: ${item.surname}`);
          doc.text(20, yOffset + 20, `Email: ${item.email}`);
          doc.text(20, yOffset + 30, `Fecha de inicio: ${item.startDate}`);
          doc.text(20, yOffset + 40, `Fecha final: ${item.endDate}`);
          doc.text(20, yOffset + 50, `Número de Espacio: ${item.spaceNumber}`);
          doc.text(20, yOffset + 60, `DNI: ${item.dni}`);
  
          yOffset += 80;
        });
        

        // Agregar algo en la parte final del documento
        doc.setFontSize(12);
        doc.text('Texto final del documento', 20, doc.internal.pageSize.getHeight() - 20);

        doc.save('formulario.pdf');
      }
    }
  };
  </script>