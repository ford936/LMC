function switchLang(event) {
    if(event === 'en' && !window.location.pathname.includes('en/')) {
         window.location = '/en' + window.location.pathname
    } else if(event === 'ru' && window.location.pathname.includes('en/')) {
        let str = window.location.pathname
        window.location = str.replace('/en', '')
    }
}

function open_menu() {
    let element = document.getElementById("mySidebar")
    element.style.display = "block";
    setTimeout(() => element.style.opacity = 1, 250)
}

function close_menu() {
    let element = document.getElementById("mySidebar")
    element.style.opacity = 0
    setTimeout(() => element.style.display = "none", 250)
}
