<template>
  <el-form>
    <el-form-item label="introduction">
      <el-input v-model.trim="user.introduction" />
    </el-form-item>
    <el-form-item label="Email">
      <el-input v-model.trim="user.email" />
    </el-form-item>
    <el-form-item label="Phone">
      <el-input v-model.trim="user.phone" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submit">Update</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { update_userinfo } from '@/api/user'
export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          introduction: '',
          email: '',
          phone: ''
        }
      }
    }
  },
  methods: {
    submit() {
      update_userinfo({
        'introduction': this.user.introduction,
        'email': this.user.email,
        'phone': this.user.phone
      }).then(response => {
        if (response === 200) {
          this.$message({
            message: 'User information has been updated successfully',
            type: 'success',
            duration: 5 * 1000
          })
        } else {
          this.$message({
            message: response,
            type: 'error',
            duration: 5 * 1000
          })
        }
      }).catch(err => {
        // eslint-disable-next-line no-undef
        reject(err)
      })
    }
  }
}
</script>
