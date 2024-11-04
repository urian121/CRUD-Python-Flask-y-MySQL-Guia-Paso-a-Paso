document.addEventListener('DOMContentLoaded', function () {
/** Efecto View Transitions */
const content = document.querySelector('.main-panel')
const links = document.querySelectorAll('a.nav-link') // Solo los enlaces del menú

links.forEach((link) => {
    link.addEventListener('click', function (e) {
    e.preventDefault()
    content.classList.add('fade-out')

    setTimeout(() => {
        window.location.href = link.href
    }, 300)
    })
})
content.classList.add('fade-in')
/* fin del efecto View Transitions */

let tables = document.querySelectorAll('table')
if (tables.length == 0) return
tables.forEach((table) => {
    // Captura el id de la tabla actual
    let tableId = table.id

    // Inicializa DataTables para cada tabla usando su id
    $(`#${tableId}`).DataTable({
    pageLength: 10,
    language: {
        url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json'
    }
    })
})

const currentPath = window.location.pathname
const baseUrl = 'ruta-aqui'
const navLinks = document.querySelectorAll('.nav-link')

console.log('Current Path:', currentPath) // Para verificar el valor

navLinks.forEach((link) => {
    // Combina el $base_static con el href del enlace para obtener la URL completa
    const linkPath = new URL(link.getAttribute('href'), baseUrl).pathname

    console.log('Link Path:', linkPath) // Para verificar el valor

    // Compara el linkPath con el currentPath
    if (currentPath === linkPath || currentPath === linkPath + '/') {
    link.classList.add('active') // Agrega clase al enlace activo
    link.closest('.nav-item').classList.add('active') // Agrega clase al contenedor nav-item
    }
})
})