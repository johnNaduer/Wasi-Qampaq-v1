<template>
  <div>
    <div class="dashboard row">
      <div class="dashboard-item col-md-4">
        <h4>Numero-Espacio</h4>
        <div class="dashboard-value">{{ totalNumeroEspacio }}</div>
      </div>
      <div class="dashboard-item col-md-4">
        <h4>Habitaciones</h4>
        <div class="dashboard-value">{{ totalHabitaciones }}</div>
      </div>
      <div class="dashboard-item col-md-4">
        <h4>Gráfico de Habitaciones</h4>
        <canvas ref="chartCanvas"></canvas>
      </div>
    </div>

    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Habitaciones</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in datos" :key="item.name">
          <td>{{ item.name }}</td>
          <td>{{ item.habitaciones }}</td>
          <td>{{ item.email }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      datos: [
        { name: 'John Doe', numeroEspacio: 123, habitaciones: 2, email: 'johndoe@example.com' },
        { name: 'Jane Smith', numeroEspacio: 456, habitaciones: 3, email: 'janesmith@example.com' },
        { name: 'Mark Johnson', numeroEspacio: 789, habitaciones: 1, email: 'markjohnson@example.com' },
        { name: 'Marki Johnsan', numeroEspacio: 7589, habitaciones: 8, email: 'markjohn@example.com' }
      ],
      chart: null
    };
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      const habitacionesData = this.datos.map(item => item.habitaciones);
      const nombresData = this.datos.map(item => item.name);

      const chartData = {
        labels: nombresData,
        datasets: [
          {
            label: 'Habitaciones',
            data: habitacionesData,
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }
        ]
      };

      const chartOptions = {
        scales: {
          y: {
            beginAtZero: true,
            precision: 0
          }
        }
      };

      const ctx = this.$refs.chartCanvas.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: chartOptions
      });
    }
  },
  computed: {
    totalNumeroEspacio() {
      return this.datos.reduce((total, item) => total + item.numeroEspacio, 0);
    },
    totalHabitaciones() {
      return this.datos.reduce((total, item) => total + item.habitaciones, 0);
    }
  }
};
</script>

<style scoped>
.dashboard {
  margin-bottom: 20px;
}

.dashboard-item {
  text-align: center;
  padding: 10px;
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
}

.dashboard-value {
  font-size: 24px;
  font-weight: bold;
}

canvas {
  max-width: 100%;
  height: auto;
}
</style>
