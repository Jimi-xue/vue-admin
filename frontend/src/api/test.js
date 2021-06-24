import request from '@/utils/request'

export function getBooks() {
  return request({
    url: '/show_books', // 假地址 自行替换
    method: 'get'
  })
}