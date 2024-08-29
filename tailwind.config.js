/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  content: ["./src/**/*.{css,js}", "./**/templates/**/*.html"],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: "1rem", // Default padding for container
        sm: "2rem", // Padding on small screens
        lg: "4rem", // Padding on large screens
        xl: "5rem", // Padding on extra large screens
      },
    },

    maxWidth: {
      xxs: "20rem", // 320px
      xs: "25rem", // 400px
      sm: "30rem", // 480px
      md: "35rem", // 560px
      lg: "48rem", // 768px
      xl: "64rem", // 1024px
      xxl: "80rem", // 1280px
      full: "100%",
    },

    boxShadow: {
      xxsmall: "0px 1px 2px rgba(0, 0, 0, 0.05)",
      xsmall: "0px 1px 3px rgba(0, 0, 0, 0.1), 0px 1px 2px rgba(0, 0, 0, 0.06)",
      small: "0px 4px 8px -2px rgba(0, 0, 0, 0.1), 0px 2px 4px -2px rgba(0, 0, 0, 0.06)",
      medium: "0px 12px 16px -4px rgba(0, 0, 0, 0.08), 0px 4px 6px -2px rgba(0, 0, 0, 0.03)",
      large: "0px 20px 24px -4px rgba(0, 0, 0, 0.08), 0px 8px 8px -4px rgba(0, 0, 0, 0.03)",
      xlarge: "0px 24px 48px -12px rgba(0, 0, 0, 0.18)",
      xxlarge: "0px 32px 64px -12px rgba(0, 0, 0, 0.14)",
      xxsmallDark: "0px 1px 2px rgba(212 ,212, 212, 0.05)",
      xsmallDark: "0px 1px 3px rgba(212 ,212, 212, 0.1), 0px 1px 2px rgba(212 ,212, 212, 0.06)",
      smallDark: "0px 4px 8px -2px rgba(212 ,212, 212, 0.1), 0px 2px 4px -2px rgba(212 ,212, 212, 0.06)",
      mediumDark: "0px 12px 16px -4px rgba(212 ,212, 212, 0.08), 0px 4px 6px -2px rgba(212 ,212, 212, 0.03)",
      largeDark: "0px 20px 24px -4px rgba(212 ,212, 212, 0.08), 0px 8px 8px -4px rgba(212 ,212, 212, 0.03)",
      xlargeDark: "0px 24px 48px -12px rgba(212 ,212, 212, 0.18)",
      xxlargeDark: "0px 32px 64px -12px rgba(212 ,212, 212, 0.14)",
    },

    fontSize: {
      xs: ["0.75rem", { lineHeight: "1.5" }], // 12px
      sm: ["0.875rem", { lineHeight: "1.5" }], // 14px
      base: ["1rem", { lineHeight: "1.5" }], // 16px
      md: ["1.125rem", { lineHeight: "1.5" }], // 18px
      lg: ["1.25rem", { lineHeight: "1.5" }], // 20px
      xl: ["1.25rem", { lineHeight: "1.4" }], // 20px
      "2xl": ["1.5rem", { lineHeight: "1.4" }], // 24px
      "3xl": ["1.75rem", { lineHeight: "1.4" }], // 28px
      "4xl": ["2rem", { lineHeight: "1.3" }], // 32px
      "5xl": ["2.25rem", { lineHeight: "1.2" }], // 36px
      "6xl": ["2.5rem", { lineHeight: "1.2" }], // 40px
      "7xl": ["2.75rem", { lineHeight: "1.2" }], // 40px
      "8xl": ["3rem", { lineHeight: "1.2" }], // 48px
      "9xl": ["3.25rem", { lineHeight: "1.2" }], // 52px
      "10xl": ["3.5rem", { lineHeight: "1.2" }], // 56px
    },

    fontFamily: {
      sans: ["Inter", ...defaultTheme.fontFamily.sans],
      serif: ["Georgia", "serif"],
    },
    colors: {
      primary: "#cb2238",
      secondary: "#D94E5A",

      accent: "#F2C4CD",
      neutral: {
        100: "#f5f5f5",
        200: "#e5e5e5",
        300: "#d4d4d4",
        500: "#737373",
        600: "#525252",
        700: "#404040",
        900: "#171717",
      },
      white: "#FFFFFF",
      black: "#000000",
      muted: "#9E9E9E",
      success: "#198754",
      danger: "#DC3545",
      warning: "#FFC107",
      info: "#0D6EFD",
    },

    extend: {
      keyframes: {
        "open-menu": {
          "0%": { transform: "scaleY(0)" },
          "80%": { transform: "scaleY(1.2)" },
          "100%": { transform: "scaleY(1)" },
        },
      },
      animation: {
        "open-menu": "open-menu .5s ease-in-out forwards",
      },
    },
  },

  corePlugins: {
    aspectRatio: false, // No changes needed
  },

  plugins: [
    require("@tailwindcss/aspect-ratio"),
    // Add any additional plugins here if needed
  ],
};
