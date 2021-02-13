<template>
  <h1>Hello {{ greeting }}</h1>
</template>
<script>
import {ref} from 'vue';
export default {
  setup(){
    const greeting = ref("Welcome To Dashboard.")

    return {
      greeting
    }
  }
}
</script>