var slideIndex = 0;

var signup = {
    "Email": "",
    "First": "",
    "Last": "",
    "Company": {
        "Name": "",
        "Industry": ""
    },
    "CreditCard": {
        "Ccv": "",
        "ExpirationMonth": "",
        "ExpirationYear": "",
        "Name": "",
        "Number": ""
    },
    "ResellerId": "",
    "Page": ""
};

window.onload = function () {
    var i;
    var x = document.getElementsByClassName("slides");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > x.length) {
        slideIndex = 1
    }
    x[slideIndex - 1].style.display = "block";
}

function carousel(back = 0) {

    var i;
    var x = document.getElementsByClassName("slides");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    if (back == 0) {
        slideIndex++;
    } else {
        slideIndex--;
    }
    if (slideIndex > x.length) {
        slideIndex = 1
    }
    x[slideIndex - 1].style.display = "block";

}

function json_obj() {
    signup.First = document.getElementById("firstNameBox").value;
    signup.Last = document.getElementById("lastNameBox").value;
    signup.Email = document.getElementById("emailBox").value;
    signup.Company.Name = document.getElementById("companyBox").value;
    signup.Company.Industry = document.getElementById("industryBox").value;
    signup.CreditCard.Name = document.getElementById("ccNameBox").value;
    signup.CreditCard.Number = document.getElementById("ccBox").value;
    signup.CreditCard.ExpirationMonth = document.getElementById("expMonBox").value;
    signup.CreditCard.ExpirationYear = document.getElementById("expYrBox").value;
    signup.CreditCard.Ccv = document.getElementById("ccvBox").value;

}

window.onresize = function (event) {
    navbar = this.document.getElementsByClassName("navbar-nav")[0];

    if (navbar.offsetHeight > 25) {
        navbar.appendChild(moreMenu);
        navItem1.classList.remove("nav-link");
        navItem2.classList.remove("nav-link");

        navItem1.classList.add("dropdown-item");
        navItem2.classList.add("dropdown-item");

        moreMenuDiv.appendChild(navItem1);
        moreMenuDiv.appendChild(navItem2);

    } else {
        if (!!moreMenu.parentElement && navbar.offsetWidth >= 425) {
            navItem1.classList.add("nav-link");
            navItem2.classList.add("nav-link");

            navItem1.classList.remove("dropdown-item");
            navItem2.classList.remove("dropdown-item");

            navbar.childNodes[5].appendChild(navItem1);
            navbar.childNodes[7].appendChild(navItem2);
            navbar.removeChild(moreMenu);
        } else {

        }
    }
}

navItem1 = this.document.getElementById("link1");
navItem2 = this.document.getElementById("link2");

moreMenu = document.createElement("li");
moreMenu.classList.add("nav-item");
moreMenu.classList.add("dropdown");


moreMenuTitle = document.createElement("a");
moreMenuTitle.classList.add("nav-link");
moreMenuTitle.classList.add("dropdown-toggle");
moreMenuTitle.href = "#";
moreMenuTitle.id = "navbarDropdownMenuLink";
moreMenuTitle.innerText = "More";
moreMenuTitle.setAttribute("data-toggle", "dropdown");

moreMenuDiv = document.createElement("div");
moreMenuDiv.classList.add("dropdown-menu");

moreMenu.appendChild(moreMenuTitle);
moreMenu.appendChild(moreMenuDiv);