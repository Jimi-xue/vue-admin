import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/users/token/get',
    method: 'post',
    data
  })
}

export async function resettoken(data) {
  return await request({
    url: '/users/token/refresh',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/users/userinfo',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/vue-element-admin/user/logout',
    method: 'post'
  })
}

export function update_userinfo(data) {
  return request({
    url: '/users/userinfo',
    method: 'put',
    data
  })
}
export function update_useravatar(data) {
  return request({
    url: '/users/useravatar',
    method: 'post',
    data
  })
}
