const emailField = document.querySelector(".js-email-input")
const EMAIL_REGEX_PATTERN = /^[a-z]\w{2,}@\w{2,}\.\w{2,}$/

const isSubscriptionFormValid = () => {
    return isEmailFieldValid()
}

const isEmailFieldValid = () => {
    const errorHolder = emailField.closest(".js-input-container").querySelector(".js-error-holder")
    if(emailField.value.trim() === ""){
        errorHolder.textContent = "البريد الالكتروني مطلوب"
        return false
    }
    if(!EMAIL_REGEX_PATTERN.test(emailField.value)){
        errorHolder.textContent = "يرجى ادخال بريد الكتروني صحيح"
        return false
    }
    errorHolder.textContent = ""
    return true
}

emailField.addEventListener("keyup", isEmailFieldValid)