
## 2024-06-20 - Mobile Accessibility Pattern for Hover States
**Learning:** Hiding interactive cues (like arrow icons) behind `group-hover` classes creates a critical accessibility barrier for mobile and touch device users, as they cannot trigger the hover state to see the call-to-action.
**Action:** When adding hover-based reveals for interactive UI elements, utilize responsive breakpoints (e.g., Tailwind's `sm:opacity-0`) to ensure the elements remain visible by default (`opacity-100`) on touch devices where hover is unavailable.
