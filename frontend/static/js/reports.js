document.addEventListener("DOMContentLoaded", function () {

    let selectedRow = null;

    document.querySelectorAll(".report-row").forEach(row => {
        row.addEventListener("click", function () {

            document.querySelectorAll(".report-row")
                .forEach(r => r.classList.remove("selected"));

            this.classList.add("selected");
            selectedRow = this;
        });
    });

});