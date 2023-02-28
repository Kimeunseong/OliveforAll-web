// eslint-disable-next-line no-unused-vars
function imgSlider(anything) {
  document.querySelector(".starbucks").src = anything;
}
// eslint-disable-next-line no-unused-vars
function changeCircleColor(color) {
  const circle = document.querySelector(".circle");
  circle.style.background = color;
}
// eslint-disable-next-line no-unused-vars
function toggleMenu() {
  var menuToggle = document.querySelector(".toggle");
  var navigation = document.querySelector(".navigation");
  menuToggle.classList.toggle("active");
  navigation.classList.toggle("active");
}
imgSlider;
