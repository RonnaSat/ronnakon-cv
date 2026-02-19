<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    v-if="page.contact"
    id="contact"
    title="Contact"
    :ui="{
      container: 'max-w-4xl mx-auto',
      title: 'text-2xl font-bold mb-6'
    }"
  >
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-gray-600 dark:text-gray-300">
      <div class="flex flex-col gap-4">
        <p class="text-lg">
          Feel free to reach out for collaborations or just to say hi!
        </p>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-mail"
            class="w-5 h-5 text-primary"
          />
          <a
            :href="`mailto:${page.contact.email}`"
            class="hover:underline hover:text-primary transition-colors font-medium"
          >{{ page.contact.email }}</a>
        </div>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-phone"
            class="w-5 h-5 text-primary"
          />
          <span class="font-medium">{{ page.contact.phone }}</span>
        </div>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-map-pin"
            class="w-5 h-5 text-primary"
          />
          <span class="font-medium">{{ page.contact.location }}</span>
        </div>
      </div>
    </div>
  </UPageSection>
</template>
