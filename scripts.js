function show(div_id) {
  var x = document.getElementById(div_id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}