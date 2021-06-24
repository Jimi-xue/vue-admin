<template>
  <div className="app-container">
    <p v-for="(item,i) in dataObj">{{ i }}-----{{ item.fields.book_name }}-----{{ item.fields.add_time }}</p>
  </div>
</template>

<script>

import { getBooks } from '@/api/test'
export default {
  data() {
    return {
      dataObj: [],
    }
  },
  methods: {
    show() {
      return new Promise((resolve, reject) => {
        getBooks().then(response => {
          const datas = response
          this.dataObj = datas.list
          resolve(true)
        }).catch(err => {
          console.log(err)
          reject(false)
        })
      })
    }
  },
    created() {
    console.log('created Event  --> Goto init()')
    this.show()
  }
}
</script>
