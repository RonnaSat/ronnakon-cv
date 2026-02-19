<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    id="experience"
    :title="page.experience.title"
    :ui="{
      container: 'max-w-4xl mx-auto',
      title: 'text-2xl font-bold mb-6'
    }"
  >
    <div class="flex flex-col gap-8">
      <Motion
        v-for="(experience, index) in page.experience.items"
        :key="index"
        :initial="{ opacity: 0, transform: 'translateY(20px)' }"
        :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
        :transition="{ delay: 0.2 * index }"
        :in-view-options="{ once: true }"
        class="flex flex-col sm:flex-row gap-4 sm:gap-8"
      >
        <div class="sm:w-1/4 text-sm text-gray-500 dark:text-gray-400 font-medium whitespace-nowrap">
          {{ experience.date }}
        </div>
        <div class="sm:w-3/4 flex flex-col gap-2">
          <div class="flex items-center gap-2">
            <h3 class="text-lg font-semibold">
              {{ experience.position }}
            </h3>
            <span class="text-gray-400">@</span>
            <ULink
              class="inline-flex items-center gap-1 hover:text-primary transition-colors"
              :to="experience.company.url !== '#' ? experience.company.url : undefined"
              :target="experience.company.url !== '#' ? '_blank' : undefined"
            >
              <span class="font-medium">{{ experience.company.name }}</span>
            </ULink>
          </div>

          <ul class="list-disc list-outside ml-4 text-gray-500 dark:text-gray-400 space-y-1">
            <li
              v-for="(desc, dIndex) in experience.description"
              :key="dIndex"
            >
              {{ desc }}
            </li>
          </ul>
        </div>
      </Motion>
    </div>
  </UPageSection>
</template>

<style scoped>

</style>
