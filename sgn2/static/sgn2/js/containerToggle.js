document.addEventListener("DOMContentLoaded", function() {
    var checkbox = document.getElementById("status");
    var container1 = document.getElementById("container1");
    var container2 = document.getElementById("container2");
    
    checkbox.addEventListener("change", function() {
        if (checkbox.checked) {
            container1.style.display = "none";
            container2.style.display = "flex";
        } else {
            container1.style.display = "flex";
            container2.style.display = "none";
        }
    });
});