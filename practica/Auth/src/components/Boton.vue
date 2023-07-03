<template>
  <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12],
        backgroundColor: [
            'rgba(255, 99, 132, 0.8)',  // Color para la primera barra
            'rgba(54, 162, 235, 0.8)', // Color para la segunda barra
            'rgba(75, 192, 192, 0.8)', // Color para la tercera barra
          ],
        barThickness: 70,
        },

        ]
      },
      chartOptions: {
        responsive: true
      }
    }
  }
}
</script>
