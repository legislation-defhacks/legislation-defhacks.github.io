//javascript file with functions

(function (){

	var key = "FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9"
	"use strict";

	/*Sets up event listeners for button pressing and sets up the puzzle pieces and the background.
	selector for the page. */
	window.onload = function() {
		document.getElementById("submit").onclick = buildPopupDom;
		//addStatesToDropDown();
		//document.getElementById("searchbystate").onclick = findRepresentatives;
	};

	// Given an array of URLs, build a DOM list of those URLs in the
// browser action popup.
function buildPopupDom() {
	debugger;
  var radiosBill = document.getElementsByName('bill');
  var valueBill = "";

  for(var i = 0; i < radiosBill.length; i++) {
    if(radiosBill[i].checked) {
      valueBill = radiosBill[i].value;
      break;
    }
  }
  var radiosPerson = document.getElementsByName('person');
  var valuePerson = "";
  for(var i = 0; i < radiosPerson.length; i++) {
    if(radiosPerson[i].checked) {
      valuePerson = radiosPerson[i].value;
      break;
    }
  }
  var array = [valueBill, valuePerson];
  var valueFirstRadio = document.getElementById("")
	console.log(array);
  $.ajax({
    type: "POST",
    url: "http://localhost:5000/spectrum",
    data: {
      urlArray: JSON.stringify(array)
    },
    success: function( result ) {
      $( "#finalscore" ).html( "<strong>" + result + "%</strong>" );
    }
  });

  // $.ajax({
  //   type: "POST",
  //   url: "http://localhost:5000/credibility",
  //   data: {
  //     urlArray: JSON.stringify(array)
  //   },
  //   success: function( result ) {
  //       var creditiblity = "";
  //       result = parseInt(result);
  //       if(0 <= result && result <= 33){
  //            creditiblity = "Low Credibility";
  //       }else if(34 < result && result  <= 67){
  //            creditiblity = "Medium Credibility";
  //       }else if(68 < result && result <= 100){
  //            creditiblity = "High Credibility";
  //       }
  //     $("#credibility_title").text(creditiblity);
  //     $(".credibility_ticker").css("margin-left", result + "%");
  //     $( "#credibility" ).html( "<strong>" + Math.abs(result) + "%</strong>" );
  //     $("#suggest_credibility").text(creditiblity);
  //   }
  // });
}


	//setting up our ajax request to get data.
	//takes in the url that we are requesting and the
	//onload function that is used once the data is loaded.
	function ajaxRequest(url, onloadFunction) {
		document.getElementById("")
		var ajax = new XMLHttpRequest();
		ajax.onload = onloadFunction;
		ajax.open("GET", url, true);
		ajax.setRequestHeader("X-API-Key", "FDBDTKNO6cAmhbDXpAACrvLL82JRryke3RN7oU9");
		ajax.send();
	}


	//could do a boolean for house of representatives or not.
	function searchByState() {
		var stateSelector = document.getElementById("state-selector");
		var selectedState = stateSelector.options[stateSelector.selectedIndex].value;
		var senateUrl = "https://api.propublica.org/congress/v1/members/" + "senate" + "/" + selectedState + "/current.json";
		var representativeUrl = "https://api.propublica.org/congress/v1/members/" + "house/" + selectedState + "/1/current.json";

	}

	function mapStateToRepresentativeNumber() {
		var stateToRepresentativeNumber = [];
		d3.json("state-district-num.json", function(data) {
			data.results.forEach(function(d) {
				stateToRepresentativeNumber.push()
				//var infoString = "name: " + d.name + ", " + "party: " + d.party
				//stateToRepresentativeNumber.push("element");
			});
		})
	}

	//adds the state lables to the dropdown with each of the choices.
	function addStatesToDropDown() {
		d3.json("state-arr.json", function(data) {
			var stateSelector =
  					document.getElementById("state-selector");
  			data.forEach(function(d) {
  				var newOption = document.createElement("option");
  				newOption.label = d.abbreviation;
  				newOption.innerHTML = d.name + "(" + d.abbreviation + ")";
  				stateSelector.appendChild(newOption);
  			});
		});
	}

})();
