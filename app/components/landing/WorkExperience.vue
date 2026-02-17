<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    :title="page.experience.title"
    :ui="{
      container: '!p-0 gap-4 sm:gap-4',
      title: 'text-left text-xl sm:text-xl lg:text-2xl font-medium',
      description: 'mt-2'
    }"
  >
    <template #description>
      <div class="flex flex-col gap-6">
        <Motion
          v-for="(experience, index) in page.experience.items"
          :key="index"
          :initial="{ opacity: 0, transform: 'translateY(20px)' }"
          :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
          :transition="{ delay: 0.4 + 0.2 * index }"
          :in-view-options="{ once: true }"
          class="flex flex-col gap-2"
        >
          <div class="flex items-center flex-wrap gap-2 text-muted">
            <p class="text-sm min-w-fit">
              {{ experience.date }}
            </p>
            <USeparator class="hidden sm:block" />
            <div class="flex items-center gap-1 flex-wrap">
              <span class="text-sm font-semibold">{{ experience.position }}</span>
              <span class="text-sm">at</span>
              <ULink
                class="inline-flex items-center gap-1"
                :to="experience.company.url !== '#' ? experience.company.url : undefined"
                :target="experience.company.url !== '#' ? '_blank' : undefined"
                :style="{ color: experience.company.color }"
              >
                <span class="font-medium">{{ experience.company.name }}</span>
                <UIcon :name="experience.company.logo" />
              </ULink>
            </div>
          </div>

          <ul class="list-disc list-inside text-sm text-gray-500 dark:text-gray-400 pl-4 space-y-1">
            <li
              v-for="(desc, dIndex) in experience.description"
              :key="dIndex"
            >
              {{ desc }}
            </li>
          </ul>
        </Motion>
      </div>
    </template>
  </UPageSection>
</template>

<style scoped>

</style>
