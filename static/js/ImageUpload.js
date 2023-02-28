function validateForm() {
  var fileInput = document.getElementById("photo");
  var filePath = fileInput.value;
  var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
  if (!allowedExtensions.exec(filePath)) {
    document.getElementById("error-message").innerHTML =
      "잘못된 형식의 파일입니다.";
    fileInput.value = "";
    return false;
  } else {
    document.getElementById("error-message").innerHTML = "";
    return true;
  }
}
const photoInput = document.querySelector("#photo");
const preview = document.querySelector("#preview");
photoInput.addEventListener("change", function () {
  const file = photoInput.files[0];
  const reader = new FileReader();
  reader.onload = function (e) {
    preview.src = e.target.result;
    preview.style.display = "block";
  };
  reader.readAsDataURL(file);
});
