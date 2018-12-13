function test() {
    alert("TESTING...")
    //console.log("test!...");
    document.getElementById("output").innerHTML= 5+6;
}



function main () 
{
	//	Load inputs
	var minage = document.getElementById("minage");
	var maxage = document.getElementById("maxage");
	var gender = document.getElementById("gender");
	var paap = document.getElementById("paap");

	alert("Calling main Test " + minage.value + maxage.value + gender.value + paap.value);

	// $.post("receiver", JSON.stringify(paap.value), function(){
	// 	alert("Posting to receiver");
	// });

		$.post( "receiver", {
    "paap.value": "paap.value", function(){}
});


	alert("After reciever");


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
        