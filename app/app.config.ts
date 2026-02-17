export default defineAppConfig({
  global: {
    picture: {
      dark: '', // Placeholder or remove if no image
      light: '', // Placeholder or remove if no image
      alt: 'Ronnakon Nisaensat'
    },
    email: 'ronnakornniseansut@gmail.com',
    meetingLink: 'mailto:ronnakornniseansut@gmail.com',
    available: true
  },
  ui: {
    colors: {
      primary: 'blue',
      neutral: 'neutral'
    },
    pageHero: {
      slots: {
        container: 'py-18 sm:py-24 lg:py-32',
        title: 'mx-auto max-w-xl text-pretty text-3xl sm:text-4xl lg:text-5xl',
        description: 'mt-2 text-md mx-auto max-w-2xl text-pretty sm:text-md text-muted'
      }
    }
  },
  footer: {
    credits: `Ronnakon Nisaensat • © ${new Date().getFullYear()}`,
    colorMode: false,
    links: [{
      'icon': 'i-simple-icons-github',
      'to': 'https://github.com/ronnakon-cv', // Assuming this is the user's github based on repo name
      'target': '_blank',
      'aria-label': 'Ronnakon on GitHub'
    }]
  }
})
