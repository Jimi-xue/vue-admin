import request from '@/utils/request'

export function getHosts() {
  return request({
    url: '/assets/show_hosts',
    method: 'get'
  })
}
export function setHost(data) {
  console.log(data)
  return request({
    url: '/assets/add_host',
    method: 'post',
    data
  })
}
export function delHost(params) {
  return request({
    url: '/assets/host/' + params,
    method: 'delete',
  })
}
