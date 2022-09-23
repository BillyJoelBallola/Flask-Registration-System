const openBtn = document.querySelector(".hamburger")
const closeBtn = document.querySelector(".close")
const alertMsg = document.querySelector(".alert")
const closeAlertBtn = document.querySelector(".alert-close")
const navLinks = document.querySelector(".nav-links")
const registeredContainer = document.querySelector('.registered')
const tableRow = document.querySelectorAll("table tr")
const allCheckBox = document.querySelectorAll("table input")
const checkBox = document.querySelector(".select-all")

openBtn.addEventListener("click", ()=> {
    if (openBtn.classList.contains("show")){
        openBtn.classList.remove("show")
        closeBtn.classList.add("show")
        navLinks.style.top = "4em"
    }else{
        openBtn.classList.add("show")
        closeBtn.classList.remove("show")
    }
})

closeBtn.addEventListener("click", ()=> {
    if (closeBtn.classList.contains("show")){
        closeBtn.classList.remove("show")
        openBtn.classList.add("show")
        navLinks.style.top = "-20em"
    }else{
        closeBtn.classList.add("show")
        openBtn.classList.remove("show")
    }
})

window.addEventListener("scroll", ()=> {
    for (row in tableRow) {
        if (row > 5){
            registeredContainer.style.height = "100%"
        }
    }
})

closeAlertBtn.addEventListener("click", ()=> {
    alertMsg.style.display = "none"
})