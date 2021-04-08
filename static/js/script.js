const currentTheme = localStorage.getItem("theme");
if (currentTheme) {
    document.documentElement.setAttribute("data-theme", currentTheme);
}

const lightBtn = document.querySelector(".theme__light");
const darkBtn = document.querySelector(".theme__dark");

if (currentTheme == "light") {
    lightBtn.style.display = "none";
} 
else {
    darkBtn.style.display = "none";
}

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

const likeBtns = document.querySelectorAll('.like');
likeBtns.forEach((item) => {
    item.addEventListener('click', function() {
        item.children[0].classList.toggle('like_selected');
        item.children[0].classList.toggle('fas');
    })
})

const searchBtn = document.querySelector('.search__submit');
const searchInput = document.querySelector('.search__input');

// да, без второй кнопочки немного костыльно, но пойдет)))
// работает не идеально, но, что смог, я сделал. Есть один небольшой баг, но как его устранить я уже хз
searchBtn.addEventListener('click', function() {
    searchInput.focus();
    
    searchBtn.addEventListener('click', function() {
        if (searchInput.value) {//если есть введенный текст, то можно и при следующем клике отправлять форму, а если инпут пустой, то нельзя
            searchBtn.setAttribute('type', 'submit');
        }
    })
    searchBtn.setAttribute('type', 'button');
})