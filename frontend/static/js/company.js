document.addEventListener("DOMContentLoaded", function () {

    const modalElement = document.getElementById("companyModal");
    const modal = new bootstrap.Modal(modalElement);

    const deleteModalEl = document.getElementById("deleteModal");
    const deleteModal = new bootstrap.Modal(deleteModalEl);

    const openCreateBtn = document.getElementById("openCreateModal");
    const openEditBtn = document.getElementById("openEditModal");
    const openDeleteBtn = document.getElementById("openDeleteModal");

    const companyIdInput = document.getElementById("companyId");
    const companyNameInput = document.getElementById("companyName");
    const modalTitle = document.getElementById("modalTitle");
    const modalSubmitBtn = document.getElementById("modalSubmitBtn");

    const deleteIdInput = document.getElementById("deleteId");
    const deleteCompanyName = document.getElementById("deleteCompanyName");

    let selectedRow = null;

// ROW SELECTION
    document.querySelectorAll(".company-row").forEach(row => {
        row.addEventListener("click", function () {
            document.querySelectorAll(".company-row")
                .forEach(r => r.classList.remove("selected"));
            this.classList.add("selected");
            selectedRow = this;
        });
    });
    openCreateBtn.addEventListener("click", function () {

        selectedRow = null;

        companyIdInput.value = "";
        companyNameInput.value = "";

        modalTitle.textContent = "Create Company";
        modalSubmitBtn.textContent = "Create";

        modal.show();
    });
    openEditBtn.addEventListener("click", function () {

        if (!selectedRow) {
            alert("Please select a company first.");
            return;
        }

        const id = selectedRow.dataset.id;
        const name = selectedRow.dataset.name;

        companyIdInput.value = id;
        companyNameInput.value = name;

        modalTitle.textContent = "Edit Company";
        modalSubmitBtn.textContent = "Update";

        modal.show();
    });
    openDeleteBtn.addEventListener("click", function () {
        if (!selectedRow) {
            alert("Please select a company first.");
            return;
        }

        deleteIdInput.value = selectedRow.dataset.id;
        deleteCompanyName.textContent = selectedRow.dataset.name;

        deleteModal.show();
    });
});