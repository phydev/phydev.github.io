function showHide(div_id) {
  var div = document.getElementById(div_id);
  if (div.style.display === "none") {
    div.style.display = "block";
  } else {
    div.style.display = "none";
  }
}