<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    v-if="page.contact"
    title="Contact"
    :ui="{
      container: '!p-0 gap-4 sm:gap-4',
      title: 'text-left text-xl sm:text-xl lg:text-2xl font-medium',
      description: 'mt-2'
    }"
  >
    <template #description>
      <div class="flex flex-col gap-4 text-gray-500 dark:text-gray-400">
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-mail"
            class="w-5 h-5"
          />
          <a
            :href="`mailto:${page.contact.email}`"
            class="hover:underline hover:text-primary transition-colors"
          >{{ page.contact.email }}</a>
        </div>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-phone"
            class="w-5 h-5"
          />
          <span>{{ page.contact.phone }}</span>
        </div>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-user"
            class="w-5 h-5"
          />
          <span>{{ page.contact.name }}</span>
        </div>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-map-pin"
            class="w-5 h-5"
          />
          <span>{{ page.contact.location }}</span>
        </div>
      </div>
    </template>
  </UPageSection>
</template>
