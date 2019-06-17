import axios from 'axios'



class APIProvider {
  constructor ({ url }) {
    this.http = axios.create({
      baseURL: url,
       headers: { 'Content-Type': 'application/json' }
    })
  }

  login (token) {
    this.ttp.defaults.headers.common.Authorization = `Bearer ${token}`
  }

  logout () {
    this.http.defaults.headers.common.Authorization = ''
  }

  // REST Methods
  find ({ resource, query }) {
    return this.http.get(resource, {
      params: query
    })
  }

  get ({ resource, id, query }) {
    return this.http.get(`${resource}/${id}`, {
      params: query
    })
  }

  getAll ({ resource, query }) {
    return this.http.get(`${resource}`, {
      params: query
    })
  }

  create ({ resource, data, query }) {
    return this.http.post(resource, data, {
      params: query
    })
  }

  update ({ resource, id, data, query }) {
    return this.http.patch(`${resource}/${id}`, data, {
      params: query
    })
  }

  destroy ({ resource, id }) {
    return this.http.delete(`${resource}/${id}`)
  }
}

export default new APIProvider({
  url: process.env.VUE_APP_API_URL  
})