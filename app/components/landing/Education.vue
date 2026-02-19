<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    id="education"
    :title="page.education.title"
    :ui="{
      container: 'max-w-4xl mx-auto',
      title: 'text-2xl font-bold mb-6'
    }"
  >
    <div class="flex flex-col gap-6">
      <Motion
        v-for="(education, index) in page.education.items"
        :key="index"
        :initial="{ opacity: 0, transform: 'translateY(20px)' }"
        :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
        :transition="{ delay: 0.2 * index }"
        :in-view-options="{ once: true }"
        class="flex flex-col sm:flex-row gap-4 sm:gap-8 justify-between"
      >
        <div class="sm:w-1/4 text-sm text-gray-500 dark:text-gray-400 font-medium whitespace-nowrap">
          {{ education.date }}
        </div>
        <div class="sm:w-3/4 flex flex-col gap-1">
          <h3 class="text-lg font-semibold">
            {{ education.institution }}
          </h3>
          <p class="text-gray-500 dark:text-gray-400">
            {{ education.degree }}
          </p>
        </div>
      </Motion>
    </div>
  </UPageSection>
</template>

<style scoped>

</style>
