// let screenVal = document.getElementById("headingID");

const header = document.querySelector("h1");
const c_classBttn = document.querySelector(".c_class");

c_classBttn.addEventListener("click", () => {
  header.innerText = "Cleared the Screen";
});

const bksp_classBttn = document.querySelector(".bksp_class");

bksp_classBttn.addEventListener("click", () => {
  if (header.innerText.length > 0) {
    header.innerText = header.innerText.slice(0, -1);
  }
});

const numButtons = document.querySelectorAll(
  ".num_0, .num_1, .num_2, .num_3, .num_4, .num_5, .num_6, .num_7, .num_8, .num_9",
);
