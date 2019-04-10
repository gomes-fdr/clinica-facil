/* eslint-disable standard/no-callback-literal */
/* globals localStorage */

import axios from 'axios'
import { API_URL } from './main'

export default {

  login (email, pass, cb) {
    cb = arguments[arguments.length - 1]
    delete localStorage.token
    delete localStorage.perfil
    if (localStorage.token) {
      if (cb) cb(true)
      this.onChange(true)
      return
    }
    pretendRequest(email, pass, (res) => {
      if (res.authenticated) {
        localStorage.token = res.token
        const data = JSON.parse(atob(res.token.split('.')[1]))
        localStorage.setItem('perfil', data.profile)
        localStorage.setItem('nome', data.nome)
        localStorage.setItem('situacao', data.situacao)
        if (cb) cb(true)
        this.onChange(true)
      } else {
        if (cb) cb(false)
        this.onChange(false)
      }
    })
  },

  getToken () {
    return localStorage.token
  },

  logout (cb) {
    if (cb) cb()
    this.onChange(false)
    delete localStorage.token
    delete localStorage.perfil
    delete localStorage.nome
    delete localStorage.situacao
    location.reload()
  },

  loggedIn () {
    return localStorage.token
  },

  onChange () {},

  isValidJwt (jwt) {
    if (!jwt || jwt.split('.').length < 3) {
      return false
    }
    const data = JSON.parse(atob(jwt.split('.')[1]))
    const exp = new Date(data.exp * 1000) // JS deals with dates in milliseconds since epoch
    const now = new Date()
    return now < exp
  },

  getProfile () {
    return this.profile
  }
}

function pretendRequest (email, pass, cb) {
  setTimeout(() => {
    axios({
      method: 'post',
      url: API_URL + 'token',
      data: {
        email: email,
        password: pass
      }
    })
    .then(response => {
      cb({
        authenticated: true,
        token: response.data['token']
      })
    })
    .catch(error => {
      cb({ authenticated: false })
    })
  }, 100)
}
