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
    url: '/vue-element-admin/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-element-admin/user/logout',
    method: 'post'
  })
}
