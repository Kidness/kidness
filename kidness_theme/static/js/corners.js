function hasBorderRadius() {
		  var element = document.documentElement;
		  var style = element.style;
		  if (style) {
			  var b = style.borderRadius;
			  var t = document.getElementById("main-container").style;
			  
			  return style.borderRadius == "" ||
			    style.MozBorderRadius == "" ||
			    style.WebkitBorderRadius == "" ||
			    style.KhtmlBorderRadius == "";
		  }
		  return null;
} 
(function( $ ){
	  $.fn.formCorners = function(radius) {  
		  return this.each(function(){
			  var input = $(this);
			  if(input.attr("type") != "hidden") {
				  var input_background = input.css("background-color");
				  var input_border = input.css("border-color");
				  input_border = input_background;
				  input.css("border", "none");
				  var wrap_width = parseInt(input.css("width")) + 15;
				  var wrapper = input.wrap("<div></div>").parent();
				  var border = wrapper.wrap("<div></div>").parent();
				  wrapper.css("background-color", input_background).css("padding", "1px");
				  wrapper.css("background-color", input_border).css("width", wrap_width + "px").css("padding", "1px");
				  wrapper.corner("round " + radius + "px");
				  border.corner("round " + radius + "px");
		  	  }
		  });
	  };
	})( jQuery );
