document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const instance = document.querySelector("#instance").value;
        const ope_sys = document.querySelector("#ope_sys").value;
        const year = document.querySelector("#year").value;
        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `company=${instance}&car_models=${ope_sys}&year=${year}`
        })
        .then(response => response.text())
        .then(prediction => {
            document.querySelector("#result").innerHTML = `Predicted value: ${prediction}`;
        })
        .catch(error => console.error(error));
    });
});