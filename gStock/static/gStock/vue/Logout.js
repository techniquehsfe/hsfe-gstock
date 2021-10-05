export default {
  created () {
    this.$store.dispatch('logoutUser')
      .then(() => {
        this.$router.push({ name: 'home' })
      })
  }
}

<style scoped>
</style>
