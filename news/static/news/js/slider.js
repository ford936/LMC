const playVideo = (id)=> {
    let element = document.getElementById(id)
    let video = element.getElementsByTagName('video')[0]
    element.getElementsByTagName('button')[0].style.display = 'none'
    video.play()
    video.controls = true
}

function swiperDeclaring() {
    let slidesPerView = 3
    if(window.innerWidth <= 768){
        slidesPerView = 1
    } else if(window.innerWidth <= 1360) slidesPerView = 2
    return new Swiper(".mySwiper", {
      slidesPerView: slidesPerView,
      spaceBetween: 30,
      loop: false,
      pagination: {
            el: ".swiper-pagination",
            clickable: true,
      },
      navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
      },
    });
}
window.addEventListener('resize', () => {
    swiper = swiperDeclaring()

});
let swiper = swiperDeclaring()