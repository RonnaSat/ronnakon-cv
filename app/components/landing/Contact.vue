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
        <div class="flex items-center gap-3 group">
          <UIcon
            name="i-lucide-mail"
            class="w-5 h-5 text-primary"
          />
          <a
            :href="`mailto:${page.contact.email}`"
            class="hover:underline hover:text-primary transition-colors font-medium rounded-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary"
          >{{ page.contact.email }}</a>
          <UButton
            icon="i-lucide-copy"
            color="neutral"
            variant="ghost"
            size="xs"
            class="opacity-100 sm:opacity-0 sm:-translate-x-2 sm:group-hover:translate-x-0 sm:group-hover:opacity-100 sm:focus-visible:opacity-100 sm:focus-visible:translate-x-0 transition-all pointer-events-auto sm:pointer-events-none sm:group-hover:pointer-events-auto"
            aria-label="Copy email address"
            @click="copyToClipboard(page.contact.email, 'Email copied to clipboard')"
          />
        </div>
        <div class="flex items-center gap-3 group">
          <UIcon
            name="i-lucide-phone"
            class="w-5 h-5 text-primary"
          />
          <span class="font-medium">{{ page.contact.phone }}</span>
          <UButton
            icon="i-lucide-copy"
            color="neutral"
            variant="ghost"
            size="xs"
            class="opacity-100 sm:opacity-0 sm:-translate-x-2 sm:group-hover:translate-x-0 sm:group-hover:opacity-100 sm:focus-visible:opacity-100 sm:focus-visible:translate-x-0 transition-all pointer-events-auto sm:pointer-events-none sm:group-hover:pointer-events-auto"
            aria-label="Copy phone number"
            @click="copyToClipboard(page.contact.phone, 'Phone number copied to clipboard')"
          />
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
