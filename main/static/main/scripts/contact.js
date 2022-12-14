const nameField = document.querySelector(".js-name-input")
const emailField = document.querySelector(".js-email-input")
const msgField = document.querySelector(".js-msg-input")
const NAME_REGEX_PATTERN = /^([a-z]|[A-Z])\w{4,}$/
const EMAIL_REGEX_PATTERN = /^[a-z]\w{2,}@\w{2,}\.\w{2,}$/

const isContactFormValid = () => {
    const isValid = (isEmailFieldValid() & isNameFieldValid() & isMsgFieldValid()) === 0 ? false : true
    return isValid
}

const isNameFieldValid = () => {
    const errorHolder = nameField.closest(".js-input-container").querySelector(".js-error-holder")
    if(nameField.value.trim() === ""){
        errorHolder.textContent = "اسم المستخدم مطلوب"
        return false
    }
    if(!NAME_REGEX_PATTERN.test(nameField.value)){
        errorHolder.textContent = "يرجى ادخال اسم مستخدم صحيح مكون من 5 حروف و ارقام و _ فقط ، بشرط ان يبدء بحرف"
        return false
    }
    errorHolder.textContent = ""
    return true
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

const isMsgFieldValid = () => {
    const errorHolder = msgField.closest(".js-input-container").querySelector(".js-error-holder")
    if(msgField.value.trim() === ""){
        errorHolder.textContent = "الرسالة مطلوبة"
        return false
    }
    errorHolder.textContent = ""
    return true
}

nameField.addEventListener("keyup", isNameFieldValid)
emailField.addEventListener("keyup", isEmailFieldValid)
msgField.addEventListener("keyup", isMsgFieldValid)