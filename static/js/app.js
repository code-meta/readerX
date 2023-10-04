// toggle navbar
const navbarToggleBtn = document.getElementById("navbar-toggle");
const navMenu = document.getElementById("nav-menu");

// toggle theme mode
const changeTheme = document.getElementById("change-theme");
const iconDark = document.getElementById("icon-dark");
const iconLight = document.getElementById("icon-light");

navbarToggleBtn.addEventListener("click", (e) => {
  navMenu.classList.toggle("hidden");
});

if (
  localStorage.theme === "dark" ||
  (!("theme" in localStorage) &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  document.documentElement.classList.add("dark");
  iconLight.classList.remove("hidden");
} else {
  document.documentElement.classList.remove("dark");
  iconDark.classList.remove("hidden");
}

changeTheme.addEventListener("click", (e) => {
  const root = document.documentElement;

  if (!root.classList.contains("dark")) {
    root.classList.add("dark");

    iconDark.classList.add("hidden");
    iconLight.classList.remove("hidden");

    localStorage.theme = "dark";
  } else {
    root.classList.remove("dark");

    iconLight.classList.add("hidden");
    iconDark.classList.remove("hidden");

    localStorage.theme = "light";
  }
});

// scroll to top fab

const srTopFab = document.getElementById("sr-top");
const navbar = document.getElementById("navbar");

srTopFab.addEventListener("click", (e) => {
  navbar.scrollIntoView();
});

window.addEventListener("scroll", (e) => {
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    srTopFab.style.display = "block";
  } else {
    srTopFab.style.display = "none";
  }
});
