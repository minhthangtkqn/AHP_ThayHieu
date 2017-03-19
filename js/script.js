var levelAmount = 0;
var currentLevel = 0;
var container = "";

var levelElementAmount = []; // số tiêu chí trong từng bậc
var levelElementName = []; // mảng 2 chiều lưu tên các tiêu chí 

function addDropDown(row, column) {
    var select = document.createElement("select");
    select.id = "select_" + (row - 1) + "_" + (column - 1);

    for (i = 1; i <= 9; i++) {
        var option = document.createElement("option");
        option.value = i;
        option.innerHTML = i;
        select.appendChild(option);
    }

    return select;
}

function nhapDuLieuMaTran() {
    //theo level
    for (level = 0; level < levelAmount; level++) {
        // số lượng ma trận trong 1 bậc = số tiêu chí của bậc trên nó
        var matrixAmount = 0;
        if (level === 0) {
            matrixAmount = 1;
        } else {
            matrixAmount = levelElementAmount[level - 1];
        }

        //for theo số lượng ma trận
        for (matrixNumber = 0; matrixNumber < matrixAmount; matrixNumber++) {
            var table = document.createElement("table");
            table.id = "table_" + level + "_" + matrixNumber;
            table.style = "width: 45%";
            container.appendChild(table);

            //theo số lượng tiêu chí của từng bậc --> lập ma trận
            for (row = 0; row <= levelElementAmount[level]; row++) {
                var currentRow = document.createElement("tr");

                for (column = 0; column <= levelElementAmount[level]; column++) {
                    var currentBox = document.createElement("th");

                    if (row === 0) { // hàng đầu tiên chỉ chứa tên
                        if (column === 0) { //nếu là ô đầu tiên trong hàng 0
                            if (level > 0) {
                                currentBox.innerHTML = levelElementName[level - 1][matrixNumber];
                                currentRow.appendChild(currentBox);
                            } else {
                                currentBox.innerHTML = "";
                                currentRow.appendChild(currentBox);
                            }
                        } else {
                            currentBox.innerHTML = levelElementName[level][column - 1];
                            currentRow.appendChild(currentBox);
                        }

                    } else {
                        if (column === 0) {
                            currentBox.innerHTML = levelElementName[level][row - 1];
                            currentRow.appendChild(currentBox);
                        } else {
                            if (row === column) {
                                // đường chéo số 1
                                currentBox.innerHTML = "1";
                                currentRow.appendChild(currentBox);
                            } else {
                                // các ô được chọn để thêm drop-down
                                if (row >= 1 && row < levelElementAmount[level]) {
                                    if (column > row && column <= levelElementAmount[level]) {
                                        var select = addDropDown(row, column);

                                        currentBox.appendChild(select);
                                        currentRow.appendChild(currentBox);
                                    } else {
                                        currentBox.innerHTML = "";
                                        currentRow.appendChild(currentBox);
                                    }
                                } else {
                                    currentBox.innerHTML = "";
                                    currentRow.appendChild(currentBox);
                                }
                            }
                        }
                    }
                } //end for column
                table.appendChild(currentRow);
                table.appendChild(document.createElement("br"));
            } //end for row

        }

    }
}

function clearScreen() {
    var first = document.getElementById("first");
    while (first.hasChildNodes()) {
        first.removeChild(first.lastChild);
    }

    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
}

function submitValue() {
    // for theo bậc
    for (level = 1; level <= levelAmount; level++) {
        // lấy số lượng thành phần trong bậc
        levelElementAmount.push(document.getElementById("value_" + level).value);

        // lấy mảng tên các thành phần
        levelElementName.push([]);
        for (nameNumber = 1; nameNumber <= levelElementAmount[level - 1]; nameNumber++) {
            levelElementName[level - 1].push(document.getElementById("level_" + level + "_" + nameNumber).value);
        }
    }
    clearScreen();
    // -----------------------
    // hiển thị kết quả
    container.appendChild(document.createTextNode("Số lượng các phần tử của các bậc"));
    container.appendChild(document.createElement("br"));

    var a = document.createElement("div");
    for (i = 0; i < levelElementAmount.length; i++) {
        a.innerHTML += "Tầng " + (i + 1) + ": " + levelElementAmount[i] + "--> " + levelElementName[i] + "<br/>";

    }
    container.appendChild(a);
    // -----------------------
    nhapDuLieuMaTran();
}

function addButton(id, style, innerHTML) {
    var button = document.createElement("button");
    if (id !== "") {
        button.id = id;
    }
    button.style = style;
    button.innerHTML = innerHTML;
    button.setAttribute("class", "btn btn-success");

    return button;
}

function addInput(id, style) {
    var input = document.createElement("input");
    input.id = id;
    input.type = "text";
    input.style = style;
    input.setAttribute("class", "form-control");

    return input;
}

function nhapDuLieu(nameAmounts) {
    //kiem tra gia tri nhap vao isNumber hay ko
    if (!isNaN(nameAmounts)) {
        for (currentName = 1; currentName <= nameAmounts; currentName++) {
            var input = addInput("level_" + currentLevel + "_" + currentName, "margin-left: 10px; margin-top: 5px;");
            container.appendChild(input);
        }
        //-------------------------------------------
        //-------------------------------------------
        //-------------------------------------------
        //hien thi button --> level ke tiep (neu con)
        container.appendChild(document.createElement("br"));
        if (currentLevel < levelAmount) {

            currentLevel++;
            showLevel();

        } else {
            //hiển thị button chuyển sang nhập ma trận
            var submitBtn = addButton("submitBtn", "", "SUBMIT");
            submitBtn.addEventListener("click", function () {
                //lấy các giá trị trong input lưu vào biến
                submitValue();
            });
            container.appendChild(submitBtn);
        }
    } else {
        alert(nameAmounts + " không phải là số");
    }
}

function showLevel() {
    container.appendChild(document.createTextNode("Tầng " + currentLevel + "  :  "));

    //nhap so tieu chi cua moi tang
    var input = addInput("value_" + currentLevel, "margin-top: 5px");
    container.appendChild(input);

    //nhap ten cho cac tieu chi
    var nameBtn = addButton("", "margin-top: 10px", ">>>");
    nameBtn.addEventListener("click", function () {
        nhapDuLieu(document.getElementById("value_" + currentLevel).value);
    });
    container.appendChild(nameBtn);

}

function addItems() {
    levelAmount = document.getElementById("amounts").value;
    container = document.getElementById("container");

    //xoa trang container
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }

    if (levelAmount > 0 && levelAmount < 4) {

        currentLevel = 1;
        showLevel();
    } else {
        alert("Giá trị nằm trong khoảng từ 1 -> 3");
    }

}
