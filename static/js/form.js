//Reservation-Form-Validation AND Submit

const button = document.querySelector(".submitBtn");
const form = document.forms[0];
let name = document.querySelector("#name");
let phone = document.querySelector("#phone");
let pet = document.querySelectorAll('#pet');
let service = document.querySelectorAll("#service");
let time = document.querySelectorAll("#time");
let postcode = document.querySelector("#postcode");
let detailaddr = document.querySelector("#detailaddress");
const pattern_spc = /[~!@#$%^&*()_+|<>?:{}]/;
const pattern_num = /[0-9]/;
const pattern_eng = /[a-zA-Z]/;
const pattern_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;

button.addEventListener('click', () => {

    if (checkName() && checkPhone() && checkChecked() && checkAddr()) {
        toSubmit();
    }
});

function checkName() {
    const nameValue = name.value;
    //입력안하면 false
    if (nameValue == '') {
        alert("이름을 입력해주세요.");
        return false;
    }
    //특수문자나 숫자 입력하면 false
    if (pattern_spc.test(nameValue) || pattern_num.test(nameValue)) {
        alert("이름을 올바른 형식으로 입력해주세요.");
        return false;
    }
    return true;
}

function checkPhone() {
    let phoneValue = phone.value;
    //입력안하면 false
    if (phoneValue == '' || phoneValue.length < 10 || phoneValue.length > 12) {
        alert("전화번호 10~11자리를 입력해주세요.");
        return false;
    }
    //숫자 외에 입력하면 false
    if (pattern_spc.test(phoneValue) || pattern_eng.test(phoneValue) || pattern_kor.test(phoneValue)) {
        alert("전화번호에 숫자만 입력해주세요.");
        return false;
    }
    //10자리와 11자리인 경우 
    return checkPhoneValue(phoneValue);
}

function checkPhoneValue(phoneValue) {
    let len = phoneValue.length;
    let first = phoneValue.substring(0, 3);
    if (len == 10) {
        if (!(first === '011')) {
            alert("전화번호를 다시 입력해주세요.");
            return false;
        }
    } else if (len == 11) {
        if (!(first === '010')) {
            alert("전화번호를 다시 입력해주세요.");
            return false;
        }
    }
    return true;
}

function checkChecked() {
    //체크박스를 모두 체크하지 않은 경우
    if (!(checkCheckedTrue(pet)) || !(checkCheckedTrue(service)) || !(checkCheckedTrue(time))) {
        alert("모든 항목을 선택해주세요.");
        return false;
    }
    return true;
}

function checkCheckedTrue(items) {
    for (let i = 0; i < items.length; i++) {
        if (items[i].checked == true) {
            return true;
        }
    }
    return false;
}

function checkAddr() {
    const postValue = postcode.value;
    const detailaddrValue = detailaddr.value;
    if (!postValue) {
        alert("주소를 입력해주세요.");
        return false;
    } else if (!detailaddrValue) {
        alert("상세주소를 입력해주세요.");
        return false;
    }

    return true;
}

function toSubmit() {

    const form = document.form;
    form.submit();

};
