/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./views/**/*.ejs",    // Verzeichnis für EJS-Dateien
    "./public/**/*.html",   // falls du HTML-Dateien verwendest
    "./src/**/*.js",        // falls du JavaScript-Dateien verwendest
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
