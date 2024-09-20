//function openServices(content, title, img) {
//    let modalServices =  `
//    <div class="modalBackground" id="modalService" onclick="closeServices(event)" style="opacity:0">
//        <div class="modalActive container">
//            <button onclick="closeServices('close')">
//                <svg width="23" height="23" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
//                    <path d="M1 1L22 22" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
//                    <path d="M1 22L22 1" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
//                </svg>
//            </button>
//            <img src="${img}" alt="img"/>
//            <h4>${title}</h4>
//            <p>${content}</p>
//        </div>
//    </div>
//    `
//    document.body.insertAdjacentHTML('afterbegin', modalServices)
//    setTimeout(()=>{
//        document.getElementsByClassName('modalBackground')[0].style.opacity = 1
//    }, 0)
//}
//function closeServices(event) {
//    if(event?.target?.className === 'modalBackground' || event === 'close'){
//        document.getElementsByClassName('modalBackground')[0].style.opacity = 0
//        setTimeout(()=>{
//            document.getElementById("modalService").remove();
//        }, 200)
//    }
//}