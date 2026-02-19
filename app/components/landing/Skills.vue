<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    id="skills"
    :title="page.skills.title"
    :ui="{
      container: 'max-w-4xl mx-auto',
      title: 'text-2xl font-bold mb-6'
    }"
  >
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <Motion
        v-for="(category, index) in page.skills.categories"
        :key="index"
        :initial="{ opacity: 0, transform: 'translateY(20px)' }"
        :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
        :transition="{ delay: 0.1 * index }"
        :in-view-options="{ once: true }"
        class="flex flex-col gap-4"
      >
        <h3 class="text-lg font-semibold border-b pb-2 border-gray-200 dark:border-gray-800">
          {{ category.name }}
        </h3>
        <div class="flex flex-wrap gap-2">
          <UBadge
            v-for="skill in category.items"
            :key="skill"
            :label="skill"
            variant="subtle"
            size="md"
            class="rounded-full font-normal px-3 py-1"
          />
        </div>
      </Motion>
    </div>
  </UPageSection>
</template>
