window.addEventListener("scroll", function () {
    const btn = document.querySelector(".topbtn");
    if (window.scrollY > 200) {
        btn.classList.add("show");
    } else {
        btn.classList.remove("show");
    }
});