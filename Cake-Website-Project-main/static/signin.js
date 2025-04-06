const apiver = 1;

let login_button = document.getElementById('regBtn');
login_button.addEventListener("click",function(){
  console.log("fired");

  let email_value = document.getElementById("email").value;
  let password_value = document.getElementById("password").value;
  let username_value = document.getElementById("user").value;

  if( email_value == "" || password_value == "" || username_value == "" ){
    console.log("Not valid...")
    return;
  }

  fetch(`/api/v${apiver}/sign-up`, {
    method: "POST",
    body: JSON.stringify({
      email: email_value,
      password: password_value,
      username: username_value,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
});