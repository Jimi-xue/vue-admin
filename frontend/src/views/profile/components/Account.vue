<template>
  <el-form :model="user" :rules="userRules">
    <el-form-item label="introduction" prop="introduction">
      <el-input v-model.trim="user.introduction" />
    </el-form-item>
    <el-form-item label="Email" prop="email">
      <el-input v-model.trim="user.email" />
    </el-form-item>
    <el-form-item label="Phone" prop="phone">
      <el-input v-model.trim="user.phone" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submit">Update</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { update_userinfo } from '@/api/user'
import { validEmail, validNumber } from '@/utils/validate'

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
  data() {
    const validateEmail = (rule, value, callback) => {
      if (!validEmail(value)) {
        callback(new Error('Please enter the email'))
      } else {
        callback()
      }
    }
    const validatePhone = (rule, value, callback) => {
      if (!validNumber(value)) {
        callback(new Error('Please enter the number'))
      } else if (value.length < 11) {
        callback(new Error('Please enter the phone number for 11'))
      } else {
        callback()
      }
    }
    const validateText = (rule, value, callback) => {
      console.log(value)
      if (!value) {
        callback(new Error('Please enter the introduction'))
      } else {
        callback()
      }
    }
    return {
      userRules: {
        introduction: [{ required: true, trigger: 'blur', validator: validateText }],
        email: [{ required: true, trigger: 'blur', validator: validateEmail }],
        phone: [{ required: true, trigger: 'blur', validator: validatePhone }]
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
