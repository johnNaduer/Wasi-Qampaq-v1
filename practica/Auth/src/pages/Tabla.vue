<template>
    <div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Surname</th>
            <th>DNI</th>
            <th>Space ID</th>
            <th>Space Number</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(registro, index) in registrosPaginados" :key="index">
            <td>{{ registro.id }}</td>
            <td>{{ registro.name }}</td>
            <td>{{ registro.surname }}</td>
            <td>{{ registro.dni }}</td>
            <td>{{ registro.spaceId }}</td>
            <td>{{ registro.spaceNumber }}</td>
          </tr>
        </tbody>
      </table>
  
      <div class="pagination">
        <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
        <span>{{ currentPage }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        registros: [
          { id: 1, name: 'John', surname: 'Doe', dni: '123456789', spaceId: 'A1', spaceNumber: 101 },
          { id: 2, name: 'Jane', surname: 'Smith', dni: '987654321', spaceId: 'B2', spaceNumber: 202 },
          { id: 3, name: 'Robert', surname: 'Johnson', dni: '456789123', spaceId: 'C3', spaceNumber: 303 },
          { id: 4, name: 'Alice', surname: 'Williams', dni: '789123456', spaceId: 'D4', spaceNumber: 404 },
          { id: 5, name: 'Michael', surname: 'Brown', dni: '321654987', spaceId: 'E5', spaceNumber: 505 },
          { id: 6, name: 'Emily', surname: 'Jones', dni: '654789321', spaceId: 'F6', spaceNumber: 606 },
          { id: 7, name: 'David', surname: 'Taylor', dni: '987321654', spaceId: 'G7', spaceNumber: 707 },
          { id: 8, name: 'Sophia', surname: 'Miller', dni: '159753852', spaceId: 'H8', spaceNumber: 808 },
          { id: 9, name: 'Daniel', surname: 'Anderson', dni: '753951852', spaceId: 'I9', spaceNumber: 909 },
          { id: 10, name: 'Olivia', surname: 'Wilson', dni: '258369147', spaceId: 'J10', spaceNumber: 1010 }
        ],
        registrosPorPagina: 8,
        currentPage: 1
      };
    },
    computed: {
      totalRegistros() {
        return this.registros.length;
      },
      totalPages() {
        return Math.ceil(this.totalRegistros / this.registrosPorPagina);
      },
      registrosPaginados() {
        const inicio = (this.currentPage - 1) * this.registrosPorPagina;
        const fin = inicio + this.registrosPorPagina;
        return this.registros.slice(inicio, fin);
      }
    },
    methods: {
      previousPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
        }
      }
    }
  };
  </script>
  
  <style>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  .pagination {
    margin-top: 16px;
    display: flex;
    justify-content: center;
  }
  
  .pagination button {
    margin: 0 5px;
  }
  </style>
  