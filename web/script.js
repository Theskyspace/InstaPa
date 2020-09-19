
function getInputValue(){
  // Selecting the input element and get its value 
  window.name = document.getElementById("username").value;
  window.pwd = document.getElementById("pwd").value;

  eel.login(window.name,window.pwd)(); 
}




window.hashtags = []
window.comments = []


function newElement() {

  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  window.hashtags.push(inputValue);
  var t = document.createTextNode("# "+inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";

 
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

function newcomment() {
  console.log("called ");
  var li = document.createElement("li");
  var comment = document.getElementById("comment").value;
  window.comments.push(comment);
  var t = document.createTextNode(comment);
  li.appendChild(t);
  if (comment === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myULcomments").appendChild(li);
  }
  document.getElementById("comment").value = "";

 
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}




function Like(){
  var no_of_Like = document.getElementById('quantity').value
  eel.MainProcess(window.hashtags,window.comments,no_of_Like)()
}



function terminate(){
  eel.terminate()()
}