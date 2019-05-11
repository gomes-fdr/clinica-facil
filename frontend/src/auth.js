/* eslint-disable standard/no-callback-literal */
/* globals localStorage */

import axios from 'axios'

export default {

  login (email, pass, cb) {
    cb = arguments[arguments.length - 1]
    if (localStorage.token) {
      if (cb) cb(true)
      this.onChange(true)
      return
    }
    pretendRequest(email, pass, (res) => {
      if (res.authenticated) {
        if (cb) cb(true)
        this.onChange(true)
      } else {
        if (cb) cb(false)
        this.onChange(false)
      }
    })
  },
  loggedIn () {
    return localStorage.token
  },

  onChange () {},

  isValidJwt (jwt) {
    if (!jwt || jwt.split('.').length < 3) {
      return false
    }
    return true
  },

  getProfile () {
    return this.profile
  }
}

function pretendRequest (email, pass, cb) {
  setTimeout(() => {
    axios({
      method: 'post',
      url: process.env.API_URL + 'token',
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
