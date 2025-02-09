function deleteListItem(element) {
    element.parentElement.remove();
}

function completeTask(checkbox) {
    let li = checkbox.parentElement;
    let p = li.querySelector(".task");

    if (checkbox.checked) {
        p.style.textDecoration = "line-through";
    } else {
        p.style.textDecoration = "none";
    }
}

function addListItem() {
    let Input = document.getElementById("task"); 
    let Message = Input.value.trim();
    if (Message === "") {
        alert("You need to write the task");
        return;
    }

    let li = document.createElement("li");
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.onclick = function () {
        completeTask(this);
    };
    let Text = document.createElement("p");
    Text.className = "task";
    Text.textContent  = Message;

    let deleteIcon = document.createElement("img");
    deleteIcon.className = "garbage";
    deleteIcon.src = "assets/images/garbagge.png";
    deleteIcon.alt = "Delete";
    deleteIcon.onclick = function () {
        deleteListItem(this);
    };

    let taskList = document.getElementById("task_list");
    li.appendChild(checkbox);
    li.appendChild(Text);
    li.appendChild(deleteIcon);
    taskList.appendChild(li);

    Input.value = "";
}