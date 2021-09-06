import request from '@/utils/request'

export function getBooks() {
  return request({
    url: '/show_books',
    method: 'get'
  })
}
export function setBook(data) {
  console.log(data)
  return request({
    url: '/add_book',
    method: 'post',
    data
  })
}
export function delBook(params) {
  return request({
    url: '/book/' + params,
    method: 'delete',
  })
}