/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/crudweb/*.html',  // Asegúrate de que coincida con la estructura de tu proyecto
    './crudweb/**/*.{py,html}',  // Incluye los archivos de tus vistas y templates
    './static/**/*.{js,jsx,ts,tsx,html}', // Agrega cualquier otro archivo que necesite Tailwind
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};


