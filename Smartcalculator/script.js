// let screenVal = document.getElementById("headingID");

const header = document.querySelector("h1");
const c_classBttn = document.querySelector(".c_class");

c_classBttn.addEventListener("click", () => {
  header.innerText = "Cleared the Screen";
});
