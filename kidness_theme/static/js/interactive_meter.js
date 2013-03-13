function show_begunok(e, selectedPosLeft, selectedPosRight){
	var mousePos = e.pageX;
	var linejkaPosLeft = $("#begunok").parent().position().left;
	var begunPosCenter = mousePos - linejkaPosLeft;
	var begunPosLeft = mousePos - linejkaPosLeft - 78;
	var begunPosRight = begunPosLeft + 156;
	if (begunPosLeft < 0) {
		begunPosLeft = 0;
	}
	if (begunPosRight  > $("#begunok").parent().width()) {
		begunPosLeft = $("#begunok").parent().width() - 156;
	}
	var showBegunok = true;
	if (selectedPosLeft || selectedPosRight) {
		if (selectedPosLeft < begunPosLeft && begunPosLeft < selectedPosRight) {
			begunPosLeft = selectedPosRight;
		}
		if (selectedPosLeft < begunPosRight && begunPosRight < selectedPosRight) {
			begunPosLeft = selectedPosLeft-156;
		}
		if (selectedPosLeft < begunPosCenter && begunPosCenter < selectedPosRight) {
			showBegunok = false;
		}
	}
	if(showBegunok) {
		$("#begunok").attr("style","width: 156px; height: 89px; position: absolute; left: " + begunPosLeft + "px; top: 3px; padding: 0px; border: 0px none; background:url('/media/kidness_theme/img/begunok3.png') no-repeat center top;opacity:0.5;");
	} else {
		$("#begunok").attr("style","display:none");
	}
}

function show_begunok_descrete_old(e, selectedPosLeft, selectedPosRight){
	var mousePos = e.pageX;
	var begunok_name = "begunok.png";
	var begunokWidth = "156px";
	var linejkaPosLeft = $("#begunok").parent().position().left;
	var begunPosLeft = mousePos - linejkaPosLeft;
	var begunPosRight = begunPosLeft + 156;
	if (begunPosLeft < 0) {
		begunPosLeft = 0;
	}
	if (0 < begunPosLeft && begunPosLeft < 190) {
		begunok_name = "begunok.png";
		begunokWidth = 200;
		begunPosLeft = 0;
	}
	if (190 < begunPosLeft && begunPosLeft < 331) {
		begunok_name = "begunok.png";
		begunokWidth = 156;
		begunPosLeft = 180;
	}
	if (331 < begunPosLeft && begunPosLeft < 472) {
		begunok_name = "begunok.png";
		begunokWidth = 156;
		begunPosLeft = 321;
	}
	if (472 < begunPosLeft && begunPosLeft < 652) {
		begunok_name = "begunok.png";
		begunokWidth = 190;
		begunPosLeft = 462;
	}
	begunPosRight = begunPosLeft + begunokWidth;
	if (begunPosRight  > $("#begunok").parent().width()) {
		begunPosLeft = $("#begunok").parent().width() - begunokWidth;
	}
	var showBegunok = true;
	if (selectedPosLeft || selectedPosRight) {
		if (selectedPosLeft < begunPosLeft && begunPosLeft < selectedPosRight) {
			begunPosLeft = selectedPosRight;
		}
		if (selectedPosLeft < begunPosRight && begunPosRight < selectedPosRight) {
			begunPosLeft = selectedPosLeft-begunokWidth;
		}
	}
	if(showBegunok) {
		$("#begunok").attr("style","z-index:2000;width: " + begunokWidth + "px; height: 89px; position: absolute; left: " + begunPosLeft + "px; top: 3px; padding: 0px; border: 0px none; background:url('/media/kidness_theme/img/" + begunok_name + "') no-repeat center top;opacity:0.5;");
	} else {
		$("#begunok").attr("style","display:none");
	}
}

function show_begunok_descrete_old2(e, selectedPosLeft, selectedPosRight){
	var mousePos = e.pageX;
	var linejkaPosLeft = $(".begunok").parent().position().left;
	var begunokWidth = 190;
	var begunPosLeft = mousePos - linejkaPosLeft;
	var begunPosRight = begunPosLeft + 156;
	if (begunPosLeft < 0) {
		begunPosLeft = 0;
	}
	var blockNumber = 1;
	if (0 < begunPosLeft && begunPosLeft < 190) {
		begunPosLeft = 0;
		blockNumber = 1;
	}
	if (190 < begunPosLeft && begunPosLeft < 331) {
		begunPosLeft = 180;
		blockNumber = 2;
	}
	if (331 < begunPosLeft && begunPosLeft < 472) {
		begunPosLeft = 321;
		blockNumber = 3;
	}
	if (472 < begunPosLeft && begunPosLeft < 652) {
		begunPosLeft = 462;
		blockNumber = 4;
	}
	begunPosRight = begunPosLeft + begunokWidth;
	if (begunPosRight  > $(".begunok").parent().width()) {
		begunPosLeft = $(".begunok").parent().width() - begunokWidth;
	}
	var showBegunok = true;
	if (selectedPosLeft || selectedPosRight) {
		if (selectedPosLeft < begunPosLeft && begunPosLeft < selectedPosRight) {
			begunPosLeft = selectedPosRight;
		}
		if (selectedPosLeft < begunPosRight && begunPosRight < selectedPosRight) {
			begunPosLeft = selectedPosLeft-begunokWidth;
		}
	}
	if(showBegunok) {
		$(".begunok").hide();
		$("#begunok" + blockNumber).fadeIn();
	} else {
		$(".begunok").hide();
	}
}

function show_begunok_descrete(e ){

	$(".begunok").hide();
	$(this).fadeIn();
}

function hide_begunok(){
	$(".begunok").attr("style","display:none");
}
