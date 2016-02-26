console.log("beginning of ok.js");
$.getJSON("../out.json", function(json) {
    console.log(json); // this will show the info it in firebug console
});
