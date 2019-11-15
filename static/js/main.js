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

  var modal = document.getElementById("modal");
  var settings = document.getElementById("settings");
  var close = document.getElementById("close");
  
  settings.onclick = function () {
  	settings.classList.add("rotate");
  	modal.style.display = "block";
  }

close.addEventListener("click", closeModal);

function closeModal() {
  	modal.style.display = "none";
}

  const currentTheme = localStorage.getItem("theme");
  if (currentTheme) {
  	document.documentElement.setAttribute("data-theme", currentTheme);
  }

  document.getElementById("lightBtn").onclick = function () {
  	document.documentElement.setAttribute("data-theme", "light");
  	localStorage.setItem("theme", "light");
  }

  document.getElementById("darkBtn").onclick = function () {
  	document.documentElement.setAttribute("data-theme", "dark");
  	localStorage.setItem("theme", "dark");
  }