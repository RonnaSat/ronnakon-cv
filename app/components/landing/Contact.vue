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
            class="w-5 h-5 text-primary shrink-0"
          />
          <a
            :href="`mailto:${page.contact.email}`"
            class="hover:underline hover:text-primary transition-colors font-medium"
          >{{ page.contact.email }}</a>
          <UTooltip text="Copy email">
            <UButton
              icon="i-lucide-copy"
              color="neutral"
              variant="ghost"
              size="xs"
              aria-label="Copy email address"
              class="opacity-100 sm:opacity-0 sm:group-hover:opacity-100 focus-visible:opacity-100 transition-opacity"
              @click="copyToClipboard(page.contact.email, 'Email copied to clipboard')"
            />
          </UTooltip>
        </div>
        <div class="flex items-center gap-3 group">
          <UIcon
            name="i-lucide-phone"
            class="w-5 h-5 text-primary shrink-0"
          />
          <a
            :href="`tel:${page.contact.phone}`"
            class="hover:underline hover:text-primary transition-colors font-medium"
          >{{ page.contact.phone }}</a>
          <UTooltip text="Copy phone number">
            <UButton
              icon="i-lucide-copy"
              color="neutral"
              variant="ghost"
              size="xs"
              aria-label="Copy phone number"
              class="opacity-100 sm:opacity-0 sm:group-hover:opacity-100 focus-visible:opacity-100 transition-opacity"
              @click="copyToClipboard(page.contact.phone, 'Phone number copied to clipboard')"
            />
          </UTooltip>
        </div>
        <div class="flex items-center gap-3">
          <UIcon
            name="i-lucide-map-pin"
            class="w-5 h-5 text-primary shrink-0"
          />
          <a
            :href="`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(page.contact.location)}`"
            target="_blank"
            rel="noopener noreferrer"
            class="hover:underline hover:text-primary transition-colors font-medium"
          >{{ page.contact.location }}</a>
        </div>
      </div>
    </div>
  </UPageSection>
</template>
