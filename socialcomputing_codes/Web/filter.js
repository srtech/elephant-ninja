var fromT = "";
var toT = "";
var subjectT = "";
var haswT = "";
var hasnotwT = "";
var rsptextT= "";

function go() {
	fromT = document.getElementById("from").value;
	toT = document.getElementById("to").value;
	subjectT = document.getElementById("subject").value;
	haswT = document.getElementById("hasw").value;
	hasnotwT = document.getElementById("hasnotw").value;
	rsptextT = document.getElementById("rsptext").value;

	$.ajax({
        type: "POST",
        url: "savefilters.php",
        data: {from: fromT, to: toT, subject: subjectT, hasw: haswT, hasnotw: hasnotwT, rsptext: rsptextT}
      }).done(function(message){
      	alert(message);       
      });	
}

function clearF() {
	$.ajax({
        type: "POST",
        url: "clearfilters.php",
        data: {clear: 1}
      }).done(function(message){
      	alert(message);        
      });
}