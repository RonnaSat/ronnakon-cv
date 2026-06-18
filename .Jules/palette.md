## 2024-05-14 - Interactive Element Copy Controls
**Learning:** Found an opportunity to improve contact information accessibility and ease-of-use by providing direct "copy to clipboard" buttons for email and phone numbers, which is a common action users want to take on portfolio contact pages.
**Action:** Implemented a visible-on-hover / focus-visible pattern for copy buttons next to the contact links, paired with screen reader labels (aria-label) and toast notifications for success feedback. Used existing utility function `copyToClipboard`.
