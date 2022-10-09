function validator() {
    let user = document.getElementById("user")
    let error = document.getElementById("error")
    let password = document.getElementById("password")
    let reg = /^[A-Za-z]+$/g
    if (user.value == "") {
        error.innerHTML = "username required"
        error.style.display = "flex"
        user.style.border = "2px solid red"
        return false
    }
    if (password.value == "") {
        error.innerHTML = "password required"
        error.style.display = "flex"
        password.style.border = "2px solid red"
        return false
    } else if (user.value.length < 6) {
        error.innerHTML = "user name shpould be min 6 char"
        error.style.display = "flex"
        user.style.border = "2px solid red"
        return false
    } else if (password.value.length < 6) {
        error.innerHTML = "password should be min 6 char"
        error.style.display = "flex"
        password.style.border = "2px solid red"
        return false
    } else if (user.value.length > 10) {
        error.innerHTML = "username should not exceed more than 10 char"
        error.style.display = "flex"
        user.style.border = "2px solid red"
        return false
    } else if (reg.test(user.value) == false) {
        error.innerHTML = "username should be contain alphabets"
        error.style.display = "flex"
        user.style.border = "2px solid red"
        return false
    } else if (user.value == "username" || user.value == "querty") {
        error.innerHTML = "username should not be username"
        error.style.display = "flex"
        user.style.border = "2px solid red"
        return false
    } else {
        alert("username matches")
        return true
    }


}