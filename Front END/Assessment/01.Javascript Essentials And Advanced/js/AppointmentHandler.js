import { getData, setData } from "./storageUtils.js";

export default class AppointmentHandler {
  constructor() {
    this.form = document.getElementById("appointmentForm");
    this.message = document.getElementById("message");
    this.addEventListeners();
  }

  validateForm() {
    let valid = true;
    const now = new Date();

    this.form.querySelectorAll(".error").forEach(e => e.textContent = "");

    const fields = {
      name: document.getElementById("name"),
      email: document.getElementById("email"),
      phone: document.getElementById("phone"),
      date: document.getElementById("date"),
      time: document.getElementById("time"),
      comment: document.getElementById("comment")
    };

    if (fields.name.value.trim().length < 3) {
      fields.name.nextElementSibling.textContent = "Minimum 3 characters required";
      valid = false;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(fields.email.value)) {
      fields.email.nextElementSibling.textContent = "Invalid email address";
      valid = false;
    }

    if (!/^\d{10}$/.test(fields.phone.value)) {
      fields.phone.nextElementSibling.textContent = "Phone must be 10 digits";
      valid = false;
    }

    if (!fields.date.value || !fields.time.value ||
        new Date(`${fields.date.value} ${fields.time.value}`) <= now) {
      fields.date.nextElementSibling.textContent = "Select future date & time";
      valid = false;
    }

    if (fields.comment.value.trim().length < 50) {
      fields.comment.nextElementSibling.textContent = "Minimum 50 characters required";
      valid = false;
    }

    return valid;
  }

  saveToLocalStorage(data) {
    const appointments = getData("appointments");
    appointments.push(data);
    setData("appointments", appointments);
  }

  clearForm() {
    this.form.reset();
  }

  showMessage(type, message) {
    this.message.innerHTML = `<p class="${type}">${message}</p>`;
  }

  addEventListeners() {
    // Submit
    this.form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (this.validateForm()) {
        const data = {
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            phone: document.getElementById("phone").value,
            date: document.getElementById("date").value,
            time: document.getElementById("time").value,
            comment: document.getElementById("comment").value
        };

        console.log("Appointment Data:", data); 

        this.saveToLocalStorage(data);
        this.showMessage("success", "Your Appointment booked successfully!");
        this.clearForm();
      } else {
        this.showMessage("error", "Please Enter a Valid Data");
      }
    });

    this.form.addEventListener("input", () => this.validateForm());
  }
}
