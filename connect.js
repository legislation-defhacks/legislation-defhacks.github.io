// Given an array of URLs, build a DOM list of those URLs in the
// browser action popup.
function buildPopupDom() {
  var radiosBill = document.getElementsByName('bill');
  var valueBill = "";
  for(int i = 0; i < radiosBill.length; i++) {
    if(radiosBill[i].checked) {
      valueBill = radiosBill[i].value;
      break;
    }
  }
  var radiosPerson = document.getElementsByName('person');
  var valuePerson = "";
  for(int i = 0; i < radiosPerson.length; i++) {
    if(radiosPerson[i].checked) {
      valuePerson = radiosPerson[i].value;
      break;
    }
  }
  var array = [valueBill, valuePerson];
  var valueFirstRadio = document.getElementById("")
  $.ajax({
    type: "POST",
    url: "http://localhost:5000/spectrum",
    data: {
      urlArray: JSON.stringify(array)
    },
    success: function( result ) {
      // var position = "";
      // result = parseInt(result);
      // if(result <= -75){
      //   //really liberal
      //   position = "Mostly Liberal"
      // }else if(result >= -75 && result <= -25){
      //   position = "Semi Liberal"
      // }else if(result >= -25 && result <= 0){
      //   position = "Neutral, Leans Liberal"
      // }else if(result >= 0 && result <= 25){
      //   position = "Neutral, Leans Conservative"
      // }else if(result >= 25 && result <= 75){
      //   position = "Semi Conservative"
      // }else if(result >= 75){
      //   position = "Mostly Conservative"
      // }
      // var tickerPos = (result + 100) / 2;
      // console.log(tickerPos);
      // $("#exposure_title").text(position);
      // $(".exposure_ticker").css("margin-left", tickerPos + "%");
      $( "#finalscore" ).html( "<strong>" + result + "%</strong>" );
      // $("#lean").text(position);
    }
  });

  $.ajax({
    type: "POST",
    url: "http://localhost:5000/credibility",
    data: {
      urlArray: JSON.stringify(array)
    },
    success: function( result ) {
        var creditiblity = "";
        result = parseInt(result);
        if(0 <= result && result <= 33){
             creditiblity = "Low Credibility";
        }else if(34 < result && result  <= 67){
             creditiblity = "Medium Credibility";
        }else if(68 < result && result <= 100){
             creditiblity = "High Credibility";
        }
      $("#credibility_title").text(creditiblity);
      $(".credibility_ticker").css("margin-left", result + "%");
      $( "#credibility" ).html( "<strong>" + Math.abs(result) + "%</strong>" );
      $("#suggest_credibility").text(creditiblity);
    }
  });
}
