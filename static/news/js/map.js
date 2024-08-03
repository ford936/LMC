let YaMapsShown = false;
window.addEventListener('scroll', function() {
    if (!YaMapsShown) {
//        if (window.scrollY + window.innerHeight > document.body.offsetHeight - 700) {
            showYaMaps();
            YaMapsShown = true;
//        }
    }
});

function showYaMaps() {
     let script   = document.createElement("script");
     script.type  = "text/javascript";
     script.src   = "https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A60e0e3fd021039827d78d74be8dd374b73a933e6108c36f2e6552a8387bdecae&amp;width=600&amp;height=429&amp;lang=ru_RU&amp;scroll=true";

     let nameBlock = isElementVisible(document.querySelector('.map')) ? "map_container": "map_container_mobile"
     if(document.getElementById(nameBlock)) document.getElementById(nameBlock).appendChild(script);
}

function isElementVisible(element) {
    return (element.offsetWidth || element.offsetHeight || element.getClientRects().length)
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            timeout = null;
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
function handleResize() {
    let nameBlock = isElementVisible(document.querySelector('.map')) ? "map_container": "map_container_mobile"
     if(document.getElementById(nameBlock) &&!document.getElementById(nameBlock).querySelector('iframe')) {
        showYaMaps()
     }
}

window.addEventListener('resize', debounce(handleResize, 300));