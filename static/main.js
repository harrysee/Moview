(function($) {
	console.log("dd");
	var	$window = $(window),
		$body = $('body');

		// images preview
	  $('input[type=file]').on('change',function(){
		if(window.FileReader){
		  	var filename = $(this)[0].files[0].name;
		} else {
		 	var filename = $(this).val().split('/').pop().split('\\').pop();
		}
		$(this).siblings('label').text(filename);
		console.log("해이이");
	  });
})(jQuery);