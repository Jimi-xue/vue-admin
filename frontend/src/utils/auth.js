import Cookies from 'js-cookie'

const TokenKey = 'Token'
const RefreshKey = 'Refresh'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function getRefresh() {
  return Cookies.get(RefreshKey)
}

export function setRefresh(refresh) {
  return Cookies.set(RefreshKey, refresh)
}

export function removeRefresh() {
  return Cookies.remove(RefreshKey)
}
