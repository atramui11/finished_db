function test() {
    alert("TESTING...")
    //console.log("test!...");
    document.getElementById("output").innerHTML= 5+6;
}


function main () 
{

	$.ajaxSetup({
  		contentType: "application/json; charset=utf-8"
	});
	//	Load inputs
	var minage = document.getElementById("minage");
	var maxage = document.getElementById("maxage");
	var gender = document.getElementById("gender");
	var paap = document.getElementById("paap");

	alert("Calling main" + minage.value + maxage.value + gender.value + paap.value);

	// $.post("receiver", JSON.stringify(minage.value), function(){
	// });

// 	$.post( "receiver", {
//     "paap.value": "paap.value", function(){}
// });

	alert("After reciever HERE");


	//	Validate inputs
	if (minage.value < 0 || minage.value > maxage.value){
		alert("Please verify that minage <= maxage and that minage is positive.");
		return;
	}

	if (gender.value.localCompare("m") != 0 || gender.value.localCompare("f") != 0){
		alert("Please type correct gender: \"m\" or \"f\".");
		return;
	}

	if (paap.value.localCompare("ap") != 0 || paap.value.localCompare("pa") != 0){
		alert("Please type in correct PAAP: \"pa\" or \"ap\".");
		return;
	}


	//	SQL query here
    //pythonfile(.....);

	//	Publish results to table
    //send to div results

}
        