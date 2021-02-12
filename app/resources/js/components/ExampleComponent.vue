<template>
  <h1>Hello {{ greeting }}</h1>
</template>
<script>
import {ref} from 'vue';
export default {
  setup(){
    const greeting = ref("I am A Vue Component in App")

    return {
      greeting
    }
  }
}
</script>