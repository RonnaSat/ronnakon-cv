<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    id="about"
    :title="page.about.title"
    :description="page.about.description"
    :ui="{
      container: 'max-w-4xl mx-auto',
      title: 'text-2xl font-bold',
      description: 'text-justify mt-4 text-gray-500 dark:text-gray-400'
    }"
  />
</template>

<style scoped>

</style>
