<template>
  <div class="app-container">
    <el-button
      type="success"
      size="small"
      icon="el-icon-circle-check-outline"
      @click="add_line()"
    >
      添加数据
    </el-button>
    <el-table :data="tableData" border fit highlight-current-row style="width: 100%" row-key="id">
      <el-table-column align="center" label="ID">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleFetchPv(row.id)">{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="hostname">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.hostname" class="edit-input" size="small" />
          </template>
          <span v-else>{{ row.hostname }}</span>
        </template>
        <el-input class="edit-input" size="small" />
      </el-table-column>
      <el-table-column align="center" label="ip">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.ip_addr" class="edit-input" size="small" />
          </template>
          <span v-else>{{ row.ip_addr }}</span>
        </template>
        <el-input class="edit-input" size="small" />
      </el-table-column>
      <el-table-column align="center" label="asset">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.asset_id" class="edit-input" size="small" />
          </template>
          <span v-else>{{ row.asset_id }}</span>
        </template>
        <el-input class="edit-input" size="small" />
      </el-table-column>
      <el-table-column align="center" label="remark">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.remark" class="edit-input" size="small" />
          </template>
          <span v-else>{{ row.remark }}</span>
        </template>
        <el-input class="edit-input" size="small" />
      </el-table-column>
      <el-table-column align="center" label="time">
        <template slot-scope="{row}">
          <span>{{ row.add_time }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="操作">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <span class="link-type" @click="add_host(row.hostname,row.ip_addr,row.asset_id,row.remark)">添加</span>
          </template>
          <span v-else class="link-type" @click="delete_host(row.hostname)">删除</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>

import { getHosts, setHost, delHost } from '@/api/assets'
export default {
  data() {
    return {
      tableData: [],
      form: {
        hostname: '',
        ip_addr: '',
        asset_id: '',
        remark: ''
      },
      new_data: {}
    }
  },
  created() {
    this.show()
  },
  methods: {
    handleFetchPv(pv) {
      getHosts(pv).then(response => {
        this.pvData = response
        this.dialogPvVisible = true
      })
    },
    gethost() {
      return new Promise((resolve, reject) => {
        getHosts().then(response => {
          const datas = response
          console.log(datas)
          this.tableData = datas
          resolve(true)
        }).catch(err => {
          console.log(err)
          reject(false)
        })
      })
    },
    show() {
      return new Promise((resolve, reject) => {
        this.gethost()
      })
    },
    delete_host(hostname) {
      delHost(hostname).then(response => {
        this.gethost()
      })
    },
    add_line() {
      this.new_data = { 'hostname': null, 'ip_addr': null, 'asset_id': null, 'remark': null, 'add_time': null, 'id': null, 'edit': '1' }
      this.tableData.push(this.new_data)
    },
    add_host(hostname, ip_addr, asset_id, remark) {
      setHost({ 'hostname': hostname, 'ip_addr': ip_addr, 'asset_id': asset_id, 'remark': remark }).then(response => {
        this.gethost()
      })
    }
  }
}
</script>

