<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    :title="page.skills.title"
    :ui="{
      container: '!p-0 gap-4 sm:gap-4',
      title: 'text-left text-xl sm:text-xl lg:text-2xl font-medium',
      description: 'mt-2'
    }"
  >
    <template #description>
      <div class="flex flex-col gap-6">
        <Motion
          v-for="(category, index) in page.skills.categories"
          :key="index"
          :initial="{ opacity: 0, transform: 'translateY(20px)' }"
          :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
          :transition="{ delay: 0.2 * index }"
          :in-view-options="{ once: true }"
        >
          <p class="text-md font-semibold text-gray-900 dark:text-white mb-3">
            {{ category.name }}
          </p>
          <div class="flex flex-wrap gap-2">
            <UBadge
              v-for="skill in category.items"
              :key="skill"
              :label="skill"
              variant="subtle"
              size="md"
              class="rounded-full font-normal"
            />
          </div>
        </Motion>
      </div>
    </template>
  </UPageSection>
</template>
