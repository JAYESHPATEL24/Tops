import { getData, setData } from "./storageUtils.js";

export default class AppointmentViewer {
  constructor() {
    this.data = getData("appointments");
    this.tableBody = document.getElementById("tableBody");
    this.noData = document.getElementById("noData");
    this.search = document.getElementById("search");
    this.render(this.data);
    this.addEvents();
  }

  render(list) {
    this.tableBody.innerHTML = "";

    if (list.length === 0) {
      this.noData.textContent = "No applications found";
      return;
    }

    this.noData.textContent = "";

    list.forEach((item, index) => {

        console.log("Rendering item:", item);
      const row = `
        <tr>
          <td>${item.name}</td>
          <td>${item.email}</td>
          <td>${item.phone}</td>
          <td>${item.date}</td>
          <td>${item.time}</td>
          <td><button data-index="${index}">Delete</button></td>
        </tr>`;
      this.tableBody.innerHTML += row;
    });
  }

  addEvents() {
    this.search.addEventListener("input", () => {
      const value = this.search.value.toLowerCase();
      const filtered = this.data.filter(d =>
        d.name.toLowerCase().includes(value) ||
        d.date.includes(value)
      );
      this.render(filtered);
    });

    this.tableBody.addEventListener("click", (e) => {
      if (e.target.tagName === "BUTTON") {
        const index = e.target.dataset.index;
        this.data.splice(index, 1);
        setData("appointments", this.data);
        this.render(this.data);
      }
    });
  }
}
