<template>
  <div  class="app-container" >
        <el-button
        type="success"
        size="small"
        icon="el-icon-circle-check-outline"
        @click="add_line()"
      >
        添加数据
      </el-button>
      <el-table  :data="tableData" border fit highlight-current-row style="width: 100%" row-key="id">
        <el-table-column align="center" label="ID">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleFetchPv(row.id)">{{ row.id }}</span>
        </template>
      </el-table-column>
        <el-table-column align="center" label="name">
        <template slot-scope="{row}">
          <template v-if="row.edit">
          <el-input v-model="row.book_name" class="edit-input" size="small" />
          </template>
          <span v-else>{{ row.book_name }}</span>
        </template>
          <el-input  class="edit-input" size="small" />
      </el-table-column>
        <el-table-column align="center" label="time">
        <template slot-scope="{row}">
          <span>{{ row.add_time }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="操作">
        <template slot-scope="{row}">
          <template v-if="row.edit">
           <span class="link-type" @click="add_book(row.book_name)">添加</span>
          </template>
          <span class="link-type" @click="deletebook(row.book_name)" v-else>删除</span>
        </template>
      </el-table-column>
      </el-table>
  </div>
</template>

<script>

import { getBooks,setBook,delBook } from '@/api/test'
import Sortable from 'sortablejs'
export default {
  data() {
    return {
      tableData: [],
      form: {
          book_name: ''
        },
      new_data:{},
    }
  },
  methods: {
    handleFetchPv(pv) {
      getBooks(pv).then(response => {
        this.pvData = response
        this.dialogPvVisible = true
      })
    },
    getbook(){
          getBooks().then(response => {
          const datas = response
          console.log(datas)
          this.tableData = datas
          resolve(true)
        }).catch(err => {
          reject(false)
        })
    },
    show() {
      return new Promise((resolve, reject) => {
        this.getbook()
      })
    },
    deletebook(book_name){
      delBook(book_name).then(response => {
          this.getbook()
      })
    },
    add_line(){
      this.new_data = {"book_name":null,"add_time":null,"id":null,"edit":'1'}
      this.tableData.push(this.new_data)
    },
    add_book(book_name){
      setBook({"book_name":book_name}).then(response => {
        this.getbook()
      })
    }
  },
    created() {
    this.show()
  }
}
</script>

