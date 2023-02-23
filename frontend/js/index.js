// Variables:
const barsBtn = document.querySelector(".navbar__right-icon-container");
const menu = document.querySelector(".navbar__right-links");
const checkboxContainer = document.querySelectorAll(".tables__table-checkbox");
const table = document.querySelector(".tables__table-body");
const refreshButton = document.querySelector(".refresh__btn");

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

function getAllCourses() {
	// Fetch API:
	fetch("https://lilms.iran.liara.run/courses/")
		.then((response) => response.json())
		.then((data) => {
            console.log(data);
			data.forEach((course) => {
				table.insertAdjacentHTML(
					"beforeend",
					`
                        <tr class="tables__table-row">
                            <td class="tables__table-checkbox">
                                <input class="tables__table-input" type="checkbox" />
                            </td>
                            <td class="tables__table-title">
                                <span class="tables__table-title-text">${course.name}</span>
                            </td>
                            <td class="tables__table-code">
                                <span class="tables__table-code-text">${course.code}</span>
                            </td>
                            <td class="tables__table-group">
                                <span class="tables__table-group-text">${course.group}</span>
                            </td>
                            <td class="tables__table-teacher">
                                <span class="tables__table-teacher-text">${course.teacher}</span>
                            </td>
                            <td class="tables__table-time1">
                                <span class="tables__table-time1-text">${course.class_times[0].day}[${course.class_times[0].end_time}-${course.class_times[0].start_time}]</span>
                            </td>
                            <td class="tables__table-time2">
                                <span class="tables__table-time2-text">${course.class_times[1] === undefined ? "" : course.class_times[1].day}[${course.class_times[1] === undefined ? "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" : course.class_times[1].start_time}-${course.class_times[1] === undefined ? "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" : course.class_times[1].end_time}]</span>
                            </td>
                            <td class="tables__table-exam">
                                <span class="tables__table-exam-text">${course.exam_time.day}[${course.exam_time.start_time}0-${course.exam_time.end_time}0]</span>
                            </td>
                        </tr>
                    `
				);
			});
		});
}

window.addEventListener("load", () => {
	getAllCourses();
});

refreshButton.addEventListener("click", () => {
    console.log('click');
    table.innerHTML = ''
    getAllCourses();
});
