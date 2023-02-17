console.log("run");

// Variables:
const barsBtn = document.querySelector(".navbar__right-icon-container");
const menu = document.querySelector(".navbar__right-links");
const checkboxContainer = document.querySelectorAll(".tables__table-checkbox");

console.log(menu);

// Responsive Bars Icon:
barsBtn.addEventListener("click", () => {
	menu.classList.toggle("open");
	barsBtn.classList.toggle("open");
});

// Table CheckBox:
checkboxContainer.forEach((e) => {
	e.addEventListener("click", () => {
		if (e.childNodes[1].checked === false) {
			e.childNodes[1].checked = true;
		} else {
			e.childNodes[1].checked = false;
		}
	});
});

console.log("run");

// Fetch API:
fetch("http://127.0.0.1:8000/courses/")
	.then((response) => response.json())
	.then((data) => console.log(data));
