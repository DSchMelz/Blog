document.addEventListener("DOMContentLoaded", function () {
	document.querySelector(".ajaxbtn").addEventListener("click", function () {
		var output = document.querySelector("#placeLoad");
		var xhr = new XMLHttpRequest();

		xhr.open("GET", "http://127.0.0.1:8000/ajax", true); //гет запрос по ссылке на страницу с текстом, запрос - ассинхронный(страница не будет останавливать весь код)

		xhr.send();
		output.innerHTML = "Loading..."; //пока загружается текст будет loading...
		xhr.onreadystatechange = function () { //когда запрос завершился(хз чем отличается от события load(onload) и loadend(onloadend))
			if (xhr.readyState != 4) { //если запрос не завершён(цифра 4 - завершён)
				return
			}; //здесь оно ничего не делает, но может пригодиться
			if (xhr.status != 200) { //200- все ок
				// обработать ошибку
				alert(xhr.status + ": " + xhr.statusText); // пример вывода: 404: Not Found
			} else {
				output.style.border = "1px solid #747474";
				output.style.padding = "10%";
				// вывести результат
				output.innerHTML = xhr.responseText; // responseText -- текст ответа.
				document.querySelector(".ajaxbtn").innerHTML = "Success!";
			};
		};

		xhr.timeout = 30000; // 30 секунд (в миллисекундах)

		xhr.ontimeout = function () { //если запрос привысил время ожидания в 30 секунж
			alert('Извините, запрос превысил максимальное время');
		}
		//Печально, что если мы будем давать ссылку с html страницей, а не с httpresponce'ом как с /ajax, то responcetext будет выводить не текст, а html страницу(html страница в html странице)
		//С одной стороны это хорошо, но я хз можно и работать с responcetext, как то его обрабатывать
	});

});