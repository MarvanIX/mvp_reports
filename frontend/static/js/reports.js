document.addEventListener("DOMContentLoaded", function () {

    let selectedRow = null;

    document.querySelectorAll(".report-row").forEach(row => {
        row.addEventListener("click", function () {

            // remove previous selection
            document.querySelectorAll(".report-row")
                .forEach(r => r.classList.remove("selected"));

            // highlight clicked row
            this.classList.add("selected");
            selectedRow = this;
        });
    });

});