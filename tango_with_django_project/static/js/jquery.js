
$(document).ready(function(){
    $("#about-btn").click(function (event) {
        alert("You clicked the button using Jquery");
    });
});

$("#about-btn").click(function (event) {
    msgstr = $("#msg").html() + "ooooo";
    $("#msg").html(msgstr);
});