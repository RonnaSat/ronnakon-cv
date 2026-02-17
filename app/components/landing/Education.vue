<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    :title="page.education.title"
    :ui="{
      container: '!p-0 gap-4 sm:gap-4',
      title: 'text-left text-xl sm:text-xl lg:text-2xl font-medium',
      description: 'mt-2'
    }"
  >
    <template #description>
      <div class="flex flex-col gap-6">
        <Motion
          v-for="(education, index) in page.education.items"
          :key="index"
          :initial="{ opacity: 0, transform: 'translateY(20px)' }"
          :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
          :transition="{ delay: 0.4 + 0.2 * index }"
          :in-view-options="{ once: true }"
          class="flex flex-col gap-2"
        >
          <div class="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-2 text-muted">
            <p class="text-sm font-medium">
              {{ education.institution }}
            </p>
            <span class="hidden sm:inline text-gray-300">•</span>
            <p class="text-sm text-gray-500">
              {{ education.date }}
            </p>
          </div>
          <p class="text-sm font-semibold">
            {{ education.degree }}
          </p>
        </Motion>
      </div>
    </template>
  </UPageSection>
</template>

<style scoped>

</style>
