## 2026-06-21 - Mobile Accessibility for Hover-Revealed Elements
**Learning:** Hiding actionable UI elements (like copy buttons) entirely until hover causes them to be completely inaccessible on touch devices since they lack a hover state.
**Action:** When adding hover-based reveals for interactive UI elements, always utilize responsive breakpoints (e.g., Tailwind's `sm:` prefix for `sm:opacity-0 sm:group-hover:opacity-100`) to ensure the elements remain visible and usable on mobile/touch devices. Additionally, include `focus-visible:opacity-100` for keyboard navigation.
