import axios from 'axios'

const axiosInstance = axios.create({
    baseURL: 'http://localhost:3900/api/v1/user',
    headers:{
        'Content-Type': 'application/json'
    }
})

export default axiosInstance