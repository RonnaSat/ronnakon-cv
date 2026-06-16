<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const props = defineProps<{
  links: NavigationMenuItem[]
}>()

const processedLinks = computed(() => {
  return props.links.map((link) => {
    const isAnchor = link.to && typeof link.to === 'string' && link.to.startsWith('#')
    if (!isAnchor) return link

    return {
      ...link,
      onSelect: (e: Event) => {
        e.preventDefault()
        const targetId = (link.to as string).substring(1)

        if (targetId === '') {
          window.scrollTo({ top: 0, behavior: 'smooth' })
          history.pushState(null, '', window.location.pathname + window.location.search)
          return
        }

        const targetElement = document.getElementById(targetId)
        if (targetElement) {
          const yOffset = -80 // Offset for the fixed header
          const y = targetElement.getBoundingClientRect().top + window.scrollY + yOffset
          window.scrollTo({ top: y, behavior: 'smooth' })
          history.pushState(null, '', `#${targetId}`)
        }
      }
    }
  })
})
</script>

<template>
  <div class="fixed top-2 sm:top-4 mx-auto left-1/2 transform -translate-x-1/2 z-10">
    <UNavigationMenu
      :items="processedLinks"
      variant="link"
      color="neutral"
      class="bg-muted/80 backdrop-blur-sm rounded-full px-2 sm:px-4 border border-muted/50 shadow-lg shadow-neutral-950/5"
      :ui="{
        link: 'px-2 py-1',
        linkLeadingIcon: 'hidden'
      }"
    >
      <template #list-trailing>
        <ColorModeButton />
      </template>
    </UNavigationMenu>
  </div>
</template>
