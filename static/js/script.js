const likeBtns = document.querySelectorAll('.like');
likeBtns.forEach((item) => {
    item.addEventListener('click', function() {
        item.children[0].classList.toggle('like-animation');
        item.children[0].classList.toggle('fas');
    })
})

const searchTxt = document.querySelector(".search-input");
const searchBtn = document.querySelector(".search-btn");
const formBtn = document.querySelector(".form-btn");

function search(event) {
    event.preventDefault();
    searchTxt.focus();
    searchTxt.classList.toggle("search-input-active");
    formBtn.classList.toggle("form-btn-active");
}

searchBtn.addEventListener('click', search);

const currentTheme = localStorage.getItem("theme");
if (currentTheme) {
    document.documentElement.setAttribute("data-theme", currentTheme);
}

if (currentTheme == "light") {
    document.querySelector(".fa-sun").style.display = "none";
} 
else {
    document.querySelector(".fa-moon").style.display = "none";
}

const lightBtn = document.querySelector(".fa-sun");
const darkBtn = document.querySelector(".fa-moon");

lightBtn.addEventListener("click", function () {
    document.documentElement.setAttribute("data-theme", "light");
    localStorage.setItem("theme", "light");
    this.style.display = "none";
    darkBtn.style.display = "inline-block";
    document.body.style.transition = "all 0.3s";
});

darkBtn.addEventListener("click", function () {
    document.documentElement.setAttribute("data-theme", "dark");
    localStorage.setItem("theme", "dark");
    this.style.display = "none";
    lightBtn.style.display = "inline-block";
    document.body.style.transition = "all 0.3s";
});

document.addEventListener("keydown", function (event) {
    if (event.code == "KeyF" && event.ctrlKey) {
        search(event)
    }
});