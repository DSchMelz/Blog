document.addEventListener("DOMContentLoaded", function () {
	document.querySelector(".ajaxbtn").addEventListener("click", function () {
		var output = document.querySelector("#placeLoad");
		var xhr = new XMLHttpRequest();

		xhr.open("GET", "http://127.0.0.1:8000/ajax", true);//гет запрос по ссылке на страницу с текстом, запрос - ассинхронный(страница не будет останавливать весь код)

		xhr.send();
		xhr.onreadystatechange = function() {
			if (xhr.readyState != 4) {//пока запрос не завершён(цифра 4 - завершён)
				return
			};
			if (xhr.status != 200) {//200- все ок
				// обработать ошибку
				alert(xhr.status + ": " + xhr.statusText); // пример вывода: 404: Not Found
			} 
			else {
				output.style.border = "1px solid #747474";
				output.style.padding = "10%";
				// вывести результат
				output.innerHTML = xhr.responseText; // responseText -- текст ответа.
			}
		};
		output.innerHTML = "Loading...";//пока загружается текст будет loading...
		
		xhr.onload = function() {//если запрос завершился успешно
			document.querySelector(".ajaxbtn").innerHTML = "Success!";
		}
	
		xhr.timeout = 30000; // 30 секунд (в миллисекундах)

		xhr.ontimeout = function() {//если запрос привысил время ожидания в 30 секунж
  			alert( 'Извините, запрос превысил максимальное время' );
		}
	});
});