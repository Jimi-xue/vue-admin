<template>
  <div class="app-container documentation-container">
    <a class="document-btn" target="_blank" href="http://baidu.com">test1</a>
    <dropdown-menu class="document-btn" :items="articleList" title="test3" />
    <a class="document-btn" target="_blank" href="http://jianshu.com">test2</a>
  </div>
</template>

<script>
import DropdownMenu from '@/components/Share/DropdownMenu'

export default {
  name: 'Documentation',
  components: { DropdownMenu },
  data() {
    return {
      articleList: [
        { title: 'a1', href: '/charts/keyboard' },
        { title: 'a2', href: '/charts/line' }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.documentation-container {
  margin: 50px;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;

  .document-btn {
    flex-shrink: 0;
    display: block;
    cursor: pointer;
    background: black;
    color: white;
    height: 60px;
    padding: 0 16px;
    margin: 16px;
    line-height: 60px;
    font-size: 20px;
    text-align: center;
  }
}
</style>
