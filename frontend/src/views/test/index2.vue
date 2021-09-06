<template>
  <div  class="app-container" >
    <div class="table-wrap">
    <div class="table-box">
      <el-table  :data="tableData" border fit highlight-current-row style="width: 100%" row-key="id">
        <el-table-column v-for="(item, index) in col"
          :key="`col_${index}`"
          :prop="dropCol[index].prop"
          :label="item.label">
        </el-table-column>
      </el-table>
    </div>
    </div>
  </div>
</template>

<script>

import { getBooks } from '@/api/test'
import Sortable from 'sortablejs'
export default {
  data() {
    return {
      col : [
          {label: 'name',prop: 'book_name'},
          {label: 'time',prop: 'add_time'}
      ],
      dropCol : [
          {label: 'name',prop: 'book_name'},
          {label: 'time',prop: 'add_time'}
      ],
      tableData: [],
    }
  },
    mounted () {
    this.rowDrop()
    this.columnDrop()
  },
  methods: {
    show() {
      return new Promise((resolve, reject) => {
        getBooks().then(response => {
          const datas = response
          console.log(datas)
          this.tableData = datas
          resolve(true)
        }).catch(err => {
          reject(false)
        })
      })
    },
     rowDrop () {
      const tbody = document.querySelector('.el-table__body-wrapper tbody')
      const _this = this
      Sortable.create(tbody, {
        onEnd ({ newIndex, oldIndex }) {
          const currRow = _this.tableData.splice(oldIndex, 1)[0]
          _this.tableData.splice(newIndex, 0, currRow)
        }
      })
    },
    // 列拖拽
    columnDrop () {
      const wrapperTr = document.querySelector('.el-table__header-wrapper tr')
      this.sortable = Sortable.create(wrapperTr, {
        animation: 180,
        delay: 0,
        onEnd: evt => {
          const oldItem = this.dropCol[evt.oldIndex]
          this.dropCol.splice(evt.oldIndex, 1)
          this.dropCol.splice(evt.newIndex, 0, oldItem)
        }
      })
    }
  },
    created() {
    this.show()
  }
}
</script>
