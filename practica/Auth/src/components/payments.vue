<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br><br>
        <h1>Pay</h1>
        <hr><br><br>
        <div class="text-center mb-3">
          <svg class="chart-svg" viewBox="0 0 32 32" width="200" height="200">
            <circle
              v-for="(slice, index) in slices"
              :key="index"
              r="13"
              cx="16"
              cy="16"
              :style="{
                strokeDasharray: `${slice} 100`,
                stroke: getSliceColor(index),
                fill: 'transparent',
                strokeWidth: '3px'
              }"
              :transform="`rotate(${-90 + 360 * accumulatedSlices[index]} 16 16)`"
            />
          </svg>
          <circle
            r="13"
            cx="16"
            cy="16"
            :style="{
              fill: getSliceColor(0),
              stroke: 'none'
            }"
            class="shadow-sm rounded-circle text-white"
          />
        </div>
        <div class="text-center">
          <table class="table table-condensed">
            <tbody>
              <tr>
                <td colspan="2">Porcentaje Sí: {{ getPercentageYes }}% <span class="color-square" style="background-color: green;"></span></td>
              </tr>
              <tr>
                <td colspan="2">Porcentaje No: {{ getPercentageNo }}% <span class="color-square" style="background-color: red;"></span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <button type="button" class="btn btn-success btn-sm" @click="toggleAddBookModal">
          Add Pay
        </button>
        <br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th class="col">ID</th>
              <th class="col">ID tenant</th>
              <th class="col">Name</th>
              <th class="col">Property</th>
              <th class="col">Number</th>
              <th class="col">Date Time</th>
              <th class="col">Pay ?</th>
              <th class="col">Actions</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data in dataList" :key="data.ID">
              <td>{{ data.ID }}</td>
              <td>{{ data['ID tenant'] }}</td>
              <td>{{ data.Name }}</td>
              <td>{{ data.Property }}</td>
              <td>{{ data.Number }}</td>
              <td>{{ data['Date Time'] }}</td>
              <td>{{ data.Pay }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<style>
.chart-svg {
  width: 180px; /* Ajusta el ancho del gráfico según tus preferencias */
  height: 180px; /* Ajusta el alto del gráfico según tus preferencias */
  margin: 0 auto; /* Centra horizontalmente el gráfico */
}
.color-square {
  display: inline-block;
  width: 15px;
  height: 15px;
  margin-right: 5px;
  border-radius: 2px;
}


.table-condensed td {
  padding: 7px; /* Ajusta el espaciado interno de las celdas */
  vertical-align: middle; /* Centra verticalmente el contenido de las celdas */
}       
</style>



<script>
export default {
  data() {
    return {
      dataList: [
        {
          ID: 1,
          'ID tenant': 1001,
          Name: 'John Doe',
          Property: 'ABC',
          Number: 123,
          'Date Time': '2023-06-28 09:00',
          Pay: 'Sí'
        },
        {
          ID: 2,
          'ID tenant': 1002,
          Name: 'Jane Smith',
          Property: 'XYZ',
          Number: 456,
          'Date Time': '2023-06-28 13:30',
          Pay: 'No'
        },
        {
          ID: 3,
          'ID tenant': 1003,
          Name: 'David Johnson',
          Property: 'DEF',
          Number: 789,
          'Date Time': '2023-06-28 16:45',
          Pay: 'Sí'
        }
      ]
    };
  },
  computed: {
    slices() {
      let payYes = 0;
      let payNo = 0;
      this.dataList.forEach(data => {
        if (data.Pay === 'Sí') {
          payYes++;
        } else if (data.Pay === 'No') {
          payNo++;
        }
      });
      let payYesPercentage = (payYes / this.dataList.length) * 100;
      let payNoPercentage = (payNo / this.dataList.length) * 100;
      return [payYesPercentage.toFixed(2), payNoPercentage.toFixed(2)]; // Actualización de los valores con toFixed()
    },
    accumulatedSlices() {
      let result = [];
      let sum = 0;
      for (let i = 0; i < this.slices.length; i++) {
        result.push(sum);
        sum += this.slices[i] / 100;
      }
      return result;
    },
    getPercentageYes() {
      const total = this.dataList.length;
      const countYes = this.dataList.filter((data) => data.Pay === 'Sí').length;
      return (countYes / total * 100).toFixed(2);
    },
    getPercentageNo() {
      const total = this.dataList.length;
      const countNo = this.dataList.filter((data) => data.Pay === 'No').length;
      return (countNo / total * 100).toFixed(2);
    },
  },
methods: {
    getSliceColor(index) {
      return index === 0 ? 'green' : 'red'; // Actualizado: Asigna verde al primer índice (Sí) y rojo al segundo índice (No)
    }
  }

};
</script>
