// document.addEventListener("DOMContentLoaded", function () {
// 	$.get("http://127.0.0.1:8000/ajax/", function(data) {
//     	console.log(data);
// 	})
// 	var csrftoken = $("#csrftk").val();
// 	function csrfSafeMethod(method) {
// 		// these HTTP methods do not require CSRF protection
// 		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// 	}
	
// 	$.ajaxSetup({
// 		beforeSend: function (xhr, settings) {
// 			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
// 				xhr.setRequestHeader("X-CSRFToken", csrftoken);
// 			}
// 		}
// 	});
// 	$.post("http://127.0.0.1:8000/ajax/", function(data){
// 		console.log(data)
// 	})
// });