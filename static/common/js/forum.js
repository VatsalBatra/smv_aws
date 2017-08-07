var forum = (function(){

	function add_question(){
		console.log("popopopopop")
		var name = email.value
		var question  = text.value
		console.log(question)
		if (question.length <=1 ) {
			$('#error').html('please enter the query before clicking submit')
				return;
		}
		$.ajax({
			url:'add/',
			method:'GET',
			data:{
				'name':name,
				'text':question
			},
			success:function(content){
			$("#question").html(" ")
			$('#text').val("");
			$('#email').val("");
				$('#error').html('')
				$.ajax({
					url:'content/',
					method:'GET',
					// data:{

					// },
					success:function(content){
					console.log("qweeqweqwweqw")
						for(var i =0 ;i<content.heading.length;i++){

							$("#question").append("<div><p class='back_content'>" + content.question[i] + "</p>" + "-" + content.heading[i]+ "</div>")
						$("#question").append("	<input type = 'ans_text' name = 'first_name' class ='ans_email'/><br/><div class = ans_div_back'><textarea rows ='10' cols = '70' name = 'ans_description' class = 'ans_text' placeholder= 'enter your query...'' ></textarea><br/><button class ='ans_submit'>Submit</button></div>")	

						}


					},error:function(){

					}
				})
			},
			error:function(){
				console.log("problem_1");

			}

		})
	}
	$(document).on('ajaxComplete',function(){
		$(".ans_submit").off('click').click(function(){
		console.log($(this).parent().prev().prev().prev().find("p").text())
		console.log($(this).siblings()[0].value)
		$.ajax({
			url:'addans/',
			method:'GET',
			// data:{
			// 	'name':name,
			// 	'text':answer
			// },
			success:function(content){
			console.log("qweeqweqwweqwSTEP1")
			// $("#question").html(" ")
			// $('#text').val("");
			// $('#email').val("");
			// 	$('#error').html('')
				$.ajax({
					url:'upload/',
					method:'GET',
					// data:{

					// },
					success:function(content){
					console.log("qweeqweqwweqw")
						// for(var i =0 ;i<content.heading.length;i++){
						// 	$("#question").append("<div><p>" + content.answer[i] + "</p>" + "-" + content.heading[i]+ "</div>")
						// $("#question").append("	<input type = 'ans_text' name = 'first_name' id ='email'/><br/><textarea rows ='10' cols = '70' name = 'ans_description' id = 'text' placeholder= 'enter your query...'' ></textarea><br/><button id ='ans_submit'>Submit</button>")	

						// }


					},error:function(){

					}
				})
			},
			error:function(){
				console.log("problem_2");

			}

		})
		})
	})

	function init(config){
		submit_click =document.getElementById(config['submit'])
		email =document.getElementById(config['email'])
		text =document.getElementById(config['text'])
		box = document.getElementById(config['box'])
		ans_submit = document.getElementById(config['ans_submit'])
		// ans_submit.addEventListener('click',add_answer)
		submit_click.addEventListener('click',add_question) 
	

	}
	
	return{
		init:init
	}

}());



