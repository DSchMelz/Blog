  var like = $(".like");
  like.click(function () {
  	var heart = $(this).children();
  	heart.toggleClass("anim");
  	heart.toggleClass("fas");
  });

  var search_txt = document.querySelector(".search-input");
  var search_btn = document.querySelector(".search-btn");
  var form_btn = document.querySelector(".form-btn");
  search_btn.onclick = function (event) {
  	event.preventDefault();
  	search_txt.focus();
  	search_txt.classList.toggle("search-input-active");
  	form_btn.classList.toggle("form-btn-active");
  }

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

var lightBtn = document.querySelector(".fa-sun");
var darkBtn = document.querySelector(".fa-moon");

lightBtn.addEventListener("click", function() {
    document.documentElement.setAttribute("data-theme", "light");
    localStorage.setItem("theme", "light");
    this.style.display = "none";
    darkBtn.style.display = "inline-block";
});

darkBtn.addEventListener("click", function() {
    document.documentElement.setAttribute("data-theme", "dark");
    localStorage.setItem("theme", "dark");
    this.style.display = "none";
    lightBtn.style.display = "inline-block";
});

document.addEventListener('keydown', function(event) {
  event.preventDefault();//отключаем поиск по странице от браузера
  if (event.code == "KeyF" && event.ctrlKey) {
    search_txt.focus();
    search_txt.classList.toggle("search-input-active");
  	form_btn.classList.toggle("form-btn-active");
  }
});